import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)
mycursor = mydb.cursor()

sql = ('insert into Mammiferi(id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s,%s,%s,%s,%s)')
val = [
  ('001','Luca', 'gatto', '12','4'),
  ('002','Totti', 'cane', '3','5'),
  ('003','Lele', 'cane', '7','2'),
  ('004','Luini', 'gatto', '9','4'),
  ('005','Bomba', 'cane', '12','3')
]

mycursor.executemany(sql, val)

mydb.commit()

print(mycursor.rowcount, "was inserted.")