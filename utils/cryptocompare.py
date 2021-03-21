import cryptocompare


def get_price(from_coins: [str, list], to_coins: [str, list]):
    compare = cryptocompare.get_price(from_coins, to_coins)

    return compare
