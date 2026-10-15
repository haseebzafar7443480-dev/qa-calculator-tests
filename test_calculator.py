import pytest
from calculator import add, subtract, multiply, divide


def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-2, -3) == -5


def test_subtract():
    assert subtract(10, 4) == 6


def test_multiply():
    assert multiply(3, 4) == 12


def test_multiply_by_zero():
    assert multiply(5, 0) == 0


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)


@pytest.mark.parametrize("a, b, expected", [
    (1, 1, 2),
    (0, 0, 0),
    (100, -50, 50),
    (0.1, 0.2, pytest.approx(0.3)),
])
def test_add_many_cases(a, b, expected):
    assert add(a, b) == expected
