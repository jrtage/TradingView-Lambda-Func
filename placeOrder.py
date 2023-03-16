import math
from trade import execTrade
from balance import balances
import dbTrans

# Declare which chart to grab live price info from
assetPrecision = 6
numOfCharts = 1
assetLimit = 1
usdBal = 1400
positionFunds = usdBal / numOfCharts


def long(price, assetChart, time):
    maxAsset = positionFunds /price
    maxAsset = math.floor(maxAsset * (10 ** assetPrecision)) / (10 ** assetPrecision)
    if maxAsset > assetLimit:
        maxAsset = assetLimit
    if balances('USD') < positionFunds:
        print('Insufficient funds for this position')
        return

    response = execTrade(assetChart, 'buy', maxAsset, price)


    # Write trade amt, cost, chart, and timestamp to database
    dbTrans.buyOrder(assetChart, time, response)
    #
    #

def short(price, assetChart, asset, time):
    print('checking Balance for ' + asset + '....')
    bal = balances(asset)
    bal = math.floor(bal * (10 ** assetPrecision)) / (10 ** assetPrecision)
    print(bal)
    if bal < 0.001:
        print('No Assets Available To Sell')
        return

    #Read most recent entry from database for specific asset
    #Read bool flag for if that position has been sold yet
    tradeAmt = dbTrans.sellOrder(assetChart, time)
    tradeAmt = math.floor(tradeAmt * (10 ** assetPrecision)) / (10 ** assetPrecision)

    execTrade(assetChart, 'sell', tradeAmt, price)