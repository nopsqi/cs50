from um import count


def test_lowercase():
    assert count("um") == 1
    assert count("thanks, um...") == 1


def test_mix():
    assert count("Um?") == 1
    assert count("Um, thanks for the album") == 1
    assert count("Um, thanks, um...") == 2