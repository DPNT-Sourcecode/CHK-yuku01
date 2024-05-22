# noinspection PyUnusedLocal
# skus = unicode string


# DB tables mock
PRICES = {'A': 50, 'B': 30, 'C': 20, 'D': 15}
OFFERS = {'A': {3: 130}, 'B': {2: 45}}


def checkout(skus: str) -> int:
    if not skus.isalpha() or not skus.isupper():
        return -1
    amount = 0
    for item in

    return amount

