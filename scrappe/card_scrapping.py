import requests
from bs4 import BeautifulSoup
import sys, os
import connect 
import id_generate as id_generate 
import threading

def scrappingAndSave():
    threading.Timer(5.0, scrappingAndSave).start()
    URL = 'https://www.gouv.bj/coronavirus/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("h2", class_="h1 adapt white")
    results2 = soup.find_all("h2", class_="h1 adapt white alt")
    covid_stat = []


    for result in results:

        if None in (result):
            continue
        covid_stat.append(result.text.strip())

    for result in results2:

        if None in (result):
            continue
        covid_stat.append(result.text.strip())
    
    connect.addOfficielle(int(covid_stat[0]),covid_stat[1],covid_stat[2],covid_stat[3])
    return covid_stat
    # connect.getAll()
    # print(covid_stat)

def getOne():
    return connect.getOne()
    
if __name__ == "__main__":
    scrappingAndSave()
    # print(connect.getOne())
