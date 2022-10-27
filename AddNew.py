import mysql.connector
from PyQt5.QtWidgets import QMessageBox
import Validation

db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

def insert_data_card(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardId.text()
        User = self.uic1.txtCardUser.text()
        CarLicense = self.uic1.txtCardCarNumber.text()
        
        query = ("INSERT INTO cardregistered (CardID, User, CarLicense)" "VALUES (%s, %s, %s)")
        val = (CardID, User, CarLicense)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()
        
def insert_data_park(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        Area = self.uic1.txtParkArea.text()
        NumOfSlot = self.uic1.txtParkNo.text()
        Available = self.uic1.txtParkAvailable.text()

        query = ("INSERT INTO parking_area (Area, NumOfSlot, Available)" "VALUES (%s, %s, %s)")
        val = (Area, NumOfSlot, Available)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()

def insert_data_user(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        FullName = self.uic1.txtUserFullName.text()
        PersonalId = self.uic1.txtUserPersonalId.text()
        PhoneNum = self.uic1.txtUserPhoneNumber.text()
        Email = self.uic1.txtUserEmail.text()

        query = ("INSERT INTO users (FullName, PersonalId, PhoneNum, Email)" "VALUES (%s, %s, %s, %s)")
        val = (FullName, PersonalId, PhoneNum, Email)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()

def insert_data_cardtype(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        CardID = self.uic1.txtCardTypeCardId.text()
        CardType = self.uic1.cbCardType.currentIndex()
        CreatedBy = self.uic1.txtCardTypeCreator.text()

        query = ("INSERT INTO cardtype (CardID, CardType, CreatedBy)" "VALUES (%s, %s,%s)")
        val = (CardID, CardType, CreatedBy)

        result = mycursor.execute(query, val)

        db.commit()
        QMessageBox.about(self, 'Inserted', 'Data insert successfully')

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
    finally:
        db.close()

def insert_data_staff(self):
    try:
        db = mysql.connector.connect(user='root', password='1234', host='127.0.0.1', database='APS')

        mycursor = db.cursor()

        UserName = self.uic1.txtStaffUserName.text()
        Password = self.uic1.txtStaffPassword.text()
        FullName = self.uic1.txtStaffFullName.text()
        PersonalId = self.uic1.txtStaffPersonalId.text()
        Address = self.uic1.txtStaffAddress.text()
        Phone =self.uic1.txtStaffPhone.text()
        
        if Validation.StaffCheckFormat(self,UserName,Password,FullName,PersonalId,Address,Phone) :
            query = ("INSERT INTO staffs (UserName, Password, FullName, PersonalId, Address, Phone)" "VALUES (%s, %s, %s, %s, %s, %s)")
            val = (UserName, Password, FullName, PersonalId, Address,Phone)

            result = mycursor.execute(query, val)

            db.commit()
            QMessageBox.about(self, 'Inserted', 'Data insert successfully')
            return True
        

    except mysql.connector.Error as e:
        QMessageBox.about(self, ' Fail', 'Insert Failed!!!')
        return False
    finally:
        db.close()
        
    
        