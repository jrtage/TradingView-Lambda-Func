import json
import balance
import trade
import math
import setChart

# Declare which chart to grab live price info from
assetPrecision = 6
numOfCharts = 1
assetLimit = 10
usdBal = 1500
positionFunds = usdBal / numOfCharts


def long(price, assetChart):
    maxAsset = positionFunds /price
    maxAsset = math.floor(maxAsset * (10 ** assetPrecision)) / (10 ** assetPrecision)
    if maxAsset > assetLimit:
        maxAsset = assetLimit
    if balance.balances('USD') < positionFunds:
        print('Insufficient funds for this position')
        return

    trade.execTrade(assetChart, 'buy', maxAsset, price)

def short(price, assetChart, asset):
    bal = balance.balances(asset)
    if bal < 0.01:
        print('No Assets Available To Sell')
        return

    trade.execTrade(assetChart, 'sell', bal, price)

def lambda_handler(event, context):
    body = event['body']
    body_json = json.loads(body)
    price = float(body_json['price'])
    assetChart, asset =  setChart(body_json['ticker'])
    if body_json['strategy'] == 'buy':
        long(price, assetChart)
    if body_json['strategy'] == 'sell':
        short(price, assetChart, asset)
