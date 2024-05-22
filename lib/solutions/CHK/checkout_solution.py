# noinspection PyUnusedLocal
# skus = unicode string
import logging


DISCOUNT_TYPE = dict[str, dict[str, int]]

# DB tables mock
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
# SQL can be like "SELECT ... FROM offers WHERE ... ORDER BY discount DESC"
OFFERS = {
    'A': [
        {'count': 5, 'item': 'A', 'discount': 50},
        {'count': 3, 'item': 'A', 'discount': 30},
    ],
    'B': [
        {'count': 2, 'item': 'E', 'price': 30},
        {'count': 2, 'item': 'B', 'price': 15},
    ],
}


def get_discount(item: str, n: int) -> DISCOUNT_TYPE:
    """

    """
    discount_prices = {}
    for offer in OFFERS[item]:
        applies = n // offer['count']
        if offer['item'] not in discount_prices:
            discount_prices[offer['item']] = {'discount': 0, 'count': 0}

        discount_prices[offer['item']]['discount'] += applies * offer['price']
        discount_prices[offer['item']]['count'] += applies * offer['count']
        n = n % offer['count']

    return discount_prices


def apply_discount(applied: DISCOUNT_TYPE, new: DISCOUNT_TYPE) -> DISCOUNT_TYPE:
    """

    """
    for item, new_discount in new.items():
        if item in applied:
            ...
        else:
            applied[item] = new_discount

    return applied


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
    total_discount = {}
    for item in set(skus):
        if item not in PRICES:
            logging.warning(f'Product {item} not in DB')
            return -1

        products_n = skus.count(item)
        item_discounts = get_discount(item, products_n)


        amount += PRICES[item] * products_n

    return amount - total_discount
