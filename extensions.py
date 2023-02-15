import json
import requests
from currency_token import keys

class APIException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Cannot be converted. You use the same currency {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'{quote} currency cannot be calculated')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'{base} currency cannot be calculated')

        try:
            amount = float(amount)
        except KeyError:
            raise APIException(f'{amount} amount cannot be calculated')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base