import sqlite3
import locale
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path
from datetime import date, datetime, time
from babel.dates import format_date, format_datetime, format_time

def getRes():
  conn = sqlite3.connect(
      path.getPath())
  c = conn.cursor()
  c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid desc')
  res = c.fetchone()
  return res

def date():
  today=datetime.now()
  today=format_datetime(today,format='long', locale='fr_FR')
  today=today.split("à")[0]
  return today


  
  
if __name__ == "__main__":
  # print(getRes())
  print(date())
