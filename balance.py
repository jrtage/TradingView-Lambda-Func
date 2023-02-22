import json
import requests
import hmac
import hashlib
import base64
import time
import api

# Send the request and print the response
def balances(currencySymbol):

    # Set the API endpoint and request parameters
    nonce = str(int(time.time() * 1000))
    payload = {'request': '/v1/balances', 'nonce': nonce}

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

    asset_balance = None
    response = requests.post(api.keys['balUrl'], headers=headers)
    if response.status_code == 200:
        try:
            response_json = response.json()
            for balance in response_json:
                if balance['currency'] == currencySymbol:
                    asset_balance = float(balance['available'])
                    return asset_balance
        except ValueError:
            print('Error: Empty response')
    else:
        print(f'Error: Request failed with status code {response.status_code}')
        print(response.content)