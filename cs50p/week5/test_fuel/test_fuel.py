import pytest
from fuel import convert, gauge


def test_convert():
    assert convert("3/4") == 75
    assert convert("2/2") == 100
    assert convert("0/3") == 0
    with pytest.raises(ValueError):
        