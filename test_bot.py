import pytest
import re
import json
from random import randint, choice

from bot import deDemRegexp, get_lennart_quote, lennart, lennart_search, get_danne_blog, format_danne_blog, danne, catan, catanRegexp

# Mock objects

class MockChat:
    sender = "test"
    should_receive = None
    def __init__(self, should_receive):
        self.should_receive = should_receive

    def send_text(self, t):
        print(t)
        print(self.should_receive)
        assert re.match(self.should_receive, t)


# Unit tests

def test_deDemRegexp():
    assert re.search(deDemRegexp, "var tycker dem du detta har")
    assert re.search(deDemRegexp, "dem!")
    assert re.search(deDemRegexp, "de!")
    assert re.search(deDemRegexp, "de?")
    assert re.search(deDemRegexp, "dem?")
    assert (not (re.search(deDemRegexp, "detta!")))
    assert (not (re.search(deDemRegexp, "detta tycker jag om")))

def test_get_lennart_quote():
    assert isinstance(get_lennart_quote(), str)
    assert isinstance(get_lennart_quote("mantis"), str)
    s = ("And I think we have a really good chance to do it together with " +
         "Campus Gotland and Uppsala University who has a lots of skills together now.")
    assert s == get_lennart_quote("campus")

def test_lennart():
    # chat = mocker.stub(name='')
    chat = MockChat(r'.*')
    lennart(chat, None)


def test_lennart_search():
    chat = MockChat(r'(?i).*mantis.*')
    lennart_search(chat, re.match('^/lennart (.*)', '/lennart mantis'))

    chat = MockChat(r'Hmm\.\.\..*')
    lennart_search(chat, re.match('^/lennart (.*)', '/lennart lskdflksdjflksjdfkljsk'))

def test_get_danne_blog():
    assert isinstance(get_danne_blog(), str)

def test_catan():
    assert re.search(catanRegexp, "Vill du köpa trä?")
    assert re.search(catanRegexp, "Vill du malm köpa?")

    m = re.search(catanRegexp, "Vill du malm köpa?")
    chat = MockChat(r'WALL STREET!')
    catan(chat, m)

def test_lennart():
    # chat = mocker.stub(name='')
    chat = MockChat(r'.*')
    danne(chat, None)
