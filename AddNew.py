import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import Validation

db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

def insert_data_card(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardId.text()
        CustomerID = self.uic1.txtCardCustomerId.text()
        CarLicense = self.uic1.txtCardCarNumber.text()
        
        query = ("INSERT INTO cardregistered (CardID, CustomerId, CarLicense)" "VALUES (%s, %s, %s)")
        val = (CardID, CustomerID, CarLicense)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()
        

def insert_data_customer(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        FullName = self.uic1.txtCustomerFullName.text()
        PersonalId = self.uic1.txtCustomerPersonalId.text()
        Room =self.uic1.txtCustomerRoom.text()
       
        if Validation.CustomerCheckValidation(self,FullName,PersonalId,Room):
            query = ("INSERT INTO customers (FullName, PersonalId, Room)" "VALUES (%s, %s, %s)")
            val = (FullName, PersonalId,Room)

            result = mycursor.execute(query, val)

            db.commit()
            QMessageBox.about(self, 'Inserted', 'Data insert successfully')
            return True
    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()

def insert_data_cardtype(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardTypeCardId.text()
        CardType = self.uic1.cbCardType.currentIndex()

        query = ("INSERT INTO cardtype (CardID, CardType)" "VALUES (%s, %s)")
        val = (CardID, CardType)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')
        return True
    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()

    
        