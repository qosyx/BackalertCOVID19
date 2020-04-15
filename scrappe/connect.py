import sqlite3
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path

def createConnexion():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    return c


def createTablesOfficielle():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    # Create officielle
    c.execute('''CREATE TABLE officielle
                (idOfficielle INT PRIMARY KEY   NOT NULL,
                mbrecasconfirme INT, 
                mbregueris INT, 
                mbresoustraitement INT, 
                mbremort INT)''')

def createTablesActualite():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    # Create officielle
    c.execute('''CREATE TABLE tableactualite
                (idactualite INT PRIMARY KEY   NOT NULL,
                actualite TEXT, 
                id_date TEXT)''')
    
def addOfficielle(idOfficielle, mbrecasconfirme, mbregueris, mbremort,mbresoustraitement):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT * from officielle ORDER BY idOfficielle asc')
    res = c.fetchone()
    if (res == None):
        print("Insertion de donnée ..........")
        c.execute("INSERT INTO officielle (idOfficielle,mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" + str(idOfficielle) + "," + str(mbrecasconfirme) +
                  "," + str(mbregueris) + "," + str(mbresoustraitement) + "," + str(mbremort)+")")
    else:
        if((int(mbrecasconfirme) == int(res[1])) and (int(mbresoustraitement) == int(res[4]))
            and (int(mbregueris) == int(res[2])) and (int(mbremort) == int(res[3])) 
           ):
            print(res)
            print("pas d'évolution ")
        else:
            print("Insertion de donnée ..........")

            c.execute("INSERT INTO officielle (idOfficielle,mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" + str(idOfficielle) + "," + str(mbrecasconfirme) +
                "," + str(mbregueris) + "," + str(mbresoustraitement) + "," + str(mbremort)+")")


    conn.commit()


def addActualite(idactualite, actualite, id_date):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute("INSERT INTO tableactualite  (idactualite,actualite,id_date) \
    VALUES (" + str(idactualite) + ",'" + str(actualite) +
    
                "' ,'" + str(id_date)+"')")
    conn.commit()


def getAll():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT * from officielle ORDER BY idOfficielle asc')
    result = c.fetchall()
    return result

def getOne():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT * from officielle ORDER BY idOfficielle desc LIMIT 1')
    result = c.fetchone()
    return result

def getActualite():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT * from tableactualite')
    result = c.fetchone()
    return result
    # if (c.fetchone() == None):
    #     print("pas de donnée")
    # else:
    #     print (c.fetchone()[0])

    # for row in c.execute('SELECT * from officielle ORDER BY idOfficielle asc'):
    #     print (row)
    # ,mbregueris,mbresoustraitement,mbremort


def check(mbrecasconfirme, mbregueris, mbresoustraitement, mbremort):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    for row in c.execute('SELECT * from officielle ORDER BY idOfficielle desc LIMIT 1'):
        if (row[1] == mbrecasconfirme and row[2] == mbregueris and row[3] == mbresoustraitement and row[4] == mbremort):
            pass
        else:
            print("ok")


if __name__ == "__main__":
    createTablesActualite()
    createTablesOfficielle()    
# addOfficielle(1,1,1,1,1)

    # r = getOne()
    # print(r)
    # check(35, 5, 1, 29)
    # addActualite(1,
    #         "Une délégation gouvernementale conduite par le MS Benjamin HOUNKPATIN est actuellement dans les départements Alibori,Donga,Borgou, Atacora pour effectuer des remises de matériels médicaux.",'14 avril 2020 à 14:20')
    # print(getActualite())