import sqlite3
import os

def creatdir():
    try:
        os.mkdir('files')
    except:
        pass

def createfiles(name):
    creatdir()
    conn = sqlite3.connect('files\\' + name + '.db')
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS data(
        id INTEGER PRIMARY KEY,
        name TEXT,
        content TEXT);
    ''')
    conn.commit()
    conn.close()