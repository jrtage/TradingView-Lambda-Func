import math
from trade import execTrade
from balance import balances

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
    if balances('USD') < positionFunds:
        print('Insufficient funds for this position')
        return

    execTrade(assetChart, 'buy', maxAsset, price)

def short(price, assetChart, asset):
    bal = balances(asset)
    if bal < 0.01:
        print('No Assets Available To Sell')
        return

    execTrade(assetChart, 'sell', bal, price)