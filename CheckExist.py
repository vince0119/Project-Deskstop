import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox



def _car_log(self, CardId):
    CarLogDB = "SELECT * FROM customerregistered WHERE CardId = %s"
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        value = (CardId)
        mycuror =db.cursor()
        mycuror.execute(CarLogDB, value)
        
        result = mycuror.fetchall()

        if(result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
            return False
        else:
            return True

    except mysql.connector.Error as e:  
        print('Fail')

def check_Customer(self):
    CustomerDB = "SELECT * FROM customers WHERE Id = %s"
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        value = (CardId)
        mycuror =db.cursor()
        mycuror.execute(CarLogDB, value)
        
        result = mycuror.fetchall()

        if(result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
            return False
        else:
            return True

    except mysql.connector.Error as e:  
        print('Fail')