import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize(
    'products,output',
    (
        ('', 0),
        ('B', 30),
        ('ABCDE', 155),
        ('AAA', 130),
        ('AAAAAA', 250),
        ('AAAA', 180),
        ('AAABB', 175),
        ('BBEE', 110),
        ('BBBEE', 125),
        ('AAAAAAAA', 330),
    ),
)
def test_checkout_success(products, output):
    assert checkout(products) == output


@pytest.mark.parametrize(
    'products',
    ('Z', 'ab', 'AB4', 'A B C D', 4),
)
def test_checkout_error(products):
    assert checkout(products) == -1

