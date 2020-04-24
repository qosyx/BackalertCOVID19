import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'scrappe'))
import connect  as connect

def addMapDb(longitude,latitude,mapdate,numeroTel):
    result = connect.addMapdb(longitude,latitude,mapdate,numeroTel)
    return "donnée enregistrée "

def getAllMapDb():
    result = connect.getAllMapdb()
    return result