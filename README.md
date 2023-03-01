api.py:

add API keys here.
change URL's depending on if you are testing in Gemini's sandbox or going live (configured for sandbox currently)


balance.py:

pass in an asset symbol ('USD', 'ETH', 'BTC', etc...) returns account balance for that asset.
Returns 'None' if there is nothing for that asset


liveprice.py:

returns the current exchange rate for any asset market. Examples: 'ethusd' or 'btcusd'


trade.py:

executes a buy or sell order dependant on parameters. Configured for market orders
Parameters: asset market ('ethusd')
            buy or sell ('buy' or 'sell')
            amount of asset to buy (float)
            price to buy asset at (float)

ADD THIS AS YOUR TRADINGVIEW ALERT MESSAGE:
{
"chart": "minute",
"ticker": "{{ticker}}",
"price": "{{close}}", 
"strategy": "{{strategy.order.action}}"
}