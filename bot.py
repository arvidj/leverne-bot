import os
import logging
import asyncio

from random import randint, choice, sample
import re
import math
import json
from util import chunk

from aiotg import Bot

bot = Bot(
    api_token=os.environ.get("API_TOKEN"),
    name=os.environ.get("BOT_NAME")
)
logger = logging.getLogger("levernebot")

thxm8Regexp = r'(^| )([Tt][Aa][Cc][Kk])( |$|[\.\?!])'
@bot.command(thxm8Regexp)
def do_correct_thx(chat, match):
    logger.info("one person (%s) thanked", chat.sender)
    used = match.group(2)
    correction = "Tacka ja till allt, tacka inte för något."
    return chat.send_text(correction)

# # if someone uses de/dem, correct them.
# deDemRegexp = r'(^| )([Dd]e(m?))( |$|[\.\?!])'
# @bot.command(deDemRegexp)
# def do_correct(chat, match):
#     logger.info("one person (%s) corrected", chat.sender)
#     used = match.group(2)
#     correction = "*" +  ("de" if used == "dem" else "dem")
#     return chat.send_text(correction)

# # if someone uses hon/han, correct them.
# hanHonRegexp = r'(^| )([Hh][oa]n)( |$|[\.\?!])'
# @bot.command(hanHonRegexp)
# def do_correct_hen(chat, match):
#     logger.info("one person (%s) han/hon corrected", chat.sender)
#     used = match.group(2)
#     correction = "*hen"
#     return chat.send_text(correction)

# Note: commands have priority: the first matching one will be executed.

@bot.command(r'^/lennart (.*)')
def lennart_search(chat, match):
    logger.info("grace of mantis (%s), search (%s)", \
               chat.sender, match.group(1))
    quote = get_lennart_quote(match.group(1))
    return chat.send_text("Hmm... intressant." if quote == None else quote)

@bot.command(r'/lennart')
def lennart(chat, match):
    logger.info("grace of mantis (%s)", chat.sender)
    return chat.send_text(get_lennart_quote())

def get_lennart_quote(query=None):
    s = open("lb.txt", 'rb').read().decode('utf-8', 'ignore')
    linesp = matching_lines(s, query)
    return choice(linesp).strip() if linesp else None

def matching_lines(s, query):
    # split on punctuation
    lines = re.split("([!.?]+)", s)
    # join again to get complete phrases
    linesp = [''.join(i) for i in chunk(lines, 2)]

    if query != None:
        linesp = [i for i in linesp if i.lower().find(query.lower()) > -1]

    return linesp

@bot.command(r'^/danne (.*)')
def danne_search(chat, match):
    logger.info("danne (%s), search (%s)", chat.sender, match.group(1))
    s = get_danne_blog(match.group(1))
    return chat.send_text(s)

@bot.command(r'/danne')
def danne(chat, match):
    logger.info("champagne (%s)", chat.sender)
    return chat.send_text(get_danne_blog())

def get_danne_blog(query=None):
    blog = json.load(open("danne.json"))
    if query == None:
        entry = choice(blog)
        return format_danne_blog(entry)
    else:
        # select all blogs matching query
        # run matching lines
        entries = [s for s in blog if query.lower() in s['body'].lower()]

        lines =[l.strip() for s in entries
                   for l in matching_lines(s['body'], query)]

        # choice 10 lines
        limit = 10
        lines = sample(lines, limit) if len(lines) > limit else lines

        return ("Kram." if lines == [] else "\n".join(lines))

def format_danne_blog(entry):
    return "{}\n\n{}".format(entry['title'].strip(), entry['body'].strip())

catanRegexp = r'(^| )(malm|ull|trä|korn|lera)( |$|[\.\?!])'
@bot.command(catanRegexp)
def catan(chat, match):
    logger.info("catan (%s): (%s)", chat.sender, match.group(1))
    return chat.send_text('WALL STREET!')

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s')
    logger.info("start")

    bot.run()
