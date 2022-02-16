from asyncore import read
from pydoc import importfile
import mysql.connector as i

y=open("C:\\Users\\lenovo pc\\python\\password.txt")
pas=y.read()

log=i.connect(host="localhost",user="root",password=pas,database="library")

def addbook():
    bn=input("Enter the book name:")
    c=input("Enter the book code:")
    t=input("Enter the total number of books:")
    s=input("Enter the subject of books:")
    data = (bn,c,t,s)
    sql='insert into book values(%s,%s,%s,%s)'
    c=log.cursor()
    c.execute(sql,data)
    log.commit()
    print("Book(s) Added sucessfully")
    print("------------------------------------------------------------------")

