from delta_rest_client import DeltaRestClient

delta_client = DeltaRestClient(
  base_url='https://api.india.delta.exchange',
  api_key='fnt50ywnlG4uxIGKvngah6vIIES3IG',
  api_secret='NNhshCxdxRWUQUJX2WR8nQTLIDom5UC6HnU3FcsySQImUw7Xsqq1iGhSjpKN'
)
response = delta_client.get_assets()
# print(response)

'''
27	BTCUSD	perpetual_futures	Bitcoin Perpetual futures margined and settled in INR
3136	ETHUSD	perpetual_futures	Ethereum perpetual futures margined and settled in INR
2000	P-BTC-38100-230124	put_options	BTC put option strike price $38100 and expiring on 23/01/2024
5000	C-BTC-55800-170224	call_options	BTC call option strike price $55800 and expiring on 17/02/2024

'''
btc_product_id = 27
product = delta_client.get_product(btc_product_id) # Current Instrument
settling_asset = product['settling_asset'] # Currency in which the pnl will be realised
# print(settling_asset)

btc_symbol = 'BTCUSD'
response = delta_client.get_ticker(btc_symbol)
# print(response)

# response = delta_client.get_l2_orderbook(btc_product_id)
# print(btc_product_id)

orders = delta_client.get_live_orders()
print("orders",orders)

order_response = delta_client.place_stop_order(
        product_id=btc_product_id,
        size=10,
        side='buy',
				limit_price='7800',
        order_type=OrderType.LIMIT,
     		time_in_force=TimeInForce.FOK
    )
