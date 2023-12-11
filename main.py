"""
from os import environ
import requests

API_KEY = 'AIzaSyBOEvN4OzAePlFp1fSRKWJlioA9r2WPZHw'
AUTH_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
TRANSACTION_URL = 'http://platform.the-brawl.eu/api/transaction'

data = {
    "email": environ['173746@stud.prz.edu.pl'],
    "password": environ['Pocotujestem'],
    "returnSecureToken": True,
}
res = requests.post(AUTH_URL, json=data, params={'key': API_KEY}).json()
id_token = res['idToken']
#bruh
res = requests.post(TRANSACTION_URL, headers={
    'Authorization': f'Bearer {id_token}'
}, json={
    "sourceWalletId": '1d0e3ee6-1fac-4246-a869-9c383ae8fa9c',
    "destWalletId": '030bcff8-1bde-4b89-b814-b9c75cfda896',
    "amountFromSourceWallet": 10,
    "exchangeRate": 2.2,
}, verify=False)

print(res.json())
print("bum cyk cyk")
print(669969)
"""
#This example uses Python 2.7 and the python-request library.

from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

bitcoin_id = 1  # ID Bitcoina na CoinMarketCap

bitcoin_url = f'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest?id={bitcoin_id}&convert=USD'

url = 'https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5000',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '1bee53f7-2d13-44e6-8344-45e04721a562',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(bitcoin_url)
  bitcoin_data = json.loads(response.text)
  bitcoin_price = bitcoin_data['data'][str(bitcoin_id)]['quote']['USD']['price']
  print(f'Aktualna cena Bitcoina w USD: {bitcoin_price}')
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)