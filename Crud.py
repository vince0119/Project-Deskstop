import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

CardReDB = 'SELECT * FROM cardregistered'
ParksDB = 'SELECT * FROM parking_area'
CarLogDB = 'SELECT * FROM cardlog'
CustomerDB = 'SELECT * FROM customers'
CarTypeDB = 'SELECT * FROM cardtype'


#load data
def load_data_card(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CardReDB)
        
        result = mycuror.fetchall()

        num = 0
        for row in result:
            num = len(row)
        self.uic1.tblCard.setRowCount(len(result))
        self.uic1.tblCard.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblCard.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    except mysql.connector.Error as e:
        print('Fail')

           

def load_data_customer(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CustomerDB)
        
        result = mycuror.fetchall()

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

def load_data_cardType(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CarTypeDB)
        
        result = mycuror.fetchall()

        num = 0
        for row in result:
            num = len(row)
        self.uic1.tblCardType.setRowCount(len(result))
        self.uic1.tblCardType.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblCardType.setItem(row_number, column_number, QTableWidgetItem(str(data)))

    except mysql.connector.Error as e:
        print('Fail')             

def load_data_carlog(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(CarLogDB)
        
        result = mycuror.fetchall()

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
