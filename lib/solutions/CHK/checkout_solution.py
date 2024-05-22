# noinspection PyUnusedLocal
# skus = unicode string
import logging

# DB tables mock
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15, 'E': 40}
# SQL can be like "SELECT ... FROM offers WHERE ... ORDER BY count DESC"
OFFERS = {
    'A': [
        {'count': 5, 'item': 'A', 'discount': 20},
        {'count': 3, 'item': 'A', 'discount': 50},
    ],
    'B': [{'count': 2, 'item': 'B', 'price': 15}],
    'E': [{'count': 2, 'item': 'B', 'price': 30}],
}


def get_discount(item: str, n: int) -> dict:
    """

    """
    discount_price = {} # {'A': {'discount': 15, 'count': 5}}
    for offer in OFFERS[item]:
        if offer['item'] not in discount_price:
            discount_price[offer['item']] = {'discount': 0, 'count': 0}
        discount_price

    return


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
    total_discount = 0
    for item in set(skus):
        if item not in PRICES:
            logging.warning(f'Product {item} not in DB')
            return -1

        products_n = skus.count(item)

        amount += PRICES[item] * products_n

    return amount - total_discount
