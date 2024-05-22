# noinspection PyUnusedLocal
# skus = unicode string
import logging
from collections import Counter


# DB tables mock (it was better to collect it from task file)
PRICES = {
    'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40, 'F': 10, 'G': 20, 'H': 10,
    'I': 35, 'J': 60, 'K': 70, 'L': 90, 'M': 15, 'N': 40, 'O': 10, 'P': 50,
    'Q': 30, 'R': 50, 'S': 20, 'T': 20, 'U': 40, 'V': 50, 'W': 20, 'X': 17,
    'Y': 20, 'Z': 21,
}
# SQL can be like "SELECT ... FROM offers WHERE product_in in ... ORDER BY discount DESC"
OFFERS = [
    {'condition': [('A', 5)], 'discount': 50},
    {'condition': [('P', 5)], 'discount': 50},
    {'condition': [('U', 4)], 'discount': 40},
    {'condition': [('B', 1), ('E', 2)], 'discount': 30},
    {'condition': [('R', 3), ('Q', 1)], 'discount': 30},
    {'condition': [('A', 3)], 'discount': 20},
    {'condition': [('H', 10)], 'discount': 20},
    {'condition': [('K', 2)], 'discount': 20},
    {'condition': [('V', 3)], 'discount': 20},
    {'condition': [('Z', 3)], 'discount': 18},
    {'condition': [('Z', 2), ('S', 1)], 'discount': 17},
    {'condition': [('Z', 2), ('T', 1)], 'discount': 17},
    {'condition': [('Z', 2), ('Y', 1)], 'discount': 17},
    {'condition': [('Z', 1), ('S', 1), ('T', 1)], 'discount': 16},
    {'condition': [('Z', 1), ('S', 1), ('Y', 1)], 'discount': 16},
    {'condition': [('Z', 1), ('T', 1), ('Y', 1)], 'discount': 16},
    {'condition': [('Z', 1), ('S', 2)], 'discount': 16},
    {'condition': [('Z', 1), ('T', 2)], 'discount': 16},
    {'condition': [('Z', 1), ('Y', 2)], 'discount': 16},
    {'condition': [('B', 2)], 'discount': 15},
    {'condition': [('N', 3), ('M', 1)], 'discount': 15},
    {'condition': [('S', 1), ('T', 1), ('Y', 1)], 'discount': 15},
    {'condition': [('S', 3)], 'discount': 15},
    {'condition': [('T', 3)], 'discount': 15},
    {'condition': [('Y', 3)], 'discount': 15},
    {'condition': [('S', 2), ('Y', 1)], 'discount': 15},
    {'condition': [('S', 2), ('T', 1)], 'discount': 15},
    {'condition': [('Y', 2), ('S', 1)], 'discount': 15},
    {'condition': [('Y', 2), ('T', 1)], 'discount': 15},
    {'condition': [('T', 2), ('Y', 1)], 'discount': 15},
    {'condition': [('T', 2), ('S', 1)], 'discount': 15},
    {'condition': [('X', 1), ('Z', 2)], 'discount': 14},
    {'condition': [('X', 1), ('Z', 1), ('S', 1)], 'discount': 13},
    {'condition': [('X', 1), ('Z', 1), ('T', 1)], 'discount': 13},
    {'condition': [('X', 1), ('Z', 1), ('Y', 1)], 'discount': 13},
    {'condition': [('X', 1), ('S', 1), ('T', 1)], 'discount': 12},
    {'condition': [('X', 1), ('S', 1), ('Y', 1)], 'discount': 12},
    {'condition': [('X', 1), ('T', 1), ('Y', 1)], 'discount': 12},
    {'condition': [('X', 1), ('S', 2)], 'discount': 12},
    {'condition': [('X', 1), ('T', 2)], 'discount': 12},
    {'condition': [('X', 1), ('Y', 2)], 'discount': 12},
    {'condition': [('X', 2), ('Z', 1)], 'discount': 12},
    {'condition': [('F', 3)], 'discount': 10},
    {'condition': [('Q', 3)], 'discount': 10},
    {'condition': [('V', 2)], 'discount': 10},
    {'condition': [('X', 2), ('S', 1)], 'discount': 9},
    {'condition': [('X', 2), ('T', 1)], 'discount': 9},
    {'condition': [('X', 2), ('Y', 1)], 'discount': 9},
    {'condition': [('X', 3)], 'discount': 6},
    {'condition': [('H', 5)], 'discount': 5},
]


def get_discount(items: Counter) -> int:
    """
    Calculates max discount for checkout

    :param items: number of each item
    :return: maximum discount
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
                item: min_applies * n * -1
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
