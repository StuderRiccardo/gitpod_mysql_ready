import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)

mycursor = mydb.cursor()
sql = 'insert into Mammiferi(id,Nome_Proprio,Razza,Peso,Eta) values (%s,%s,%s,%i,%i)'
val = ('001','Luca','gatto',12,4)



mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")
