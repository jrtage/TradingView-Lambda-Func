import json
import setChart
import placeOrder


def lambda_handler(event, context):
    body = event['body']
    body_json = json.loads(body)
    price = float(body_json['price'])
    assetChart, asset =  setChart(body_json['ticker'])
    if body_json['strategy'] == 'buy':
        placeOrder.long(price, assetChart)
    if body_json['strategy'] == 'sell':
        placeOrder.short(price, assetChart, asset)
