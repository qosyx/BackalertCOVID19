import os
import sys
full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)
def getPath():
    dbpath = path+"/covid_base.db"
    return dbpath
def getPath():
    Connectpath = path+"/connectParameters.json"
    return Connectpath