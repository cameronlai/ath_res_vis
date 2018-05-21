"""
This file inserts the data from the tmp sql file to do the existing database file.
"""
import sqlite3

tmp_db_file = 'tmp_db.sqlite3'
tmp_conn = sqlite3.connect(tmp_db_file)
tmp_cur = tmp_conn.cursor()
tmp_cur.execute('SELECT * from ath_results')

db_file = 'db.sqlite3'
conn = sqlite3.connect(db_file)
cur = conn.cursor()

# Attempt to delete table first
sql_delete_cmd = '''
    DROP TABLE IF EXISTS ath_results
    '''
cur.execute(sql_delete_cmd)

# Attempt to create table
sql_create_cmd = '''
    CREATE TABLE IF NOT EXISTS ath_results (
        id INTEGER PRIMARY KEY, Name TEXT, School TEXT, Event TEXT,
        Sex TEXT, Result REAL, Date TIMESTAMP, IsTrack INTEGER
        );
    '''
cur.execute(sql_create_cmd)

for i, item in enumerate(tmp_cur.fetchall()):
    if i % 1000 == 0: print(i)
    sql_insert_cmd = '''
        INSERT INTO ath_results("Name", "School", "Event", "Sex", "Result", "Date", "IsTrack")
        VALUES ("%s", "%s", "%s", "%s", "%s", "%s", "%s");
        ''' % tuple(item[1:8])
        
    cur.execute(sql_insert_cmd)
    
conn.commit()
conn.close()
tmp_conn.close()

conn = sqlite3.connect(db_file)
cur = conn.cursor()
cur.execute('SELECT * from ath_results')
a = cur.fetchall()
print(a[0])
print(a[100])


