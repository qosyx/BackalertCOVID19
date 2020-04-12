import sqlite3

def createConnexion():
    conn = sqlite3.connect('/home/archange/Documents/Mobile/Alert COVID 19/back-end/covid_base.db')
    c = conn.cursor()
    return c

def createTables():
    conn = sqlite3.connect('/home/archange/Documents/Mobile/Alert COVID 19/back-end/covid_base.db')
    c = conn.cursor()
    # Create officielle
    c.execute('''CREATE TABLE officielle
                (idOfficielle INT PRIMARY KEY   NOT NULL,
                mbrecasconfirme INT, 
                mbregueris INT, 
                mbresoustraitement INT, 
                mbremort INT)''')

def addOfficielle(idOfficielle,mbrecasconfirme,mbregueris,mbresoustraitement,mbremort):
    conn = sqlite3.connect('/home/archange/Documents/Mobile/Alert COVID 19/back-end/covid_base.db')
    c = conn.cursor()
    # for row in c.execute('SELECT * from officielle ORDER BY idOfficielle desc LIMIT 1'):
    #     print(row)
    c.execute("INSERT INTO officielle (idOfficielle,mbrecasconfirme,mbregueris,mbresoustraitement,mbremort) \
    VALUES (" +str(idOfficielle) +"," + str( mbrecasconfirme) + 
    ","  + str( mbregueris) +"," +  str(mbresoustraitement) + ","+ str( mbremort )+")")

    conn.commit()

def getAll():
    conn = sqlite3.connect('/home/archange/Documents/Mobile/Alert COVID 19/back-end/covid_base.db')
    c = conn.cursor()
    for row in c.execute('SELECT * from officielle ORDER BY idOfficielle asc'):
        print (row)
    # ,mbregueris,mbresoustraitement,mbremort
def check(mbrecasconfirme,mbregueris,mbresoustraitement,mbremort):
    conn = sqlite3.connect('/home/archange/Documents/Mobile/Alert COVID 19/back-end/covid_base.db')
    c = conn.cursor()
    for row in c.execute('SELECT * from officielle ORDER BY idOfficielle desc LIMIT 1'):
        if (row[1] == mbrecasconfirme and row[2] == mbregueris and row[3] == mbresoustraitement and row[4]  == mbremort):
            pass
        else:
            print("ok")



if __name__ == "__main__":
    # createTables()
    addOfficielle(1,1,1,1,1)

    getAll()
    # check(35, 5, 1, 29)


