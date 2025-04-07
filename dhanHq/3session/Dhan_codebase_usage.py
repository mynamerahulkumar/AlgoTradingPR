import pdb
import time
import datetime
import traceback
from Dhan_Tradehull import Tradehull
# import pandas as pd

import os 



client_code = os.getenv("CLIENT_CODE")
token_id = os.getenv("TOKEN_ID")
tsl=Tradehull(client_code,token_id)
availableBalnce=tsl.get_balance()

print("available balance",availableBalnce)

max_risk_for_the_day=(availableBalnce*1)/100 # max risk for the day


all_ltp_data   = tsl.get_ltp_data(names = ['NIFTY 19 DEC 24000 akshdgasjhgdhgasjgdhjagsdCALL', 'NIFTY 19 DEC 24000 PUT', "ACC", "CIPLA"])
acc_ltp = all_ltp_data['ACC']
pe_ltp  = all_ltp_data['NIFTY 19 DEC 24000 PUT']



stock_name = 'NIFTY'
ltp   = tsl.get_ltp_data(names = [stock_name])[stock_name]

print(ltp)

# # pdb.set_trace()

# ltp1=tsl.get_ltp('ACC')
# ltp2=tsl.get_ltp('NIFTY')
# ltp3=tsl.get_ltp('BANKNIFTY 28 AUG 51600 CALL')

# #historical data

# previous_hist_data=tsl.get_historical_data('ACC','NSE',12) # 12 days
# intraday_hist_data=tsl.get_intraday_data('ACC','NSE',1)


# print(previous_hist_data)
# print(intraday_hist_data)