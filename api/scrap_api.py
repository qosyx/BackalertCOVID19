import os
import sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'scrappe'))
import card_scrapping as card_scrapping

def scrappingAndSave():
    result = card_scrapping.scrappingAndSave()
    return result

def getOne():
    result = card_scrapping.getOne()
    print(result)
    return result