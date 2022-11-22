import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import Validation

db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

def insert_data_customer_regis(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardIDCustomer.text()
        CustomerID = self.uic1.txtCustomerId.text()
        CarLicense = self.uic1.txtCarLicenseCustomer.text()
        CarColor = self.uic1.txtCarColor.text()
        CarModel = self.uic1.txtCarModel.text()
        Active = self.uic1.cbActiveCustomerRegis.currentIndex()
        
        query = ("INSERT INTO customerregistered (CardID, CustomerID, CarLicense, CarColor, CarModel, Active)" "VALUES (%s, %s, %s, %s, %s, %s)")
        val = (CardID, CustomerID, CarLicense, CarColor, CarModel, Active)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()
        

def insert_data_customers(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        FullName = self.uic1.txtFullName.text()
        PersonalId = self.uic1.txtPersonalID.text()
        Room = self.uic1.txtRoom.text()
        Active = self.uic1.cbActiveCustomer.currentIndex()
       
        if Validation.CustomerCheckValidation(self, FullName, PersonalId, Room):
            query = ("INSERT INTO customers (FullName, PersonalId, Room, Active)" "VALUES (%s, %s, %s, %s)")
            val = (FullName, PersonalId, Room, Active)
            result = mycursor.execute(query, val)

            db.commit()
            QMessageBox.about(self, 'Inserted', 'Data insert successfully')
            return True
    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()

def insert_data_guest_regis(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardIdGuest.text()
        CarLicense = self.uic1.txtCarLicenseGuest.text()
        Active = self.uic1.cbActiveGuest.currentIndex()

        query = ("INSERT INTO guestregistered (CardID, CarLicense, Active)" "VALUES (%s, %s, %s)")
        val = (CardID, CarLicense, Active)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')
        
    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()

    
        