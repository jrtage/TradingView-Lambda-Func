def setChart(tvChart):
    assetChart = tvChart.lower()
    asset = assetChart.replace('usd','').upper()
    return assetChart, asset