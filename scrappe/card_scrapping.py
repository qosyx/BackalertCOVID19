import requests
from bs4 import BeautifulSoup
import sys, os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import scrappe.connect as connect
import threading

def scrappingAndSave():
    threading.Timer(5.0, scrappingAndSave).start()
    URL = 'https://www.gouv.bj/coronavirus/'
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all("h2", class_="h1 adapt white left-5")
    results2 = soup.find_all("h2", class_="h1 adapt white regular")
    covid_stat = []


    for result in results:
        # print(result)
        if None in (result):
            continue
        covid_stat.append(result.text.strip())
    for result in results2:

        if None in (result):
            continue
        covid_stat.append(result.text.strip())
    print(covid_stat)
    connect.addOfficielle(int(covid_stat[0]),covid_stat[1],covid_stat[3],covid_stat[2])
    return covid_stat
    # connect.getAll()
    # print(covid_stat)

def getOne():
    return connect.getOne()[0]
    
if __name__ == "__main__":
    scrappingAndSave()
    # print(getOne())
