import json
import requests
import hmac
import hashlib
import base64
import time
import balance
import liveprice


def long():
    bal = balance.balances('USD')
    currentPrice = liveprice.currentPrice('ethusd')
    maxAsset = bal/currentPrice
    if maxAsset <= 10:
        pass
    else:
        pass

def short():
    pass

def lambda_handler(event, context):
    print("Hello, World!")
    return {
        'statusCode': 200
    }