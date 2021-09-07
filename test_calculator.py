from calculator import add
from pytest import approx
from math import pi, sqrt


def test_add():
    assert add(1, 2) == 3
    assert add(0.1, 0.2) == approx(0.3)

def test_divide():
    assert divide(4, 2) == 2
    assert divide(1, 3) == approx(0.333333)

def test_factorial():
    assert factorial(5) == 120
    assert factorial(1) == 1
    assert factorial(2) == 2

def test_sin():
    assert sin(0) == approx(pi/4)
    assert sin(pi/4) == approx(1/sqrt(2))
    assert sin(pi/2) == approx(1)
    assert sin(3*pi/2) == approx(-1)

