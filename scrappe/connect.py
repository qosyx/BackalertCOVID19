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


def createTables():
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


def addOfficielle(idOfficielle, mbrecasconfirme, mbregueris, mbresoustraitement, mbremort):
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
        if((mbrecasconfirme == res[1])):
            print("pas d'évolution ")
        else:
            print("Insertion de donnée ..........")

            c.execute("INSERT INTO officielle (idOfficielle,mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" + str(idOfficielle) + "," + str(mbrecasconfirme) +
                "," + str(mbregueris) + "," + str(mbresoustraitement) + "," + str(mbremort)+")")


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
    # createTables()
    # addOfficielle(1,1,1,1,1)

    r = getOne()
    print(r)
    # check(35, 5, 1, 29)

