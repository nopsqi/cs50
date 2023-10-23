from bank import value


def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hai") == 20
    assert value("hai") == 20
    assert value("What's up") == 100
    assert value("what's up") == 100