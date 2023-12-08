from os import environ
import requests

API_KEY = 'AIzaSyBOEvN4OzAePlFp1fSRKWJlioA9r2WPZHw'
AUTH_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
TRANSACTION_URL = 'http://platform.the-brawl.eu/api/transaction'

# Dane do uwierzytelnienia
auth_data = {
    "email": environ['THE_BRAWL_EMAIL'],
    "password": environ['THE_BRAWL_PASSWORD'],
    "returnSecureToken": True,
}

# Uwierzytelnianie
auth_response = requests.post(AUTH_URL, json=auth_data, params={'key': API_KEY}).json()
id_token = auth_response.get('idToken')

if id_token:
    # Dalsze operacje, jeśli autentykacja się powiedzie

    # Przykładowe pobranie danych ze strony (zmień URL według swoich potrzeb)
    sample_url = 'https://example.com'
    response = requests.get(sample_url)

    if response.status_code == 200:
        # Jeśli pobranie się powiedzie
        page_content = response.text
        print("Pobrano zawartość strony:")
        print(page_content)
    else:
        print(f"Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}")
else:
    print("Błąd uwierzytelniania. Nie uzyskano tokena ID.")
