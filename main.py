from os import environ
import requests

API_KEY = 'AIzaSyBOEvN4OzAePlFp1fSRKWJlioA9r2WPZHw'
AUTH_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
TRANSACTION_URL = 'http://platform.the-brawl.eu/api/transaction'

data = {
    "email": environ['THE_BRAWL_EMAIL'],
    "password": environ['THE_BRAWL_PASSWORD'],
    "returnSecureToken": True,
}
res = requests.post(AUTH_URL, json=data, params={'key': API_KEY}).json()
id_token = res['idToken']
#bruh
res = requests.post(TRANSACTION_URL, headers={
    'Authorization': f'Bearer {id_token}'
}, json={
    #USD WALLET      a8128857-ead7-491d-9b33-67c1226f4313
    #BITCOIN WALLET  b15556c1-d545-4813-b4c0-ba33c72478a3
    #ETHERIUM WALLET ace6007f-077d-4118-94ff-4cc12f36498a
    "sourceWalletId": 'b15556c1-d545-4813-b4c0-ba33c72478a3',
    "destWalletId": 'a8128857-ead7-491d-9b33-67c1226f4313',
    "amountFromSourceWallet": 0.00002263,
    "exchangeRate": 2.2,
}, verify=False)

print(res.json())
print("bum cyk cyk")
print(669969)