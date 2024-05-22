# noinspection PyUnusedLocal
# skus = unicode string
import logging
from collections import Counter


DISCOUNT_TYPE = dict[str, dict[str, int]]

# DB tables mock
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
# SQL can be like "SELECT ... FROM offers WHERE product_in in ... ORDER BY discount DESC"
OFFERS = [
    {'condition': [('A', 5)], 'discount': 50},
    {'condition': [('A', 3)], 'discount': 30},
    {'condition': [('B', 1), ('E', 2)], 'discount': 30},
    {'condition': [('B', 2)], 'discount': 15},
]


def get_discount(items: dict[str, int]) -> int:
    """

    """
    discount = 0
    for offer in OFFERS:
        applies = {
            item: items[item] // n
            for item, n in offer['condition']
        }
        min_applies = min(applies.values())
        if min_applies > 0:
            discount += offer['discount'] * min_applies
            left = {
                item: items[item] % n
                for item, n in offer['condition']
            }
            items.update(left)

    return discount


def checkout(skus: str) -> int:
    """
    Calculates amount of received checkout.

    :param skus: the SKUs of all the products in the basket
    :return: total checkout value of the items
      or -1 if "skus" parameter is wrong
    """
    if (
        not isinstance(skus, str)
        or skus and (not skus.isalpha() or not skus.isupper())
    ):
        return -1

    amount = 0
    items = Counter(skus)
    for item in set(skus):
        if item not in PRICES:
            logging.warning(f'Product {item} not in DB')
            return -1

        amount += PRICES[item] * items[item]

    total_discount = get_discount(items)

    return amount - total_discount

