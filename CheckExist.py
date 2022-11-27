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

def check_Customer(self,CustomerId,showInactive):
    CustomerDB = "SELECT * FROM customers WHERE Id = %s"
    if(not showInactive):
        CustomerDB+=" and active =1"
    
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        value = (CustomerId)
        mycuror =db.cursor()
        mycuror.execute(CustomerDB, value)
        
        result = mycuror.fetchall()

        return result

    except mysql.connector.Error as e:  
        QMessageBox.about(self, ' Fail', 'Connect database failed!!!')
    finally:
        db.close()

def check_CardId_Customer_Registered(self, CardId,showInactive): #dùng để check card id, cái showInactive để true khi search, false khi thêm mới
    CustomerRegisteredDB = "SELECT * FROM customerregistered WHERE CardId = %s"
    if(not showInactive):
        CustomerRegisteredDB+=" and active =1"
    
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        value = (CardId)
        mycuror =db.cursor()
        mycuror.execute(CustomerRegisteredDB, value)
        
        result = mycuror.fetchall()

        return result

    except mysql.connector.Error as e:  
        QMessageBox.about(self, ' Fail', 'Connect database failed!!!')
    finally:
        db.close()

def check_CardId_Guest_Registered(self, CardId,showInactive):