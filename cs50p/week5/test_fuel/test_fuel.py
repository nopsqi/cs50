import pytest
from fuel import convert, gauge


def test_convert_normal():
    assert convert("3/4") == 75
    assert convert("2/2") == 100
    assert convert("0/3") == 0


def test_convert_error():
    with pytest.raises(ValueError):
        convert("cat/2")
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("dog/cat")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ZeroDivisionError):
        convert("0/0")


def test_gauge():
    assert gauge(100) == "F"
    assert gauge(75) == "75%"
    assert gauge(1) == "E"
    assert gauge(0) == "E"
    assert gauge(110) == None