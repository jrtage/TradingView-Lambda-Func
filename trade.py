import json
import requests
import hmac
import hashlib
import base64
import time
import api


def execTrade(sym, exec, tradeVal):
    # Set your API credentials
    api_key = api.apiKey()
    api_secret = api.apiSecret()


    # Set the Sandbox API endpoint and request parameters
    endpoint = api.balEndpoint()
    nonce = str(int(time.time() * 1000))
    symbol = sym #'ethusd'
    amount = tradeVal
    side = exec #'buy/sell'
    order_type = 'exchange market'

    # Set the order payload
    payload = {
        'request': '/v1/order/new',
        'nonce': nonce,
        'symbol': symbol,
        'amount': amount,
        'side': side,
        'type': order_type,
    }

    # Generate the signature using the payload and API secret
    payload_json = json.dumps(payload)
    payload_b64 = base64.b64encode(payload_json.encode('utf-8'))
    signature = hmac.new(api_secret.encode(), payload_b64, hashlib.sha384).hexdigest()

    # Set the headers for the request
    headers = {
        'Content-Type': 'text/plain',
        'Content-Length': '0',
        'X-GEMINI-APIKEY': api_key,
        'X-GEMINI-PAYLOAD': payload_b64,
        'X-GEMINI-SIGNATURE': signature
    }

    # Send the request and print the response
    response = requests.post(endpoint, headers=headers)
    print(response.json())