keys = {
    'api': 'account-xVcci5i7ZOEjZQ05oGmY',
    'secret': b'44YWohaW9DhQM3gVEA6cndFQ9DhB',
    'balUrl': 'https://api.sandbox.gemini.com/v1/balances',
    'tradeUrl': 'https://api.sandbox.gemini.com/v1/order/new',
    'priceUrl': 'https://api.gemini.com/v1/pubticker/'
}

def priceEndpoint(symbol):
    url = keys['priceUrl'] + symbol
    return url