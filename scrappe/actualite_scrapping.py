import requests
from bs4 import BeautifulSoup
import sys, os
import connect 
import id_generate as id_generate 
import threading
import pandas as pd
import connect
import sqlite3
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path

taille_actualite_date = 0

def scrappingActualiteAndSave():
    threading.Timer(5.0, scrappingActualiteAndSave).start()
    actualite = []
    actualite_date = []
    i =  connect.getCountActualite()
    # print(i)
    # threading.Timer(5.0, scrappingAndSave).start()
    URL = 'https://www.gouv.bj/coronavirus/flashinfos/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("h3", class_="adapt error regular bottom-10")
    results_day = soup.find_all("div", class_="flex row space middle")

    # results_day = soup.find_all( class_="black p adapt")



    for result in results:

        if None in (result):
            continue
        actualite.append(result.text.strip())
        # print(result.text.strip())
    
    # print(actualite)
    # df_empty = pd.DataFrame(actualite)
    
    for result in results_day:

        if None in (result):
            continue
        actualite_date.append(result.text.strip().split("\n")[0])
    # print(actualite_date)

    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT count(actualite) FROM tableactualite')
    res = c.fetchone()
    res = int(res[0])
    # print(len(actualite_date))
    if (res == 0):
        i = 0
        while (i<len(actualite_date)):
            print("Insertion de donnée ..........")
            # print("Insertion de donnée ..........")

            c.execute("INSERT INTO tableactualite  (actualite,id_date) \
        VALUES ('" + str(echapper(actualite[i])) +
    
                "' ,'" + str(actualite_date[i])+"')")
            i = i +1
            conn.commit()
    else: 
        if(int(res)==len(actualite_date)):
            print("pas d'évolution des informations")
        # print(actualite_date)
        if(int(res) < len(actualite_date) ): 
            taille = len(actualite_date) 
            taille = taille -res
            while (taille>0):
                print("Insertion de donnée à partir d'index..........")
                # print("Insertion de donnée ..........")

                c.execute("INSERT INTO tableactualite  (actualite,id_date) \
            VALUES ('" + str(echapper(actualite[taille])) +
        
                    "' ,'" + str(actualite_date[taille])+"')")
                conn.commit()
                taille = taille -1

        
        
        
    return actualite_date



def echapper(text):
    text=text.replace("'","''")
    text=text.replace("ô","o")
    return text

# def findAndReplaceDate():
#     text=text.replace("Aujourd'hui","''")


def getAllActualite():
    resultat_actualite_display = []
    resultats = connect.getAllActualite()
    for resultat in resultats:
        if None in (resultat):
            continue
        resultat_actualite_display.append(resultat)
    return resultat_actualite_display
    # resultat_actualite_display = [r[0],r[1],r[2]]
    # return resultat_actualite_display    
if __name__ == "__main__":
    scrappingActualiteAndSave()
    # print(getAllActualite())
    # print(getOne())
    # r = "L'hôpital de zone d'Allada transformé en centre de traitement et de prise en charge du Covid-19."
    # print(echapper(r))