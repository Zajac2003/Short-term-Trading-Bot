from os import environ
import requests
import time
import threading
from itertools import count
from datetime import datetime

def dopiszDoPliku(transakcja):
    nazwa_pliku = 'transakcje.txt'

    with open(nazwa_pliku, 'a') as plik:
        # Zamień datę na ciąg znaków w odpowiednim formacie
        data_str = transakcja['data'].strftime("%Y-%m-%d %H:%M:%S")

        # Tworzenie linii do zapisania w pliku
        linia = f"id: {transakcja['id']}, kupno: {transakcja['kupno']}, sprzedaz: {transakcja['sprzedaz']}, profit: {transakcja['profit']}, data: {data_str}, boughtBTCammount: {transakcja['boughtBTCammount']}, soldBTCammount: {transakcja['soldBTCammount']}"

        # Zapisz linię do pliku
        plik.write(linia + '\n')

#amount from source wallet
def buyBitcoin(amountInDollars):

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
        "amountFromSourceWallet": amountInDollars,
        "exchangeRate": 2.2,
    }, verify=False)

    print(res.json())

#amount
def sellBitcoin(amountInBitcoins):

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
        "amountFromSourceWallet": amountInBitcoins,
        "exchangeRate": 2.2,
    }, verify=False)

    print(res.json())

##wyswietla menu dzialan, bylo potrzebne do testow, teraz rzadko sie przyda
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

#returns current bitcoin value in USD (float)
def currentBitcoinExchangeRate():
    url = "https://api.coinbase.com/v2/exchange-rates?currency=BTC"

    # Wykonaj GET request
    response = requests.get(url)

    # Sprawdź, czy odpowiedź jest udana (status code 200)
    if response.status_code == 200:
        # Pobierz dane z odpowiedzi
        data = response.json()
        kurs = data['data']['rates']['BUSD']
        kurs = float(kurs)
        return kurs + 120
    else:
        # W przypadku nieudanej odpowiedzi, wyświetl komunikat o błędzie
        print(f"Nieudany GET request. Status code: {response.status_code}")

#sprawdza, czy bitcoin ma gwaltowne zmiany
#zwraca True, jesli w ciagu ostatnich 10 kursow rozstęp wynosi więcej niż 20 dolarów
def fun_turbulencje():
    max_val = max(kursy[:5])
    min_val = min(kursy[:5])

    rozstep = max_val - min_val

    return rozstep > 50


##wątek aktualizujący cenę bitcoina na dodanej liście. Działa na !oryginale!
##Najnowsze rekordy na index 0, im wyzszy indeks tym starszy rekord
def aktualizujListe(kursy):
    lock.acquire()
    kursy.append(currentBitcoinExchangeRate())
    lock.release()

    #print(kursy)
    while(True):
        element = currentBitcoinExchangeRate()
        if element != kursy[0]:
            lock.acquire()
            kursy.insert(0, element)
            lock.release()
            print(len(kursy), kursy)
        if len(kursy) > 200:
            lock.acquire()
            kursy = kursy[:-100]
            lock.release()
            #print("dlugosc listy to ", len(kursy))
        time.sleep(5)

#zwraca wartość średnią z n pierwszych rekordów
#n = wartość którą podajesz
def srednia(ogranicznik):
    ogranicznik = int(ogranicznik)
    if len(kursy) >= ogranicznik:
        srednia = 0
        for i in range(0,ogranicznik):
            srednia += float(kursy[i])
        return srednia/ogranicznik

