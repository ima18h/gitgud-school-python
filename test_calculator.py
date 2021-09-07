from calculator import add
from pytest import approx


def test_add():
    assert add(1, 2) == 3

def test_add2():
    assert add(0.1, 0.2) == approx(0.3)

