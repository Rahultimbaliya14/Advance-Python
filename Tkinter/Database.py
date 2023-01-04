import mysql.connector

try:
    mydb=mysql.connector.connect(host="locahost",user="root",password="")
    print("ok")
except(Exception):
    print("no",)