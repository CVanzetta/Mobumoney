import time
import requests
from bs4 import BeautifulSoup
from plyer import notification

url = 'https://www.binance.com/fr/support/announcement'

def obtenir_titres_annonces():
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    titres = soup.select('a.css-1ej4hfo')
    return [titre.text for titre in titres]

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
        titres_vus.add(titre)

    time.sleep(60)
