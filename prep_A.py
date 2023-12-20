import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='Animali'
)

mycursor = mydb.cursor()
n= int(input('Vuoi aggiungere dei numeri? si(0) no(1)'))
while(n!=0){
    cd== input('codice dellanimale:'),
    n == input('nome dellanimale:'),
    r == input('razza dellanimale:'),
    p == input('peso dellanimale:'),
    e == input('età dellanimale:'),
    sql = ('insert into Mammiferi(id, Nome_Proprio, Razza,)')
 
}
