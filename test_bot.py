import pytest
import re

from bot import deDemRegexp

def test_deDemRegexp():
    assert re.search(deDemRegexp, "var tycker dem du detta har")
    assert re.search(deDemRegexp, "dem!")
    assert re.search(deDemRegexp, "de!")
    assert re.search(deDemRegexp, "de?")
    assert re.search(deDemRegexp, "dem?")
    assert (not (re.search(deDemRegexp, "detta!")))
    assert (not (re.search(deDemRegexp, "detta tycker jag om")))
