import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  
)
mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE Animali")
mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE Mammiferi (id char(3) primary key,Nome_Proprio varchar(30),Razza varchar(30),Peso int,Eta int)")
