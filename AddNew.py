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
        
        query = ("INSERT INTO customerregistered (CardID, CustomerID, CarLicense, CarColor, CarModel)" "VALUES (%s, %s, %s, %s, %s)")
        val = (CardID, CustomerID, CarLicense, CarColor, CarModel)

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
       
        if Validation.CustomerCheckValidation(self, FullName, PersonalId, Room):
            query = ("INSERT INTO customers (FullName, PersonalId, Room)" "VALUES (%s, %s, %s)")
            val = (FullName, PersonalId, Room)
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

        query = ("INSERT INTO guestregistered (CardID, CarLicense)" "VALUES (%s, %s)")
        val = (CardID, CarLicense )

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')
        
    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()

    
        