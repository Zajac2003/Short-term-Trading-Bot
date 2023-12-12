from os import environ
import requests

#amount from source wallet
def buyBitcoin(amount):

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
        "sourceWalletId": 'a8128857-ead7-491d-9b33-67c1226f4313',
        "destWalletId": 'b15556c1-d545-4813-b4c0-ba33c72478a3',
        "amountFromSourceWallet": amount,
        "exchangeRate": 2.2,
    }, verify=False)

    print(res.json())

def sellBitcoin(amount):

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
        "amountFromSourceWallet": amount,
        "exchangeRate": 2.2,
    }, verify=False)

    print(res.json())

def menu():
    operacja = int(input())
    if operacja == 1:
        print("buying")
        buyBitcoin(input())
        print("Bought succesfully")

    elif operacja == 2:
        print("selling")
        sellBitcoin(input())
        print("Sold succesfully")




records = [20];

print(type(records))