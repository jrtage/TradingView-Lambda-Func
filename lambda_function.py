import json
import balance
import trade
import math

# Declare which chart to grab live price info from
assetChart = 'ethusd'
asset = 'ETH'
assetPrecision = 6
tradeAmt = 750
assetLimit = 10

def long(price):
    maxAsset = tradeAmt/price
    maxAsset = math.floor(maxAsset * (10 ** assetPrecision)) / (10 ** assetPrecision)
    if maxAsset > assetLimit:
        maxAsset = assetLimit

    trade.execTrade(assetChart, 'buy', maxAsset, price)

def short(price):
    bal = balance.balances(asset)
    if bal < 0.01:
        print('No Assets Available To Sell')
        return

    trade.execTrade(assetChart, 'sell', bal, price)

def lambda_handler(event, context):
    body = event['body']
    body_json = json.loads(body)
    price = float(body_json['price'])
    if body_json['strategy'] == 'buy':
        long(price)
    if body_json['strategy'] == 'sell':
        short(price)
