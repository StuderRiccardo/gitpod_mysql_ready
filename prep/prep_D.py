import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)

mycursor = mydb.cursor()
n= int(input('Vuoi aggiungere dei dati? si(0) no(1) '))
while n==0:
  sql = ('insert into Mammiferi(id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s,%s,%s,%s,%s)')
  val = []
  a = int(input('quanti animali vuoi aggiungere? '))
  for i in range(a):
    cd= input('codice dellanimale: ')
    n = input('nome dellanimale: ')
    r = input('razza dellanimale: ')
    p = input('peso dellanimale: ')
    e = input('età dellanimale: ')
    al = (cd,n,r,p,e)
    val.append(al)

  
      
  mycursor.executemany(sql,val)    
  mydb.commit()    
  mycursor.execute('select * from Mammiferi')
  myresult = mycursor.fetchall()
  for i in myresult:
    print(i)
  n= int(input('Vuoi continuare? si(0) no(1)'))
 

