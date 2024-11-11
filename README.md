# BinanceNotifier

**BinanceNotifier** est un bot Python qui utilise **Selenium** et **Plyer** pour surveiller en temps réel les nouvelles annonces de cryptomonnaies listées sur Binance. Le bot envoie une notification de bureau accompagnée d'un son à chaque nouvelle annonce, permettant ainsi aux utilisateurs de rester informés sans avoir à surveiller la page manuellement.

## Fonctionnalités
- **Surveillance en temps réel** des nouvelles annonces de listing de cryptomonnaies sur Binance.
- **Notifications de bureau Windows** pour chaque nouvelle annonce.
- **Son de notification** pour attirer l'attention de l'utilisateur.
- **Actualisation automatique** toutes les 60 secondes.

## Prérequis
- **Python** 3.6+
- **Google Chrome** et le **ChromeDriver** correspondant à la version de Chrome installée.
- Modules Python : **Selenium**, **Plyer**

## Installation

### 1. Cloner le dépôt

```bash
# Cloner le dépôt GitHub
git clone https://github.com/votre_nom_utilisateur/BinanceNotifier.git
cd BinanceNotifier
```

### 2. Installer les dépendances Python

Assurez-vous d'avoir un environnement Python actif, puis installez les dépendances nécessaires :

```bash
pip install selenium plyer
```

### 3. Télécharger et configurer ChromeDriver

Téléchargez **ChromeDriver** correspondant à la version de Google Chrome installée sur votre ordinateur.

Placez `chromedriver.exe` dans un répertoire, par exemple `D:\Code\chromedriver-win64`.

Ensuite, mettez à jour le chemin de ChromeDriver dans le fichier `binance_notifier.py` :

```python
# Spécifiez le chemin de votre ChromeDriver
PATH = r"D:\Code\chromedriver-win64\chromedriver.exe"
```

## Utilisation

Pour lancer le bot, exécutez le script Python suivant :

```bash
python binance_notifier.py
```

Le bot ouvrira une fenêtre Chrome pour accéder à la page des annonces de Binance et surveillera les nouveaux listings. Lorsqu'une nouvelle annonce est détectée, une notification de bureau s'affiche, accompagnée d'un son.

### Personnalisation du son de notification

Si vous souhaitez utiliser un son personnalisé pour les notifications :

Remplacez la ligne suivante dans le script :

```python
winsound.Beep(1000, 500)
```

par :

```python
winsound.PlaySound('chemin/vers/votre_son.wav', winsound.SND_FILENAME)
```

Assurez-vous que le fichier `.wav` est accessible et compatible avec Windows.

## Exemple de code

Voici un extrait du code principal du bot :

```python
import time
import winsound
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from plyer import notification

# Chemin vers ChromeDriver
PATH = r"D:\Code\chromedriver-win64\chromedriver.exe"
service = Service(PATH)
driver = webdriver.Chrome(service=service)

# URL de la page des annonces de Binance
url = 'https://www.binance.com/fr/support/announcement/nouveaux-listing-de-cryptomonnaies?c=48&navId=48'
driver.get(url)

def obtenir_titres_annonces():
    driver.get(url)
    titres_elements = driver.find_elements(By.CSS_SELECTOR, 'a.css-1w8j6ia div.css-1yxx6id')
    return [titre.text for titre in titres_elements]

titres_vus = set(obtenir_titres_annonces())

# Boucle principale de surveillance
while True:
    titres_actuels = obtenir_titres_annonces()
    nouveaux_titres = [titre for titre in titres_actuels if titre not in titres_vus]

    for titre in nouveaux_titres:
        notification.notify(
            title='Nouvelle annonce Binance',
            message=titre,
            timeout=10
        )
        winsound.Beep(1000, 500)  # Son de notification
        titres_vus.add(titre)

    time.sleep(60)
```

## Dépannage
- **Erreur de chemin de ChromeDriver** : Assurez-vous que le chemin spécifié dans `PATH` est correct et que `chromedriver.exe` est bien à cet emplacement.
- **Problème de notifications** : Si les notifications ne s'affichent pas, vérifiez les paramètres de notification de votre système Windows.

## Contributions
Les contributions sont les bienvenues ! N'hésitez pas à soumettre des pull requests ou à ouvrir des issues pour signaler des bogues ou proposer des améliorations.

## Licence
Ce projet est sous licence MIT.

