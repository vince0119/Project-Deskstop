import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def Disable_Customer(self,id):
    db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
    mycursor = db.cursor()
    value = (id)
    query = "UPDATE customers SET active = 0 WHERE id = %s"
    try:
        mycursor.execute(query,(value,))
        db.commit()
        return True
    except:
        db.rollback()
        return False

def Disable_Customer_regis(self,id):
    db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
    mycursor = db.cursor()
    value = (id)
    query = "UPDATE customerregistered SET active = 0 WHERE id = %s"
    try:
        mycursor.execute(query,(value,))
        db.commit()
        return True
    except:
        db.rollback()
        return False
        

def Disable_Guest_regis(self,id):
    db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
    mycursor = db.cursor()
    value = (id)
    query = "UPDATE guestregistered SET active = 0 WHERE id = %s"
    try:
        mycursor.execute(query,(value,))
        db.commit()
        return True
    except:
        db.rollback()
        return False
