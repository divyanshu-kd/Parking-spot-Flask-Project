import mysql.connector

conn = mysql.connector.connect(host = 'localhost', password = '#3108', user = 'root', database = 'org')

cursor = conn.cursor()

if conn.is_connected():
    print('connection is done')

cursor.execute('SELECT * FROM worker') 
data = cursor.fetchall()
print(data)
cursor.execute("""
    UPDATE WORKER
    SET FIRST_NAME = %s
    WHERE WORKER_ID = %s
""", ('DUBEY', 1))
cursor.execute('SELECT * FROM worker') 
data = cursor.fetchall()
print(data)
conn.commit()