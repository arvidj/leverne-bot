import pytest
import re

from bot import deDemRegexp, get_lennart_quote

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
