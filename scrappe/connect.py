import threading
import os, sys
from pg import DB
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'table'))
import my_connexion as connexion

sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as getDbPath

def read_all():
    # print(getDbPath.getConnectPath())
    db=connexion.connect(getDbPath.getConnectPath())
    result = []
    for r in db.query(  # just for example
            "SELECT officielleid, mbrecasconfirme, mbregueris, mbresoustraitement,  mbremort "
            "FROM officielle ORDER BY officielleid desc"
            ).dictresult():
            result.append(r)
    return result

    
def addOfficielle( mbrecasconfirme, mbregueris, mbresoustraitement, mbremort):
    db=connexion.connect(getDbPath.getConnectPath())
    result = []
    for r in db.query(  # just for example
            "SELECT officielleid, mbrecasconfirme, mbregueris, mbresoustraitement,  mbremort "
            "FROM officielle ORDER BY officielleid desc"
            ).dictresult():
            result.append(r)
    res = result
    if (res == []):
        print("Insertion de donnée ..........")
        db.insert('officielle', mbrecasconfirme=mbrecasconfirme,mbregueris= mbregueris, 
                  mbresoustraitement = mbresoustraitement,mbremort = mbremort)
    else:
        if(int(res[0]['mbrecasconfirme'])==int(mbrecasconfirme) and
            int(res[0]['mbregueris'])==int(mbregueris) and 
            int(res[0]['mbresoustraitement'])==int(mbresoustraitement) and 
            int(res[0]['mbremort'])==int(mbremort)
            ):
            print("pas d'évolution des statistiques ")
        else:
            print("Stat évoluées")
            print("Insertion de donnée ..........")
            db.insert('officielle', mbrecasconfirme=mbrecasconfirme,mbregueris= mbregueris, 
                    mbresoustraitement = mbresoustraitement,mbremort = mbremort)


# def addActualite(actualite, id_date):
#     conn = sqlite3.connect(
#         path.getPath())
#     c = conn.cursor()
#     c.execute("INSERT INTO tableactualite  (actualite,id_date) \
#     VALUES ('" + str(actualite) +
    
#                 "' ,'" + str(id_date)+"')")
#     conn.commit()



# def addActualite2(actualite, id_date,taille):
#     conn = sqlite3.connect(
#         path.getPath())
#     c = conn.cursor()
#     c.execute('SELECT count(actualite) FROM tableactualite')
#     res = c.fetchone()
#     res = int(res[0])
#     # print(taille)
#     if (int(res) == 0):
#         i = 0
#         while (i<int(taille)):
#             print("Insertion de donnée ..........")
#             # print("Insertion de donnée ..........")

#             c.execute("INSERT INTO tableactualite  (actualite,id_date) \
#     VALUES ('" + str(actualite) +
    
#                 "' ,'" + str(id_date)+"')")
#             i = i +1
#     else: 
#         if(int(res)==int(taille)):
#             print("pas d'évolution des statistiques")

#         if(( int(res) < int(taille)) ): 
#             taille = taille -res
#             while (taille>0):
#                 print("Insertion de donnée ..........")
#                 c.execute("INSERT INTO tableactualite  (actualite,id_date) \
#         VALUES ('" + str(actualite) +
        
#                     "' ,'" + str(id_date)+"')")
#                 taille = taille -1
#     conn.commit()

# def getCountActualite():
#     conn = sqlite3.connect(path.getPath())
#     c = conn.cursor()
#     c.execute('SELECT count(actualite) FROM tableactualite')
#     res = c.fetchone()
#     res = int(res[0])
#     return res
# def getAll():
#     conn = sqlite3.connect(
#         path.getPath())
#     c = conn.cursor()
#     c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid asc')
#     result = c.fetchall()
#     return result

def getOne():
    db=connexion.connect(getDbPath.getConnectPath())
    result = []
    for r in db.query(  # just for example
            "SELECT officielleid, mbrecasconfirme, mbregueris, mbresoustraitement,  mbremort "
            "FROM officielle ORDER BY officielleid desc"
            ).dictresult():
            result.append(r)
    return result

# def getAllActualite():
#     conn = sqlite3.connect(
#         path.getPath())
#     c = conn.cursor()
#     c.execute('SELECT actualite, id_date, rowid from tableactualite')
#     result = c.fetchall()
#     return result


################ add mapbb
### Add mapDb
def addMapdb(longitude,latitude,mapdate,numerotel):
    db=connexion.connect(getDbPath.getConnectPath())
    db.insert('mapdb', longitude=longitude,latitude= latitude, 
                  mapdate = mapdate,numerotel = numerotel)

### Read All MapDb
def getAllMapdb():
    db=connexion.connect(getDbPath.getConnectPath())
    result = []
    for r in db.query(  # just for example
            "SELECT mapdbid, longitude, latitude, mapdate, numerotel "
            "FROM mapdb ORDER BY mapdbid desc"
            ).dictresult():
            result.append(r)
    return result




if __name__ == "__main__":
    # createTablesActualite()
    # createTablesOfficielle() 
    addOfficielle(1,1,1,1)
    # print(type(getCountActualite()))   
# addOfficielle(1,1,1,1,1)

    # r = getOne()
    # print(r)
    # check(35, 5, 1, 29)
    # addActualite(1,
    #         "Une délégation gouvernementale conduite par le MS Benjamin HOUNKPATIN est actuellement dans les départements Alibori,Donga,Borgou, Atacora pour effectuer des remises de matériels médicaux.",'14 avril 2020 à 14:20')
    # print(getActualite())