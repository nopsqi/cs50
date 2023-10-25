from numb3rs import validate


def test_localhost():
    assert validate("127.0.0.1") == True


def test_subnet():
    assert validate("255.255.255.255)