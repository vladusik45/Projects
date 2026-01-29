import pytest
from calc import Calculator


@pytest.fixture
def calc():
    return Calculator()


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),
        (-1, 1, 0),
        (0, 0, 0),
        (2.5, 1.5, 4.0)
    ]
)
def test_add(calc, a, b, expected):
    assert calc.add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),
        (0, 5, -5),
        (-2, -2, 0)
    ]
)
def test_subtract(calc, a, b, expected):
    assert calc.subtract(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),
        (-2, 3, -6),
        (0, 10, 0)
    ]
)
def test_multiply(calc, a, b, expected):
    assert calc.multiply(a, b) == expected


def test_divide(calc):
    assert calc.divide(10, 2) == 5


def test_divide_by_zero(calc):
    with pytest.raises(ZeroDivisionError):
        calc.divide(10, 0)


@pytest.mark.parametrize(
    "number, expected",
    [
        (2, True),
        (3, True),
        (1, False),
        (0, False),
        (-7, False),
        (17, True),
        (18, False)
    ]
)
def test_is_prime_number(calc, number, expected):
    assert calc.is_prime_number(number) == expected
