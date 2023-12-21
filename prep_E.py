import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)
mycursor = mydb.cursor()

mycursor.execute('select * from Mammiferi where Peso > 10')
result = mycursor.fetchall()
for i in result:
    print(i)