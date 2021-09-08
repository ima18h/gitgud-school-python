from calculator import add, divide, factorial, sin
import pytest
from math import pi, sqrt


@pytest.mark.parametrize("arg, arg1, output", [(1, 2, 3), (0.1, 0.2, pytest.approx(0.3))])
def test_add(arg, arg1, output):
    assert add(arg, arg1) == output

@pytest.mark.parametrize("arg, arg1, output", [(4, 2, 2), (1, 3, pytest.approx(0.3333333333333333))])
def test_divide(arg, arg1, output):
    assert divide(arg, arg1) == output

@pytest.mark.parametrize("arg, output", [(1, 1), (2, 2), (3, 6), (5, 120), (0, 1)])
def test_factorial(arg, output):
    assert factorial(arg) == output

# TODO: wtf?
@pytest.mark.parametrize("arg, output", [(sin(0), pytest.approx(0))])
def test_sin(arg, output):
    assert sin(arg) == output
    assert sin(pi/4) == pytest.approx(1/sqrt(2))
    assert sin(pi/2) == pytest.approx(1)
    assert sin(3*pi/2) == pytest.approx(-1)

def test_is_float_raises_ValueError_for_string_arguments():
    with pytest.raises(ValueError):
        factorial(-1)

def test_factorial_raises_TypeError():
    with pytest.raises(TypeError):
        factorial(1/3)

def test_divide_raises_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)
