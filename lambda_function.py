import json
import balance
import liveprice
import trade
import math

# Declare which chart to grab live price info from
assetChart = 'ethusd'

def long(price):
    bal = balance.balances('USD')
    #currentPrice = liveprice.currentPrice(assetChart)
    maxAsset = 1500/price
    maxAsset = math.floor(maxAsset * 1000000) / 1000000
    #if maxAsset > 1:
    #    maxAsset = 1

    trade.execTrade(assetChart, 'buy', maxAsset, price)

def short(price):
    bal = balance.balances('ETH')
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
