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
                (
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
                (actualite TEXT, 
                id_date TEXT)''')
    
def addOfficielle( mbrecasconfirme, mbregueris, mbremort,mbresoustraitement):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid asc')
    res = c.fetchone()
    if (res == None):
        print("Insertion de donnée ..........")
        c.execute("INSERT INTO officielle (mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" + str(mbrecasconfirme) +
                  "," + str(mbregueris) + "," + str(mbresoustraitement) + "," + str(mbremort)+")")
    else:
        if((int(mbrecasconfirme) == int(res[0])) and (int(mbresoustraitement) == int(res[3]))
            and (int(mbregueris) == int(res[1])) and (int(mbremort) == int(res[2])) 
           ) :
            # print(res)
            print("pas d'évolution des statistiques ")
        else:
            print("Insertion de donnée ..........")

            c.execute("INSERT INTO officielle (mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" + str(mbrecasconfirme) +
                "," + str(mbregueris) + "," + str(mbresoustraitement) + "," + str(mbremort)+")")


    conn.commit()


def addActualite(actualite, id_date):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute("INSERT INTO tableactualite  (actualite,id_date) \
    VALUES ('" + str(actualite) +
    
                "' ,'" + str(id_date)+"')")
    conn.commit()



def addActualite2(actualite, id_date,taille):
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT count(actualite) FROM tableactualite')
    res = c.fetchone()
    res = int(res[0])
    # print(taille)
    if (int(res) == 0):
        i = 0
        while (i<int(taille)):
            print("Insertion de donnée ..........")
            # print("Insertion de donnée ..........")

            c.execute("INSERT INTO tableactualite  (actualite,id_date) \
    VALUES ('" + str(actualite) +
    
                "' ,'" + str(id_date)+"')")
            i = i +1
    else: 
        if(int(res)==int(taille)):
            print("pas d'évolution des statistiques")

        if(( int(res) < int(taille)) ): 
            taille = taille -res
            while (taille>0):
                print("Insertion de donnée ..........")
                c.execute("INSERT INTO tableactualite  (actualite,id_date) \
        VALUES ('" + str(actualite) +
        
                    "' ,'" + str(id_date)+"')")
                taille = taille -1
    conn.commit()

def getCountActualite():
    conn = sqlite3.connect(path.getPath())
    c = conn.cursor()
    c.execute('SELECT count(actualite) FROM tableactualite')
    res = c.fetchone()
    res = int(res[0])
    return res
def getAll():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid asc')
    result = c.fetchall()
    return result

def getOne():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid desc')
    result = c.fetchone()
    return result

def getAllActualite():
    conn = sqlite3.connect(
        path.getPath())
    c = conn.cursor()
    c.execute('SELECT actualite, id_date, rowid from tableactualite')
    result = c.fetchall()
    return result
    # if (c.fetchone() == None):
    #     print("pas de donnée")
    # else:
    #     print (c.fetchone()[0])

    # for row in c.execute('SELECT * from officielle ORDER BY idOfficielle asc'):
    #     print (row)
    # ,mbregueris,mbresoustraitement,mbremort





if __name__ == "__main__":
    createTablesActualite()
    createTablesOfficielle() 
    print(type(getCountActualite()))   
# addOfficielle(1,1,1,1,1)

    # r = getOne()
    # print(r)
    # check(35, 5, 1, 29)
    # addActualite(1,
    #         "Une délégation gouvernementale conduite par le MS Benjamin HOUNKPATIN est actuellement dans les départements Alibori,Donga,Borgou, Atacora pour effectuer des remises de matériels médicaux.",'14 avril 2020 à 14:20')
    # print(getActualite())