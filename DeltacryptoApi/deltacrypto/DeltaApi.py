import hashlib
import hmac
import requests
import time

base_url = 'https://api.india.delta.exchange'
api_key = 'fnt50ywnlG4uxIGKvngah6vIIES3IG'
api_secret = 'NNhshCxdxRWUQUJX2WR8nQTLIDom5UC6HnU3FcsySQImUw7Xsqq1iGhSjpKN'

def generate_signature(secret, message):
    message = bytes(message, 'utf-8')
    secret = bytes(secret, 'utf-8')
    hash = hmac.new(secret, message, hashlib.sha256)
    return hash.hexdigest()

# Get open orders
method = 'GET'
timestamp = str(int(time.time()))
path = '/v2/orders'
url = f'{base_url}{path}'
query_string = '?product_id=1&state=open'
payload = ''
signature_data = method + timestamp + path + query_string + payload
signature = generate_signature(api_secret, signature_data)

req_headers = {
  'api-key': api_key,
  'timestamp': timestamp,
  'signature': signature,
  'User-Agent': 'python-rest-client',
  'Content-Type': 'application/json'
}

query = {"BTC": 1, "state": 'open'}

response = requests.request(
    method, url, data=payload, params=query, timeout=(3, 27), headers=req_headers
)
print(response)
# # Place new order
# method = 'POST'
# timestamp = str(int(time.time()))
# path = '/v2/orders'
# url = f'{base_url}{path}'
# query_string = ''
# payload = "{\"order_type\":\"limit_order\",\"size\":3,\"side\":\"buy\",\"limit_price\":\"0.0005\",\"product_id\":16}"
# signature_data = method + timestamp + path + query_string + payload
# signature = generate_signature(api_secret, signature_data)

# req_headers = {
#   'api-key': api_key,
#   'timestamp': timestamp,
#   'signature': signature,