def tradingBot():
    while(len(kursy) < 16):
        time.sleep(3)

    transaction_id = int(0)
    prev_profit = 0
    ovallprofit = 0

    for przejscie in count():
        aktualny_kurs = float(kursy[0])

        prev_profit = ovallprofit
        ovallprofit = 0

        turbulencje = fun_turbulencje()

        for element in wykonane_transakcje:
            ovallprofit += float(element['profit'])

        if prev_profit != ovallprofit:
            print('Profit: ', ovallprofit)

        if(przejscie != 0):
            poprzedniaTwardaSrednia = float(twardaSrednia)
            poprzedniaMiekkaSrednia = float(miekkaSrednia)
            poprzedniaUniwersalnaSrednia = float(uniwersalnaSrednia)

        twardaSrednia = float(srednia(4))
        miekkaSrednia = float(srednia(15))
        uniwersalnaSrednia = twardaSrednia*0.7 + miekkaSrednia*0.3

        if float(kursy[0]) > float(kursy[1]) and float(kursy[2]) > float(kursy[2]):
            trend = 'rosnacy'
        elif float(kursy[0]) < float(kursy[1]) and float(kursy[1]) < float(kursy[2]):
            trend = 'malejacy'
        else:
            trend = 'zaden'

        if przejscie != 0:
            if twardaSrednia != poprzedniaTwardaSrednia:
                #print(f'Uniwersalna: {uniwersalnaSrednia}, aktualny kurs: {aktualny_kurs}')
                aktywneTransakcje = len(transakcje)

                if((float(uniwersalnaSrednia) > float(aktualny_kurs)) and aktywneTransakcje < 6 and not turbulencje):
                    print(f'Kupuje za {aktualny_kurs}')
                    buyBitcoin(1000)
                    transakcje.append({ 'id': transaction_id,'kupno': float(aktualny_kurs), 'sprzedaz': [], 'profit': [], 'data': datetime.now(), 'boughtBTCammount': 1000/aktualny_kurs, 'soldBTCammount': []})
                    transaction_id += 1

                for transakcja in transakcje:
                    wiek = datetime.now() - transakcja['data']
                    wiek = wiek.total_seconds()

                    if (float(transakcja['kupno']) - float(aktualny_kurs)) < -0.5:
                        print(f'SPRZEDAJE ZA {aktualny_kurs}')
                        #print('Sprzedaje ', transakcja['boughtBTCammount'] )
                        sellBitcoin(transakcja['boughtBTCammount'] - 0.00000000000000100)
                        transakcja['sprzedaz'] = float(aktualny_kurs)
                        transakcja['profit'] = float(transakcja['sprzedaz']) - float(transakcja['kupno'])
                        transakcja['soldBTCammount'] = float(transakcja['boughtBTCammount']) - 0.00000000000000100
                        wykonane_transakcje.append(transakcja)
                        transakcje.remove(transakcja)
                        dopiszDoPliku(transakcja)
                    elif wiek > 120:
                        print("Sprzedarz ze starosci")
                        print(f'SPRZEDAJE ZA {aktualny_kurs}')
                        sellBitcoin(transakcja['boughtBTCammount'] - 0.00000000000000100)
                        transakcja['sprzedaz'] = float(aktualny_kurs)
                        transakcja['profit'] = float(transakcja['sprzedaz']) - float(transakcja['kupno'])
                        transakcja['soldBTCammount'] = float(transakcja['boughtBTCammount']) - 0.00000000000000100
                        wykonane_transakcje.append(transakcja)
                        transakcje.remove(transakcja)

        if len(transakcje) != 0:
            print("------------------------------LISTA TRANSAKCJI------------------------------")
            for i in transakcje:
                print(i)
            print("############################################################################")

            print("------------------------------WYKONANE------------------------------")
            for i in wykonane_transakcje:
                print(i)
            print("############################################################################")

        time.sleep(1)


trend = 'brak'
#kursy = [42169.63075920577, 42151.384000613274, 42167.16556970714, 42169.175769572714, 42160.76493331926, 42177.43321370291, 42170.006727217755, 42172.287183673805, 42156.988778213024, 42153.62427613912, 42156.573839621444, 42153.06935826363, 42147.29021354233, 42150.9676652738, 42147.41286929855, 42150.802674743296, 42137.75842340797, 42125.42913103812]
kursy = []
transakcje = []
wykonane_transakcje = []

lock = threading.Lock()

thread1 = threading.Thread(target=aktualizujListe, args=(kursy,))
thread2 = threading.Thread(target=tradingBot)

thread1.start()
thread2.start()
