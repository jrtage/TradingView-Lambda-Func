import json
import balance
import liveprice
import trade

# Declare which chart to grab live price info from
assetChart = 'ethusd'

def long(price):
    bal = balance.balances('USD')
    currentPrice = liveprice.currentPrice(assetChart)
    maxAsset = (bal/currentPrice) * 0.99
    if maxAsset > 10:
        maxAsset = 10

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

long(liveprice.currentPrice(assetChart))