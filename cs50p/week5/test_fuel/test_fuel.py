import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("