import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM Mammiferi")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)