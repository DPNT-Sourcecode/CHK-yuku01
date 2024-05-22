import pytest

from lib.solutions.CHK.checkout_solution import checkout


@pytest.mark.parametrize(
    'products,output',
    (
        ('', 0),
        ('B', 30),
        ('ABCDEF', 165),
        ('AAA', 130),
        ('AAAAAA', 250),
        ('AAAA', 180),
        ('AAABB', 175),
        ('BBEE', 110),
        ('BBBEE', 125),
        ('BBBEEEE', 190),
        ('AAAAAAAA', 330),
        ('FFF', 20),
        ('FFFFF', 40),
        ('FFFFFF', 40),
        ('BBBEEFF', 145),
        ('BBBEEFFF', 145),
        ('H'*15, 125),
        ('KKMNNN', 270),
        ('PPPPPQQQQRRR', 200+80+150),
        ('UUUUVVVVV', 340),
    ),
)
def test_checkout_success(products, output):
    assert checkout(products) == output


@pytest.mark.parametrize(
    'products',
    ('ab', 'AB4', 'A B C D', 4),
)
def test_checkout_error(products):
    assert checkout(products) == -1

