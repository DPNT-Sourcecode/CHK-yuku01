# noinspection PyUnusedLocal
# skus = unicode string
import logging

# DB tables mock
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
OFFERS = {
    'A': {'count': 3, 'price': 130},
    'B': {'count': 2, 'price': 45},
}


def checkout(skus: str) -> int:
    if not skus.isalpha() or not skus.isupper():
        return -1

    amount = 0
    for item in set(skus):
        if item not in PRICES:
            logging.warning(f'Product {item} not in DB')
            return -1

        products_n = skus.count(item)
        discount_price = 0
        if item in OFFERS:
            discount_price = (
                (products_n // OFFERS[item]['count']) * OFFERS[item]['price']
            )
            products_n = products_n % OFFERS[item]['count']

        amount += PRICES[item] * products_n + discount_price

    return amount


