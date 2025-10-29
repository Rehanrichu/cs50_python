import pytest
from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    jar2 = Jar(5)
    assert jar2.capacity == 5
    assert jar2.size == 0

    # invalid capacities
    with pytest.raises(ValueError):
        Jar(-1)
    with pytest.raises(ValueError):
        Jar("ten")
    with pytest.raises(ValueError):
        Jar(3.5)


def test_str():
    jar = Jar(10)
    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪"

    jar.deposit(2)
    assert str(jar) == "🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar(4)
    jar.deposit(2)
    assert jar.size == 2

    # deposit up to capacity
    jar.deposit(2)
    assert jar.size == 4

    # exceeding capacity
    with pytest.raises(ValueError):
        jar.deposit(1)

    # invalid deposits
    with pytest.raises(ValueError):
        jar.deposit(-1)
    with pytest.raises(ValueError):
        jar.deposit(1.5)


def test_withdraw():
    jar = Jar(6)
    jar.deposit(4)
    jar.withdraw(1)
    assert jar.size == 3
    assert str(jar) == "🍪🍪🍪"

    # withdrawing too many
    with pytest.raises(ValueError):
        jar.withdraw(5)

    # invalid withdrawals
    with pytest.raises(ValueError):
        jar.withdraw(-1)
    with pytest.raises(ValueError):
        jar.withdraw(1.5)