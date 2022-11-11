import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox

CarLogDB = 'SELECT * FROM carlog'
CustomerReDB = 'SELECT * FROM customerregistered'
CustomerDB = 'SELECT * FROM customers'
GuestReDB = 'SELECT * FROM guestregistered'


#load data
def load_data_car_log(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CarLogDB)
        
        result = mycuror.fetchall()
        if(result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
            return
        else:
            num = 0
        for row in result:
            num = len(row)
        self.uic1.tblCarLog.setRowCount(len(result))
        self.uic1.tblCarLog.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblCarLog.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:  
        print('Fail')

def load_data_customer_regis(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CustomerReDB)
        
        result = mycuror.fetchall()
        if (result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
            return
        else:
            num = 0
        for row in result:
            num = len(row)
        self.uic1.tblCustomerRegis.setRowCount(len(result))
        self.uic1.tblCustomerRegis.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblCustomerRegis.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    except mysql.connector.Error as e:
        print('Fail')

def load_data_customers(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CustomerDB)
        
        result = mycuror.fetchall()
        if(result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
            return
        else:
            num = 0
        for row in result:
            num = len(row)
        self.uic1.tblCustomer.setRowCount(len(result))
        self.uic1.tblCustomer.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblCustomer.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:
        print('Fail')             

def load_data_guest_regis(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(GuestReDB)
        
        result = mycuror.fetchall()
        if(result == []):
            QMessageBox.about(self, 'Error', 'No data in table')
        else:
            num = 0
        for row in result:
            num = len(row)
        self.uic1.tblGuest.setRowCount(len(result))
        self.uic1.tblGuest.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblGuest.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:
        print('Fail')             
