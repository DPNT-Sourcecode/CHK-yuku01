import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize(
    'products,output',
    (
        ('B', 30),
        ('ABCD', 115),
        ('AAA', 130),
        ('AAAAAA', 260),
        ('AAAA', 180),
        ('AAABB', 175),
    ),
)
def test_checkout_success(products, output):
    assert checkout(products) == output


@pytest.mark.parametrize(
    'products',
    ('E', 'ab', 'AB4', 'A B C D', 4),
)
def test_checkout_error(products):
    assert checkout(products) == -1
