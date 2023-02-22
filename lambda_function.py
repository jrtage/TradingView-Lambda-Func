import json
import balance
import liveprice
import trade

# Declare which chart to grab live price info from
assetChart = 'ethusd'

def long():
    bal = balance.balances('USD')
    currentPrice = liveprice.currentPrice(assetChart)
    maxAsset = (bal/currentPrice) * 0.99
    if maxAsset > 10:
        maxAsset = 10

    trade.execTrade(assetChart, 'buy', maxAsset)

def short():
    bal = balance.balances('ETH')
    if bal == None:
        return

    trade.execTrade(assetChart, 'sell', 1)

def lambda_handler(event, context):
    print("Hello, World!")
    return {
        'statusCode': 200
    }

short()