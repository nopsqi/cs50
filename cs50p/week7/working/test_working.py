import pytest
from working import convert


def test_with_minute():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_without_minute():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mix():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"


def test_error_hour():
    with pytest.raises(ValueError):
        convert("13 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("10:00 AM to 15:43 PM")


def test_error_minute():
    with pytest.raises(ValueError):
        convert("7:63 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("10:00 AM to 4:76 PM")
