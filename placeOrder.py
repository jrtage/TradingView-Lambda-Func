import math
from trade import execTrade
from balance import balances

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

    tradeAmt = execTrade(assetChart, 'buy', maxAsset, price)

    # FIX THIS TO USE A DATABASE
    filename = './tmp/lasttrades/' + assetChart + time + '.txt'
    with open(filename, 'w') as file:
        file.write(tradeAmt)

def short(price, assetChart, asset, time):
    bal = balances(asset)
    if bal < 0.01:
        print('No Assets Available To Sell')
        return

    try:
        # FIX THIS TO USE A DATABASE
        filename = './tmp/lasttrades/' + assetChart + time + '.txt'
        with open(filename, 'r') as file:
            tradeAmt = float(file.read())
            if tradeAmt < 0.01:
                print('No Assets Available To Sell')
                return
    except:
        print('No Assets Available to sell')
        return

    execTrade(assetChart, 'sell', tradeAmt, price)