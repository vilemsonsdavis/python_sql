import psycopg2 as pg2

conn =pg2.connect(database='dvdrental', user='postgres', password='Madrid123#') #make connection

cur = conn.cursor() # make cursor

cur.execute('SELECT * FROM payment') #make query
print(cur.fetchone()) #fetch some shit

conn.close() #closes connection





