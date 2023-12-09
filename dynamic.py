from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Ścieżka do sterownika przeglądarki (np. ChromeDriver)
driver_path = '/ścieżka/do/sterownika/chromedriver'

# Inicjalizacja przeglądarki
browser = webdriver.Chrome(executable_path=driver_path)

# Adres URL strony
url = 'https://platform.the-brawl.eu/dashboard'
browser.get(url)

# Poczekaj na załadowanie się danych (może wymagać dostosowania)
element = WebDriverWait(browser, 10).until(
    EC.presence_of_element_located((By.ID, 'elementID'))
)

# Pobierz dane
account_balance = element.text
print('Stan konta:', account_balance)

# Zamknij przeglądarkę
browser.quit()
