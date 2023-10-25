import pytest
from working import convert


def test_with_minute():
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_without_minute():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_mix():
    assert convert("9:00 AM to 5 PM") == "09:00 to 17:00"


def test_not_in_range():
    with pytest.raises(ValueError):
        convert("10:63 AM to 5:00 PM")
    with pytest.raises(ValueError):
        convert("14:63 AM to 5:00 PM")
