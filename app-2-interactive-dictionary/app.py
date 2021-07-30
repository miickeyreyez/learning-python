import mysql.connector

con = mysql.connector.connect(
  user = 'root',
  password = '',
  host = '127.0.0.01',
  database = 'mysql'
)

cursor = con.cursor()

query = cursor.execute('show databases')

results = cursor.fetchall()

print(results)