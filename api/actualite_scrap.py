import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'scrappe'))
import actualite_scrapping as actualite_scrapping
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'table'))
import tableCreated as tableCreated

def scrappingActualiteAndSave():
    result = actualite_scrapping.scrappingActualiteAndSave()
    return result

def getAllActualite():
    result = actualite_scrapping.getAllActualite()
    # print(result[0][0]) 
    return result

def createTable():
    tableCreated.createTable()
    return "ok"