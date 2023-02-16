api = 'API KEY HERE'
secret = 'SECRET KEY HERE'
balUrl = 'https://api.sandbox.gemini.com/v1/balances'
tradeUrl = 'https://api.sandbox.gemini.com/v1/order/new'
priceUrl = 'https://api.gemini.com/v1/pubticker/'


def apiKey():
    return api

def apiSecret():
    return secret

def balEndpoint():
    return balUrl

def tradeEndpoint():
    return tradeUrl

def priceEndpoint(symbol):
    url = priceUrl + symbol
    return url