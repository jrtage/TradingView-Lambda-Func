import json
import requests
import hmac
import hashlib
import base64
import time
import api
import liveprice


def execTrade(symbol, side, amount):
    # Set your API credentials
    api_key = api.apiKey()
    api_secret = api.apiSecret()


    # Set the Sandbox API endpoint and request parameters
    endpoint = api.tradeEndpoint()
    nonce = str(int(time.time() * 1000))
    price = (liveprice.currentPrice(symbol))
    if side == 'buy':
        price = price * 1.005
    if side == 'sell':
        price = price * 0.995
    order_type = 'exchange limit'

    # Set the order payload
    payload = {
        'request': '/v1/order/new',
        'nonce': nonce,
        'symbol': symbol,
        'amount': amount,
        'price': price,
        'side': side,
        'type': order_type,
    }

    # Generate the signature using the payload and API secret
    payload_json = json.dumps(payload)
    payload_b64 = base64.b64encode(payload_json.encode('utf-8'))
    signature = hmac.new(api_secret, payload_b64, hashlib.sha384).hexdigest()

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
    if response.status_code == 200:
        try: 
            print(response.json())
        except ValueError:
            print('Error: Empty response')
    else:
        print(f'Error: Request failed with status code {response.status_code}')
        print(response.content)