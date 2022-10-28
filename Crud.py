import mysql.connector
from PyQt5.QtWidgets import QTableWidgetItem

CardReDB = 'SELECT * FROM cardregistered'
ParksDB = 'SELECT * FROM parking_area'
CarLogDB = 'SELECT * FROM cardlog'
UserDB = 'SELECT * FROM users'
CarTypeDB = 'SELECT * FROM cardtype'
StaffDB = 'SELECT * FROM staffs'


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

def load_data_park(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(ParksDB)
        
        result = mycuror.fetchall()

        num = 0
        for row in result:
            num = len(row)
        self.uic1.tblPark.setRowCount(len(result))
        self.uic1.tblPark.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblPark.setItem(row_number, column_number, QTableWidgetItem(str(data)))
    except mysql.connector.Error as e:
        print('Fail')            

def load_data_user(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(UserDB)
        
        result = mycuror.fetchall()

        num = 0
        for row in result:
            num = len(row)
        self.uic1.tblUser.setRowCount(len(result))
        self.uic1.tblUser.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblUser.setItem(row_number, column_number, QTableWidgetItem(str(data)))
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

def load_data_staffs(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')
        mycuror =db.cursor()
        mycuror.execute(StaffDB)
        
        result = mycuror.fetchall()

        num = 0
        for row in result:
            num = len(row)
        self.uic1.tblStaff.setRowCount(len(result))
        self.uic1.tblStaff.setColumnCount(num)

        for row_number, row_data in enumerate(result):
            for column_number, data in enumerate(row_data):
                self.uic1.tblStaff.setItem(row_number, column_number, QTableWidgetItem(str(data)))
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
