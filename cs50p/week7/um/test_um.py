from um import count


def test_lowercase():
    assert count("um") == 1
    assert count("thanks, um...") == 1


def test_uppercase():
    assert count("Um?") == 1
    assert count("Um, thanks, um...") == 2


def test_substring():
    assert count("Um, thanks for the album") == 1