import sqlite3

def insert(name_db, name, desc):
    try:
        conn = sqlite3.connect('files\\' + name_db)
    except:
        pass
    try:
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO data(name, content) 
            VALUES('{}', '{}');
        '''.format(name, desc))

        conn.commit()
        conn.close()
    except:
        pass