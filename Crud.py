from unittest import result
import mysql.connector
import numpy

db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='asp')

code_8 = 'SELECT * FROM staffs'
mycursor = db.cursor()
mycursor.execute(code_8)

result = mycursor.fetchall()

print(result)