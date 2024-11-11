import time
import winsound  # Module pour le son sous Windows
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from plyer import notification

# Chemin de ChromeDriver
PATH = r"D:\Code\chromedriver-win64\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

url = 'https://www.binance.com/en/support/announcement/new-cryptocurrency-listing?c=48&navId=48'
driver.get(url)

def obtenir_titres_annonces():
    driver.get(url)
    titres_elements = driver.find_elements(By.CSS_SELECTOR, 'a.css-1w8j6ia div.css-1yxx6id')
    titres = [titre.text for titre in titres_elements]
    return titres

titres_vus = set(obtenir_titres_annonces())

while True:
    titres_actuels = obtenir_titres_annonces()
    nouveaux_titres = [titre for titre in titres_actuels if titre not in titres_vus]

    for titre in nouveaux_titres:
        notification.notify(
            title='Nouvelle annonce Binance',
            message=titre,
            timeout=10
        )
        # Joue un son Windows pour accompagner la notification
        winsound.Beep(1000, 500)  # Fréquence 1000 Hz, durée 500 ms
        titres_vus.add(titre)

    time.sleep(60)
