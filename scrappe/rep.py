import sqlite3
import locale
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path
from datetime import date
from datetime import time
from datetime import datetime
import local
locale.setlocale(locale.LC_TIME,'')

def getRes():
  conn = sqlite3.connect(
      path.getPath())
  c = conn.cursor()
  c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid desc')
  res = c.fetchone()
  return res

def date():
  today=datetime.now()
  today = today.strftime("%d %B %G")
  print("Today's date:", today)

if __name__ == "__main__":
  # print(getRes())
  print(date())
