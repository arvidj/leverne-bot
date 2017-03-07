import os
import logging
# import pymongo
import asyncio
import json
import math

from datetime import timedelta
from aiotg import Bot

with open("config.json") as cfg:
    config = json.load(cfg)

bot = BotBot(
    api_token=os.environ.get("API_TOKEN"),
    name=os.environ.get("BOT_NAME"),
    botan_token=os.environ.get("BOTAN_TOKEN")
)
         (**config)
logger = logging.getLogger("musicbot")


# if someone uses de/dem, correct them.
deDemRegexp = r'(^| )de(m?)( |$|[\.\?!])'
@bot.command(deDemRegexp)
def usage(chat, match):
    logger.info("one person (%s) corrected", chat.sender)
    return chat.send_text("*dom")


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)

    bot.run()
