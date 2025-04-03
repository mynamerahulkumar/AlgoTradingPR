import pdb
import time
import datetime
import traceback
from Dhan_Tradehull import Tradehull
import pandas as pd
from pprint import pprint
import talib


client_code = "1102790337"
token_id    = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJkaGFuIiwicGFydG5lcklkIjoiIiwiZXhwIjoxNzM2ODYwMTMxLCJ0b2tlbkNvbnN1bWVyVHlwZSI6IlNFTEYiLCJ3ZWJob29rVXJsIjoiIiwiZGhhbkNsaWVudElkIjoiMTEwMjc5MDMzNyJ9.Leop6waGeVfmBOtczNEcjRWmC8pUGWQf54YPINGDi_PZjk1IvW-DDdaYXsgM_s8McOT44q4MjEQxGXU0lduK0A"
tsl         = Tradehull(client_code,token_id)


all_ltp_data   = tsl.get_ltp_data(names = ['NIFTY 19 DEC 24000 akshdgasjhgdhgasjgdhjagsdCALL', 'NIFTY 19 DEC 24000 PUT', "ACC", "CIPLA"])
acc_ltp = all_ltp_data['ACC']
pe_ltp  = all_ltp_data['NIFTY 19 DEC 24000 PUT']



stock_name = 'NIFTY'
ltp   = tsl.get_ltp_data(names = [stock_name])[stock_name]




chart = tsl.get_historical_data(tradingsymbol = 'NIFTY',  exchange = 'INDEX',timeframe="DAY")
data  = tsl.get_historical_data(tradingsymbol = 'NIFTY 19 DEC 24000 CALL'     ,exchange = 'NFO'  ,timeframe="15")



order_status  = tsl.get_order_status(orderid=82241218256027)
order_price   = tsl.get_executed_price(orderid=82241218256027)
order_time    = tsl.get_exchange_time(orderid=82241218256027)


positions = tsl.get_positions()
orderbook = tsl.get_orderbook()
tradebook = tsl.get_trade_book()
holdings = tsl.get_holdings()


ce_name, pe_name, strike = tsl.ATM_Strike_Selection(Underlying='NIFTY', Expiry=0)


ce_name, pe_name, ce_strike, pe_strike = tsl.OTM_Strike_Selection(Underlying='NIFTY', Expiry=0, OTM_count=3)

ce_name, pe_name, ce_strike, pe_strike = tsl.ITM_Strike_Selection(Underlying='NIFTY', Expiry=0, ITM_count=5)

# Equity
entry_orderid  = tsl.order_placement(tradingsymbol='ACC' ,exchange='NSE', quantity=1, price=0, trigger_price=0,    order_type='MARKET',     transaction_type='BUY',   trade_type='MIS')
sl_orderid     = tsl.order_placement(tradingsymbol='ACC' ,exchange='NSE', quantity=1, price=0, trigger_price=2200, order_type='STOPMARKET', transaction_type ='SELL', trade_type='MIS')

# Options
entry_orderid  = tsl.order_placement(tradingsymbol='NIFTY 19 DEC 24400 CALL' ,exchange='NFO', quantity=50, price=0, trigger_price=0, order_type='MARKET', transaction_type='BUY', trade_type='MIS')
sl_orderid     = tsl.order_placement(tradingsymbol='NIFTY 19 DEC 24400 CALL' ,exchange='NFO', quantity=25, price=29, trigger_price=30, order_type='STOPLIMIT', transaction_type='SELL', trade_type='MIS')

modified_order = tsl.modify_order(order_id=sl_orderid,order_type="STOPLIMIT",quantity=50,price=price,trigger_price=trigger_price)

order_ids      = tsl.place_slice_order(tradingsymbol="NIFTY 19 DEC 24400 CALL",   exchange="NFO",quantity=5000, transaction_type="BUY",order_type="LIMIT",trade_type="MIS",price=0.05)



margin = tsl.margin_calculator(tradingsymbol='ACC', exchange='NSE', transaction_type='BUY', quantity=2, trade_type='MIS', price=2180, trigger_price=0)

margin = tsl.margin_calculator(tradingsymbol='NIFTY 19 DEC 24400 CALL', exchange='NFO', transaction_type='SELL', quantity=25, trade_type='MARGIN', price=43, trigger_price=0)

margin = tsl.margin_calculator(tradingsymbol='NIFTY 19 DEC 24400 CALL', exchange='NFO', transaction_type='BUY', quantity=25, trade_type='MARGIN', price=43, trigger_price=0)
margin = tsl.margin_calculator(tradingsymbol='NIFTY DEC FUT', exchange='NFO', transaction_type='BUY', quantity=25, trade_type='MARGIN', price=24350, trigger_price=0)


exit_all       = tsl.cancel_all_orders()




