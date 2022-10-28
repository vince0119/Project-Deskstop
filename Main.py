from pickle import load
from sqlite3.dbapi2 import connect
import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainUI import Ui_MainWindow
from TableUI import Ui_MainWindow1

import mysql.connector
from Crud import load_data_card, load_data_customer, load_data_carlog, load_data_cardType, load_data_park
from AddNew import insert_data_card, insert_data_cardtype, insert_data_park, insert_data_customer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        
        self.uic.btnTable.clicked.connect(self.showScreen)
        

    def showScreen(self):
        # self.sub_win = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self)
        # self.sub_win.show()


        self.uic1.cbCardType.addItem("Guest")
        self.uic1.cbCardType.addItem("Customer")
        self.uic1.cbCardType.setCurrentIndex(-1)

        self.HideOkAndCancelButton()
        self.HideDisableButton()
        
        #Card tab button controller
        self.uic1.btnCardNew.clicked.connect(self.CardNewButtonClick)
        self.uic1.btnCardOk.clicked.connect(self.CardOkButtonClick)
        self.uic1.btnCardCancel.clicked.connect(self.CardCancelButtonClick)
        self.uic1.btnCardDisable.clicked.connect(self.CardDisableButtonclick)
        self.uic1.btnLoadDataCard.clicked.connect(lambda: load_data_card(self))

        #Park tab button controller
        self.uic1.btnParkNew.clicked.connect(self.ParkNewButtonClick)
        self.uic1.btnParkOK.clicked.connect(self.ParkOkButtonClick)
        self.uic1.btnParkCancel.clicked.connect(self.ParkCancelButtonClick)
        self.uic1.btnParkDisable.clicked.connect(self.ParkDisableButtonClick)
        self.uic1.btnLoadDataPark.clicked.connect(lambda: load_data_park(self))

        #Car Log
        self.uic1.btnLoadDataCar.clicked.connect(lambda: load_data_carlog(self))

        #Customer tab button controller
        self.uic1.btnCustomerNew.clicked.connect(self.CustomerNewButtonClick)
        self.uic1.btnCustomerDisable.clicked.connect(self.CustomerDisableButtonClick)
        self.uic1.btnCustomerOK.clicked.connect(self.CustomerOkButtonClick)
        self.uic1.btnCustomerCancel.clicked.connect(self.CustomerCancelButtonClick)
        self.uic1.btnLoadDataCustomer.clicked.connect(lambda: load_data_customer(self))
        #Card Type tab button controller
        self.uic1.btnCardTypeNew.clicked.connect(self.CardTypeNewButtonClick)
        self.uic1.btnCardTypeOK.clicked.connect(self.CardTypeOkButtonClick)
        self.uic1.btnCardTypeCancel.clicked.connect(self.CardTypeCancelButtonClick)
        self.uic1.btnCardTypeDisable.clicked.connect(self.CardTypeDisableButtonClick)
        self.uic1.btnLoadDataCardType.clicked.connect(lambda: load_data_cardType(self))

        
        
        self.thread = {}


    #Start of Card tab Event
    def CardButtonEvent(self, _isEditing):
        self.uic1.btnCardOk.setVisible(_isEditing)
        self.uic1.btnCardCancel.setVisible(_isEditing)
        self.uic1.btnCardDisable.setEnabled(False)
        self.uic1.txtCardId.setReadOnly(not _isEditing)
        self.uic1.txtCardId.setText("")
        self.uic1.txtCardCustomer.setReadOnly(not _isEditing)
        self.uic1.txtCardCarNumber.setReadOnly(not _isEditing)
        self.uic1.txtCardCustomer.setText("")
        self.uic1.txtCardCarNumber.setText("")

    def CardNewButtonClick(self):
        self.CardButtonEvent(True)
        self.uic1.txtCardId.setFocus()
    

    def CardOkButtonClick(self):
        #get data and add to db
        insert_data_card(self)
        self.CardButtonEvent(False)
        load_data_card(self)

    def CardCancelButtonClick(self):
        self.CardButtonEvent(False)

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
        self.uic1.btnParkDisable.setEnabled(False)
        self.uic1.txtParkArea.setReadOnly(not _isEditing)
        self.uic1.txtParkArea.setText("")
        self.uic1.txtParkNo.setReadOnly(not _isEditing)
        self.uic1.txtParkNo.setText("")

    def ParkNewButtonClick(self):
        self.ParkButtonEvent(True)
        self.uic1.txtParkAvailable.setText("0")

    def ParkOkButtonClick(self):
        #get data and add to db
        if insert_data_park(self):
            self.ParkButtonEvent(False)
            load_data_park(self)
            self.uic1.txtParkAvailable.setText("")

    def ParkCancelButtonClick(self):
        self.ParkButtonEvent(False)
        self.uic1.txtParkAvailable.setText("")

    def ParkDisableButtonClick(self):
        status = self.uic1.btnParkDisable.text()
        if status == "Disable" :
            self.uic1.btnParkDisable.setText("Enable")
        else:
            self.uic1.btnParkDisable.setText("Disable")
    #End of Park tab Event

    #Start of Car Log tab Event

    #End of Card Log tab Event

    #Start of Customer tab Event
    def CustomerButtonEnvent(self,_isEditing):
        self.uic1.btnCustomerOK.setVisible(_isEditing)
        self.uic1.btnCustomerCancel.setVisible(_isEditing) 
        self.uic1.btnCustomerDisable.setEnabled(False)
        self.uic1.txtCustomerFullName.setText("")
        self.uic1.txtCustomerFullName.setReadOnly(not _isEditing) 
        self.uic1.txtCustomerRoom.setText("")
        self.uic1.txtCustomerRoom.setReadOnly(not _isEditing) 
        self.uic1.txtCustomerPersonalId.setText("")
        self.uic1.txtCustomerPersonalId.setReadOnly(not _isEditing) 


    def CustomerNewButtonClick(self):
        self.CustomerButtonEnvent(True)
        
    def CustomerOkButtonClick(self):
         # Add new Customer function
         #get data from textfield
        if insert_data_customer(self):
            self.CustomerButtonEnvent(False)
            load_data_customer(self)
        

    


    def CustomerCancelButtonClick(self):
        self.CustomerButtonEnvent(False)

    def CustomerDisableButtonClick(self):
        status = self.uic1.btnCustomerDisable.text()
        if status == "Disable" :
            self.uic1.btnCustomerDisable.setText("Enable")
        else:
            self.uic1.btnCustomerDisable.setText("Disable")
    #End of Customer tab Event

    #Start of Card Type tab Event 
    def CardTypeButtonEvent(self, _isEditing):
        self.uic1.btnCardTypeOK.setVisible(_isEditing)
        self.uic1.btnCardTypeDisable.setEnabled(False)
        self.uic1.btnCardTypeCancel.setVisible(_isEditing)
        self.uic1.txtCardTypeCardId.setReadOnly(not _isEditing)
        self.uic1.txtCardTypeCardId.setText("")
        self.uic1.cbCardType.setCurrentIndex(-1)

    def CardTypeNewButtonClick(self):
        self.CardTypeButtonEvent(True)

    def CardTypeOkButtonClick(self):
         # Add new card  function
         #get data from textfield
        insert_data_cardtype(self)
        self.CardTypeButtonEvent(False)
        load_data_cardType(self)
        

    def CardTypeCancelButtonClick(self):
        self.CardTypeButtonEvent(False)

    def CardTypeDisableButtonClick(self):
        status = self.uic1.btnCardTypeDisable.text()
        if status == "Disable" :
            self.uic1.btnCardTypeDisable.setText("Enable")
        else:
            self.uic1.btnCardTypeDisable.setText("Disable")

    #End of Card type tab event

   
        
    #Hide OK and Cancel button  
    def HideOkAndCancelButton(self):
        self.uic1.btnParkOK.setVisible(False)
        self.uic1.btnCustomerOK.setVisible(False)
        self.uic1.btnCardOk.setVisible(False)
        self.uic1.btnCardTypeOK.setVisible(False)
        self.uic1.btnCardCancel.setVisible(False)
        self.uic1.btnParkCancel.setVisible(False)
        self.uic1.btnCustomerCancel.setVisible(False)
        self.uic1.btnCardTypeCancel.setVisible(False)

    def HideDisableButton(self):
        self.uic1.btnCardDisable.setEnabled(False)
        self.uic1.btnParkDisable.setEnabled(False)
        self.uic1.btnCustomerDisable.setEnabled(False)
        self.uic1.btnCardTypeDisable.setEnabled(False)
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())