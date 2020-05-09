import requests
from bs4 import BeautifulSoup
import sys, os
import threading
import pandas as pd
import sqlite3
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path

# postgresql+pygresql://username:password@host:port/database


def scrapperIntox():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    URL = 'https://www.who.int/fr/emergencies/diseases/novel-coronavirus-2019/advice-for-public/myth-busters'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    # html = open("https://unric.org/fr/covid-19-info-ou-intox/").read()
    # soup = BeautifulSoup(html)
    # filtered = soup.find_all(attrs={"span": "color: #ff0000"})
    # results = soup.find_all("span")
    resultsTitre = soup.find_all('h2')
    resultsContenu = soup.find_all('p')
    contenu = []
    titre = []
    for result in resultsTitre:

        if None in (result):
            continue
        titre.append(result.text.strip())
    print(len(titre))

    for result in resultsContenu:

        if None in (result):
            continue
        contenu.append(result.text.strip())
    print(len(titre))

    i = 0
    while (i<len(titre)):
        print("Insertion de donnée ..........")

        c.execute("INSERT INTO intoxDb  (intoxTitre,intoxContenu) \
        VALUES ('" + str(echapper(titre[i])) +

        "' ,'" + str(echapper(contenu[i]))+"')")
        i = i +1
    conn.commit()


def echapper(text):
    text=text.replace("'","''")
    text=text.replace("ô","o")
    return text

if __name__ == "__main__":
    scrapperIntox()
