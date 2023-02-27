# CURRENTLY DEPRECATED FROM CODEBASE
#PRICE DATA BEING USED IS BEING PASSED IN FROM TRADINGVIEW

import requests
import api



def currentPrice(symbol):
    endpoint = api.priceEndpoint(symbol)
    # Send the request and get the response
    response = requests.get(endpoint)
    data = response.json()

    # Extract the ETH price from the response
    price = float(data['last'])
    return price