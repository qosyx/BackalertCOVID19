import sys
import os
sys.path.append(os.path.join(os.path.dirname(sys.path[0])))
import table.my_connexion as connexion
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
path=path+"/connectParameters.json"
#Return all tables
def allTable(db):
    return db.get_tables()
#Creation des tables 
def createTable(db):
   
    # db.query("DROP DATABASE IF EXISTS veda")
    # db.query("create database veda")

    # db.query("truncate TABLE  entete CASCADE")
     #mapDb
    db.query("create table if not exists mapDb "
    "(mapDbid serial primary key, longitude varchar, latitude varchar, "
    "mapdate varchar, numeroTel varchar"
    ")"
    )
    #officielle
    db.query("create table if not exists officielle "
    "(officielleid serial primary key, mbrecasconfirme INT, mbregueris INT, mbresoustraitement INT, mbremort INT"
    ")"
    )
    #tableactualite
    db.query("create table if not exists tableactualite "
    "(tableactualiteid serial primary key, actualite varchar, id_date varchar"
    ")"
    )
    

def execution(parameters_path):
    r=connexion.connect(parameters_path)
    createTable(r)

def dropTableByName(db,tablename):
    myquery="drop table "+tablename
    db.query(myquery)
if __name__ == '__main__':
    # Charger tous les paramètres
    parameters_path = sys.argv[1]
    r=connexion.connect(parameters_path)
    createTable(r)
