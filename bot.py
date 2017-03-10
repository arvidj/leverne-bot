import os
import logging
import asyncio

from random import randint, choice
import re
import math
from util import chunk

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


# Note: commands have priority: the first matching one will be executed.

@bot.command(r'^/lennart (.*)')
def lennart_search(chat, match):
    logger.info("grace of mantis (%s), search (%s)", chat.sender, match.group(1))
    quote = get_lennart_quote(match.group(1))
    return chat.send_text("Hmm... intressant." if quote == None else quote)

@bot.command(r'/lennart')
def lennart(chat, match):
    logger.info("grace of mantis (%s)", chat.sender)
    return chat.send_text(get_lennart_quote())

def get_lennart_quote(query=None):
    s = open("lb.txt", 'rb').read().decode('utf-8', 'ignore')
    # split on punctuation
    lines = re.split("([!.?]+)", s)
    # join again to get complete phrases
    linesp = [''.join(i) for i in chunk(lines, 2)]

    if query != None:
        linesp = [i for i in linesp if i.lower().find(query.lower()) > -1]

    return choice(linesp).strip() if linesp else None

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s')
    logger.info("start")

    bot.run()
