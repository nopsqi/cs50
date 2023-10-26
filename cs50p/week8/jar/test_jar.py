from jar import Jar
import pytest


def test_init():
    jar = Jar(25)
    assert jar.capacity == 25
    assert jar.size == 0


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(5)
    assert jar.size == 5
    with pytest.raises(ValueError):
        jar.deposit(50)


def test_withdraw():
    jar = Jar()
    jar.deposit(5)
    jar.withdraw(1)
    assert jar.size == 4
    with pytest.raises(ValueError):
        jar.withdraw(50)
