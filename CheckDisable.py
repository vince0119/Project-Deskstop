import mysql.connector
from PyQt5.QtWidgets import QMessageBox

def Disable_Guest(self):
    db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
    mycursor = db.cursor()
    check = self.uic1.btnGuestRegisDisable.text()
    query = "UPDATE * FROM Guestregistered WHERE Active = %s"
    try:
        mycursor.execute(query)
        db.commit()
        
    except :  
        db.rollback()
    
    query = "SELECT* from guestregistered "

    mycursor.execute(query)

    print(mycursor.fetchall())