import pytest
from seasons import convert


def test_one_years_ago():
    assert convert("2022-10-26") == "Five hundred twenty-five thousand, six hundred minutes"

def test_two_years_ago():
    assert convert("2021-10-26") == "One million, fifty-one thousand, two hundred minutes"

def test_invalid_format():
    with pytest.raises(SystemExit):
        assert convert("July 3, 2020")
