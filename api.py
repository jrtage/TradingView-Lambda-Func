keys = {
    'api': 'API Key Here',
    'secret': b'Secret Key Here',
    'balUrl': 'https://api.sandbox.gemini.com/v1/balances',
    'tradeUrl': 'https://api.sandbox.gemini.com/v1/order/new',
    'priceUrl': 'https://api.gemini.com/v1/pubticker/'
}

def priceEndpoint(symbol):
    url = keys['priceUrl'] + symbol
    return url