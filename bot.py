import os
import logging
import asyncio

from aiotg import Bot

bot = Bot(
    api_token=os.environ.get("API_TOKEN"),
    name=os.environ.get("BOT_NAME")
)
logger = logging.getLogger("levernebot")

# if someone uses de/dem, correct them.
deDemRegexp = r'(^| )(de(m?))( |$|[\.\?!])'
@bot.command(deDemRegexp)
def do_correct(chat, match):
    logger.info("one person (%s) corrected", chat.sender)
    used = match.group(2)
    correction = "*" +  ("de" if used == "dem" else "dem")
    return chat.send_text(correction)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    bot.run()
