import os
import logging
import asyncio

from random import randint
import re
import math

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

@bot.command(r'/lennart')
def mantis(chat, match):
    logger.info("grace of mantis (%s)", chat.sender)
    return chat.send_text(get_lennart_quote())

def get_lennart_quote():
    s = open("lb.txt", 'rb').read().decode('utf-8', 'ignore')
    lines = re.split("([!.?]+)", s)
    i = randint(0, (math.floor(len(lines) / 2)) - 1)
    return (lines[2*i] + lines[2*i+1]).strip()

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    bot.run()
