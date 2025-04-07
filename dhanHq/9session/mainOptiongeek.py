import pdb
import time
import datetime
import traceback
from Dhan_Tradehull import Tradehull
import pandas as pd
import os 
from dotenv import load_dotenv  # Added to load .env file

load_dotenv() 


client_code = os.getenv("CLIENT_CODE")
token_id = os.getenv("TOKEN_ID")
print("client token {} token id {}".format(client_code,token_id))
tsl=Tradehull(client_code,token_id)

all_values=tsl.get_option_greek(22200,'06-04-2025','NIFTY',10,'all_val',
                                'CE')
print(all_values)