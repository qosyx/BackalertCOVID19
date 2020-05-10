import requests
from bs4 import BeautifulSoup
import sys, os
import connect 
import id_generate as id_generate 
import threading
import pandas as pd
import sqlite3
import threading
import os, sys
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time
from pg import DB
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'table'))
import my_connexion as connexion

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as getDbPath

taille_actualite_date = 0

def scrappingActualiteAndSave():
    threading.Timer(5.0, scrappingActualiteAndSave).start()
    actualite = []
    actualite_date = []

    URL = 'https://www.gouv.bj/coronavirus/flashinfos/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("h3", class_="adapt error regular bottom-10")
    results_day = soup.find_all("div", class_="flex row space middle")





    for result in results:

        if None in (result):
            continue
        actualite.append(result.text.strip())

    
    for result in results_day:

        if None in (result):
            continue
        actualite_date.append(result.text.strip().split("\n")[0])



    db=connexion.connect(getDbPath.getConnectPath())
    result = []
    r=db.query("SELECT count(actualite) FROM tableactualite").dictresult()
    res = int(r[0]['count'])
    print(len(actualite_date))
    if (res == 0):
        i = 0
        while (i<len(actualite_date)):
            print("Insertion de donnée ..........")
            db.insert('tableactualite', actualite=str(echapper(actualite[i])),id_date= str((findAndReplaceDate(actualite_date[i]))))            
            i = i+1
        #     print("Insertion de donnée ..........")
        #     # print("Insertion de donnée ..........")

        #     c.execute("INSERT INTO tableactualite  (actualite,id_date) \
        # VALUES ('" + str(echapper(actualite[i])) +
    
        #         "' ,'" + str(actualite_date[i])+"')")
        #     i = i +1
        #     conn.commit()
    else: 
        if(int(res)==len(actualite_date)):
            print("pas d'évolution des informations")
        # print(actualite_date)
        if(int(res) < len(actualite_date) ): 
            taille = len(actualite_date) 
            taille = taille -int(res)
            print(taille)
            taille = len(actualite_date)-taille+1
            while (taille<len(actualite_date) ):
                print("Insertion de donnée à partir d'index.........."+ str(taille))
                db.insert('tableactualite', actualite=str(echapper(actualite[taille])),id_date= str(findAndReplaceDate(actualite_date[taille])))            
                taille = taille +1     
    return actualite_date



def echapper(text):
    text=text.replace("'","''")
    return text

def findAndReplaceDate(text):
    print("odk")
    text=text.replace("Aujourd'hui",date())
    return text

def date():
  today=datetime.now()
  today=format_datetime(today,format='long', locale='fr_FR')
  today=today.split("à")[0]
  return today

def getAllActualite():
    # print(getDbPath.getConnectPath())
    db=connexion.connect(getDbPath.getConnectPath())
    result = [] 
    for r in db.query(  # just for example
            "SELECT tableactualiteid, actualite, id_date "
            "FROM tableactualite ORDER BY tableactualiteid asc"
            ).dictresult():
            result.append(r)
    return result
if __name__ == "__main__":
    scrappingActualiteAndSave()
    print(getAllActualite())
    # print(getOne())
    # r = "L'hôpital de zone d'Allada transformé en centre de traitement et de prise en charge du Covid-19."
    # print(echapper(r))