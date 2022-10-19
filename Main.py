import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from MainUI import Ui_MainWindow
from TableUI import Ui_MainWindow1

import mysql.connector

db = mysql.connector.connect(user = 'root', password = '1234', host = '127.0.0.1', database = 'asp')

CardReDB = 'SELECT * FROM cardregistered LIMIT 0, 5'
ParksDB = 'SELECT * FROM parking_area LIMIT 0, 5'
CarLogDB = 'SELECT * FROM cardlog LIMIT 0, 5'
UserDB = 'SELECT * FROM users LIMIT 0, 5'
CarTypeDB = 'SELECT * FROM cardtype LIMIT 0, 5'
StaffDB = 'SELECT * FROM staffs LIMIT 0, 5'

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        
        self.uic.btnTable.clicked.connect(self.showScreen)
        


    def showScreen(self):
        self.sub_win = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self.sub_win)
        self.sub_win.show()

        self.uic1.cbCardType.addItem("User")
        self.uic1.cbCardType.addItem("Guest")
        self.uic1.cbCardType.setCurrentIndex(-1)
        self.HideOkAndCancelButton()
        self.uic1.btnLoadDataStaffs.clicked.connect(self.load_data_staffs)
        
        #Card tab button controller
        self.uic1.btnCardNew.clicked.connect(self.CardNewButtonClick)
        self.uic1.btnCardOk.clicked.connect(self.CardOkButtonClick)
        self.uic1.btnCardCancel.clicked.connect(self.CardCancelButtonClick)
        self.uic1.btnCardDisable.clicked.connect(self.CardDisableButtonclick)

        #Park tab button controller
        self.uic1.btnParkNew.clicked.connect(self.ParkNewButtonClick)
        self.uic1.btnParkOK.clicked.connect(self.ParkOkButtonClick)
        self.uic1.btnParkCancel.clicked.connect(self.ParkCancelButtonClick)
        self.uic1.btnParkDisable.clicked.connect(self.ParkDisableButtonClick)


        #User tab button controller
        self.uic1.btnUserNew.clicked.connect(self.UserNewButtonClick)
        self.uic1.btnUserDisable.clicked.connect(self.UserDisableButtonClick)
        self.uic1.btnUserOK.clicked.connect(self.UserOkButtonClick)
        self.uic1.btnUserCancel.clicked.connect(self.UserCancelButtonClick)

        #Card Type tab button controller
        self.uic1.btnCardTypeNew.clicked.connect(self.CardTypeNewButtonClick)
        self.uic1.btnCardTypeOK.clicked.connect(self.CardTypeOkButtonClick)
        self.uic1.btnCardTypeCancel.clicked.connect(self.CardTypeCancelButtonClick)
        self.uic1.btnCardTypeDisable.clicked.connect(self.CardTypeDisableButtonClick)

        #Staff tab button controller
        self.uic1.btnStaffNew.clicked.connect(self.StaffNewButtonClick)
        self.uic1.btnStaffDisable.clicked.connect(self.StaffDisableButtonClick)
        self.uic1.btnStaffOK.clicked.connect(self.StaffOKButtonClick)
        self.uic1.btnStaffCancel.clicked.connect(self.StaffCancelButtonClick)
        
        self.thread = {}

    def load_data_staffs(self):
        
        mycuror =db.cursor()
        mycuror.execute(StaffDB)
        result = mycuror.fetchall()
        print(result)

        self.uic1.tblStaff.setRowCount(11)
        self.uic1.tblStaff.setColumnCount(7)

        table_row = 0
        for row in result:
            self.uic1.tblStaff.setItem(table_row, 0 , QTableWidgetItem(row[0]))
            self.uic1.tblStaff.setItem(table_row, 1 , QTableWidgetItem(row[1]))
            self.uic1.tblStaff.setItem(table_row, 2 , QTableWidgetItem(row[2]))
            self.uic1.tblStaff.setItem(table_row, 3 , QTableWidgetItem(row[3]))
            self.uic1.tblStaff.setItem(table_row, 4 , QTableWidgetItem(row[4]))
            self.uic1.tblStaff.setItem(table_row, 5 , QTableWidgetItem(str(row[5])))
            self.uic1.tblStaff.setItem(table_row, 6 , QTableWidgetItem(str(row[6])))
            table_row += 1


    #Start of Card tab Event
    def CardButtonEvent(self, _isEditing):
        self.uic1.btnCardOk.setVisible(_isEditing)
        self.uic1.btnCardCancel.setVisible(_isEditing)
        self.uic1.txtCardId.setReadOnly(not _isEditing)
        self.uic1.txtCardId.setText("")
        self.uic1.txtCardUser.setReadOnly(not _isEditing)
        self.uic1.txtCardCarNumber.setReadOnly(not _isEditing)
        self.uic1.txtCardUser.setText("")
        self.uic1.txtCardCarNumber.setText("")

    def CardNewButtonClick(self):
        self.CardButtonEvent(True)
        self.uic1.txtCardCreator.setText("admin")

    def CardOkButtonClick(self):
        #get data and add to db
        self.CardButtonEvent(False)
        self.uic1.txtCardCreator.setText("")

    def CardCancelButtonClick(self):
        self.CardButtonEvent(False)
        self.uic1.txtCardCreator.setText("")

    def CardDisableButtonclick(self):
        status = self.uic1.btnCardDisable.text()
        if status == "Disable" :
            self.uic1.btnCardDisable.setText("Enable")
        else:
            self.uic1.btnCardDisable.setText("Disable")
    #End of Card tab Event

    #Start of Park tab Event
    def ParkButtonEvent(self,_isEditing):
        self.uic1.btnParkOK.setVisible(_isEditing)
        self.uic1.btnParkCancel.setVisible(_isEditing)
        self.uic1.txtParkArea.setReadOnly(not _isEditing)
        self.uic1.txtParkArea.setText("")
        self.uic1.txtParkNoS.setReadOnly(not _isEditing)
        self.uic1.txtParkNoS.setText("")

    def ParkNewButtonClick(self):
        self.ParkButtonEvent(True)
        self.uic1.txtParkAvailable.setText("0")
        self.uic1.txtParkCreator.setText("admin")

    def ParkOkButtonClick(self):
        #get data and add to db
        self.ParkButtonEvent(False)
        self.uic1.txtParkAvailable.setText("")
        self.uic1.txtParkCreator.setText("")

    def ParkCancelButtonClick(self):
        self.ParkButtonEvent(False)
        self.uic1.txtParkAvailable.setText("")
        self.uic1.txtParkCreator.setText("")

    def ParkDisableButtonClick(self):
        status = self.uic1.btnParkDisable.text()
        if status == "Disable" :
            self.uic1.btnParkDisable.setText("Enable")
        else:
            self.uic1.btnParkDisable.setText("Disable")
    #End of Park tab Event

    #Start of Car Log tab Event

    #End of Card Log tab Event

    #Start of User tab Event
    def UserButtonEnvent(self,_isEditing):
        self.uic1.btnUserOK.setVisible(_isEditing)
        self.uic1.btnUserCancel.setVisible(_isEditing) 
        self.uic1.txtUserEmail.setText("")
        self.uic1.txtUserEmail.setReadOnly(not _isEditing)   
        self.uic1.txtUserFullName.setText("")
        self.uic1.txtUserFullName.setReadOnly(not _isEditing) 
        self.uic1.txtUserPersonalId.setText("")
        self.uic1.txtUserPersonalId.setReadOnly(not _isEditing) 
        self.uic1.txtUserPhoneNumber.setText("")
        self.uic1.txtUserPhoneNumber.setReadOnly(not _isEditing)
        # self.uic1.btnUserDisable.setEnabled(not _isEditing)
    
    def UserNewButtonClick(self):
        self.UserButtonEnvent(True)
        self.uic1.txtUserCreator.setText("admin")
        
    def UserOkButtonClick(self):
         # Add new user function
         #get data from textfield
        self.UserButtonEnvent(False)
        self.uic1.txtUserCreator.setText("")
        

    def UserCancelButtonClick(self):
        self.UserButtonEnvent(False)
        self.uic1.txtUserCreator.setText("")

    def UserDisableButtonClick(self):
        status = self.uic1.btnUserDisable.text()
        if status == "Disable" :
            self.uic1.btnUserDisable.setText("Enable")
        else:
            self.uic1.btnUserDisable.setText("Disable")
    #End of User tab Event

    #Start of Card Type tab Event 
    def CardTypeButtonEvent(self, _isEditing):
        self.uic1.btnCardTypeOK.setVisible(_isEditing)
        self.uic1.btnCardTypeCancel.setVisible(_isEditing)
        self.uic1.txtCardTypeCardId.setReadOnly(not _isEditing)
        self.uic1.txtCardTypeCardId.setText("")
        self.uic1.cbCardType.setCurrentIndex(-1)

    def CardTypeNewButtonClick(self):
        self.CardTypeButtonEvent(True)
        self.uic1.txtCardTypeCreator.setText("admin")

    def CardTypeOkButtonClick(self):
         # Add new card  function
         #get data from textfield
        self.CardTypeButtonEvent(False)
        self.uic1.txtCardTypeCreator.setText("")
        

    def CardTypeCancelButtonClick(self):
        self.CardTypeButtonEvent(False)
        self.uic1.txtCardTypeCreator.setText("")

    def CardTypeDisableButtonClick(self):
        status = self.uic1.btnCardTypeDisable.text()
        if status == "Disable" :
            self.uic1.btnCardTypeDisable.setText("Enable")
        else:
            self.uic1.btnCardTypeDisable.setText("Disable")

    #End of Card type tab event

    #Start of Staff tab Event
    def StaffButtonEvent(self, _isEditing):
        self.uic1.btnStaffOK.setVisible(_isEditing)
        self.uic1.btnStaffCancel.setVisible(_isEditing)
        self.uic1.txtStaffUserName.setReadOnly(not _isEditing)
        self.uic1.txtStaffPassword.setReadOnly(not _isEditing)
        self.uic1.txtStaffFullName.setReadOnly(not _isEditing)
        self.uic1.txtStaffAddress.setReadOnly(not _isEditing)
        self.uic1.txtStaffPersonalId.setReadOnly(not _isEditing)
        self.uic1.txtStaffUserName.setText("")
        self.uic1.txtStaffPassword.setText("")
        self.uic1.txtStaffFullName.setText("")
        self.uic1.txtStaffAddress.setText("")
        self.uic1.txtStaffPersonalId.setText("")

    def StaffNewButtonClick(self):
        self.StaffButtonEvent(True)

    def StaffDisableButtonClick(self):
        status = self.uic1.btnStaffDisable.text()
        if status == "Disable" :
            self.uic1.btnStaffDisable.setText("Enable")
        else:
            self.uic1.btnStaffDisable.setText("Disable")

    def StaffOKButtonClick(self):
        #get data from textfield
        self.StaffButtonEvent(False)

    def StaffCancelButtonClick(self):
        self.StaffButtonEvent(False)
    #End of Staff tab Event
        
    #Hide OK and Cancel button  
    def HideOkAndCancelButton(self):
        self.uic1.btnParkOK.setVisible(False)
        self.uic1.btnUserOK.setVisible(False)
        self.uic1.btnCardOk.setVisible(False)
        self.uic1.btnStaffOK.setVisible(False)
        self.uic1.btnCardTypeOK.setVisible(False)
        self.uic1.btnCardCancel.setVisible(False)
        self.uic1.btnParkCancel.setVisible(False)
        self.uic1.btnUserCancel.setVisible(False)
        self.uic1.btnStaffCancel.setVisible(False)
        self.uic1.btnCardTypeCancel.setVisible(False)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())