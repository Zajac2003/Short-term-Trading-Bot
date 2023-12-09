import requests
from os import environ

# Przykładowa strona do pobrania HTML
url_to_scrape = "https://platform.the-brawl.eu/dashboard"

# Jeśli potrzebujesz uwierzytelnienia, wykonaj odpowiednie kroki
# W tym przykładzie używam tylko nagłówka z uwierzytelnieniem z poprzedniego kodu

API_KEY = 'AIzaSyBOEvN4OzAePlFp1fSRKWJlioA9r2WPZHw'
AUTH_URL = 'https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword'
TRANSACTION_URL = 'https://platform.the-brawl.eu/dashboard'

# Dane do uwierzytelnienia
auth_data = {
    "email": environ['THE_BRAWL_EMAIL'],
    "password": environ['THE_BRAWL_PASSWORD'],
    "returnSecureToken": True,
}

# Uwierzytelnianie
auth_response = requests.post(AUTH_URL, json=auth_data, params={'key': API_KEY}, verify=False).json()
id_token = auth_response.get('idToken')

if id_token:
    # Dalsze operacje, jeśli autentykacja się powiedzie

    # Wykonaj żądanie GET do strony do scrapowania
    response = requests.get(url_to_scrape, headers={'Authorization': f'Bearer {id_token}'}, verify=False)

    if response.status_code == 200:
        # Jeśli pobranie się powiedzie
        html_content = response.text
        print("Pobrano kod HTML strony:")
        print(html_content)
    else:
        print(f"Błąd podczas pobierania strony. Kod odpowiedzi: {response.status_code}")
else:
    print("Błąd uwierzytelniania. Nie uzyskano tokena ID.")
