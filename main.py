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