import json
import requests
import hmac
import hashlib
import base64
import time
import api


def execTrade(symbol, side, amount, price):
    # Set the Sandbox API endpoint and request parameters
    nonce = str(int(time.time() * 1000))
    price = round(price, 2)

    # Set the order payload
    payload = {
        'request': '/v1/order/new',
        'nonce': nonce,
        'symbol': symbol,
        'amount': amount,
        'price': price,
        'side': side,
        'type': 'exchange limit'
    }

    # Generate the signature using the payload and API secret
    payload_json = json.dumps(payload)
    payload_b64 = base64.b64encode(payload_json.encode('utf-8'))
    signature = hmac.new(api.keys['secret'], payload_b64, hashlib.sha384).hexdigest()

    # Set the headers for the request
    headers = {
        'Content-Type': 'text/plain',
        'Content-Length': '0',
        'X-GEMINI-APIKEY': api.keys['api'],
        'X-GEMINI-PAYLOAD': payload_b64,
        'X-GEMINI-SIGNATURE': signature
    }

    # Send the request and print the response
    response = requests.post(api.keys['tradeUrl'], headers=headers)
    if response.status_code == 200:
        try: 
            print(side, price)
            print(response.json())
            jsonResponse = response.json
            return(jsonResponse['original_amount'])
        except ValueError:
            print('Error: Empty response')
    else:
        print(f'Error: Request failed with status code {response.status_code}')
        print(response.content)