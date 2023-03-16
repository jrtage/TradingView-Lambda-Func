import json
from setChart import setChart
import placeOrder


def lambda_handler(event, context):
    print('----------------BEGIN CALL----------------')
    body = event['body']
    body_json = json.loads(body)
    price = float(body_json['price'])
    assetChart, asset =  setChart(body_json['ticker'])
    timeChart = body_json['chart']
    if body_json['strategy'] == 'buy':
        placeOrder.long(price, assetChart, timeChart)
    if body_json['strategy'] == 'sell':
        placeOrder.short(price, assetChart, asset, timeChart)
    print('----------------END CALL----------------')
