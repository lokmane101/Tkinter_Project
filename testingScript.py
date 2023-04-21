import mysql.connector 
from mysql.connector import Error
connection = mysql.connector.connect(host='localhost',
                                    database='projet',
                                    user='root',
                                    password='lokmane-SQL-12')
cursorr=connection.cursor
result=cursorr.exicute("")
if connection.is_connected():
    print("connected")
else :
    print("error")
