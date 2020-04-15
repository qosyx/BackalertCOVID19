import requests
from bs4 import BeautifulSoup
import sys, os
import connect 
import id_generate as id_generate 
import threading
import pandas as pd
import connect

actualite = []
actualite_date = []
def scrappingAndSave():
    # threading.Timer(5.0, scrappingAndSave).start()
    URL = 'https://www.gouv.bj/coronavirus/flashinfos/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("h3", class_="adapt error regular bottom-10")
    results_day = soup.find_all("div", class_="flex row space middle")

    # results_day = soup.find_all( class_="black p adapt")

    covid_stat = []


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

    i = 0
    while(i<len(actualite_date)):
        r = echapper(actualite[i])
        # print(r)
        connect.addActualite(i,r,actualite_date[i])
        i = i + 1
def echapper(text):
    text=text.replace("'","''")
    text=text.replace("ô","o")
    return text
def getOne():
    return connect.getOne()
    
if __name__ == "__main__":
    scrappingAndSave()
    # r = "L'hôpital de zone d'Allada transformé en centre de traitement et de prise en charge du Covid-19."
    # print(echapper(r))