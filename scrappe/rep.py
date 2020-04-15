import sqlite3
import threading
import os, sys
sys.path.append(os.path.join(os.path.dirname(sys.path[0]), 'common_utils'))
import getDbPath as path

def getRes():
  conn = sqlite3.connect(
      path.getPath())
  c = conn.cursor()
  c.execute('SELECT  mbrecasconfirme, mbregueris, mbremort,mbresoustraitement,rowid from officielle ORDER BY rowid desc')
  res = c.fetchone()
  return res

if __name__ == "__main__":
  print(getRes())
