from numb3rs import validate


def test_localhost():
    assert validate("127.0.0.1") == True


def test_subnet():
    assert validate("255.255.255.255") == True


def test_overflow():
    assert validate("512.512.512.512") == False


def test_overflow1():
    assert validate("1.2.3.1000") == False


def test_overflow2():
    assert validate("1000") == False


def test_word():
    assert validate("cat") == False