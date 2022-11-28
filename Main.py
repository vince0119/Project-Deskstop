import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread,pyqtSignal,Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from MainUI import Ui_MainWindow
from TableUI import Ui_MainWindow1
# from liveRead import plate_Detection, OpenCamera
from Crud import load_data_car_log, load_data_customer_regis, load_data_customers, load_data_guest_regis
from AddNew import insert_data_customer_regis, insert_data_guest_regis, insert_data_customers
from CheckExist import _car_log, check_CardId_Customer_Registered,check_CardId_Guest_Registered,check_Customer

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
        
        self.HideOkAndCancelButton()
        
        #Car log tab button controller
        # self.uic1.btnLoadDataCar.clicked.connect(_car_log)
        self.uic1.btnLoadDataCar.clicked.connect(lambda: load_data_car_log(self))
        self.uic1.tblCarLog.clicked.connect(self.onCellCarLog)


       

        #Guest Registered tab button controller

        self.uic1.btnGuestRegisDisable.clicked.connect(self.GuestDisableButtonclick)

        self.uic1.tblGuest.clicked.connect(self.onCell)
        self.uic1.btnLoadDataGuest.clicked.connect(lambda: load_data_guest_regis(self))
 
        #Customer Registered button controller
        self.uic1.btnCustomerRegisNew.clicked.connect(self.CustomerRegisNewButtonClick)
        self.uic1.btnCustomerRegisDisable.clicked.connect(self.CustomerRegisDisableButtonClick)
        self.uic1.btnCustomerRegisOK.clicked.connect(self.CustomerRegisOkButtonClick)
        self.uic1.btnCustomerRegisCancel.clicked.connect(self.CustomerCancelButtonClick)
        self.uic1.btnLoadDataCustomerRegis.clicked.connect(lambda: load_data_customer_regis(self))

        #Customers tab button controller
        self.uic1.btnCustomerNew.clicked.connect(self.CustomersNewButtonClick)
        self.uic1.btnCustomerOK.clicked.connect(self.CustomersOkButtonClick)
        self.uic1.btnCustomerCancel.clicked.connect(self.CustomersCancelButtonClick)
        self.uic1.btnCustomerDisable.clicked.connect(self.CustomersDisableButtonClick)
        self.uic1.btnLoadDataCustomer.clicked.connect(lambda: load_data_customers(self))


    #CarLog table click
    def onCellCarLog(self):
        row = self.uic1.tblCarLog.currentRow()
        list = []
        for i in range(self.uic1.tblCarLog.columnCount()):
            out = self.uic1.tblCarLog.item(row,i).text()
            list.append(out)
        data = list
        self.show_data_Car(data)

    def show_data_Car(self, data):
        self.uic1.cbCarLogStatus.setCurrentIndex(int(data[3]))
        self.uic1.txtRegisteredId.setText(data[1])


    #Start of Guest tab Event
    def GuestButtonEvent(self, _isEditing):
        self.uic1.btnGuestOk.setVisible(_isEditing)
        self.uic1.btnGuestCancel.setVisible(_isEditing)
        self.uic1.btnGuestDisable.setEnabled(False)
        self.uic1.txtCardIdGuest.setReadOnly(not _isEditing)
        self.uic1.txtCardIdGuest.setText("")
        self.uic1.txtCarLicenseGuest.setReadOnly(not _isEditing)
        self.uic1.txtCarLicenseGuest.setText("")
        
    def GuestDisableButtonclick(self):
        status = self.uic1.btnGuestDisable.text()
        if status == "Disable" :
            self.uic1.btnGuestDisable.setText("Enable")
        else:
            self.uic1.btnGuestDisable.setText("Disable")


    #Start of Customer Registered tab Event
    def CustomerRegisButtonEnvent(self,_isEditing):
        self.uic1.btnCustomerRegisOK.setVisible(_isEditing)
        self.uic1.btnCustomerRegisCancel.setVisible(_isEditing) 
        self.uic1.btnCustomerRegisDisable.setEnabled(False)
        self.uic1.txtCardIDCustomer.setReadOnly(not _isEditing) 
        self.uic1.txtCustomerId.setReadOnly(not _isEditing)
        self.uic1.txtCarLicenseCustomer.setReadOnly(not _isEditing)
        self.uic1.txtCarColor.setReadOnly(not _isEditing)
        self.uic1.txtCarModel.setReadOnly(not _isEditing)


    def CustomerRegisNewButtonClick(self):
        self.uic1.cbActiveCustomerRegis.setEnabled(True)
        self.CustomerRegisButtonEnvent(True)
        self.uic1.txtCardIDCustomer.setFocus()
        
    def CustomerRegisOkButtonClick(self):
         # Add new Customer function
         #get data from textfield
        if (insert_data_customer_regis(self)):
            self.CustomerRegisButtonEnvent(False)
            load_data_customer_regis(self)
        

    def CustomerCancelButtonClick(self):
        self.CustomerRegisButtonEnvent(False)

    def CustomerRegisDisableButtonClick(self):
        QMessageBox.about(self, 'asdfsdfsadf','asdfasdfsa')
        status = self.uic1.btnCustomerRegisDisable.text()
        if status == "Disable" :
            self.uic1.btnCustomerRegisDisable.setText("Enable")
        else:
            self.uic1.btnCustomerRegisDisable.setText("Disable")
    #End of Customer tab Event

    #Start of Customers tab Event 
    def CustomersButtonEvent(self, _isEditing):
        self.uic1.btnCustomerOK.setVisible(_isEditing)
        self.uic1.btnCustomerDisable.setEnabled(False)
        self.uic1.btnCustomerCancel.setVisible(_isEditing)
        self.uic1.txtFullName.setReadOnly(not _isEditing)
        self.uic1.txtPersonalID.setReadOnly(not _isEditing)
        self.uic1.txtRoom.setReadOnly(not _isEditing)

    def CustomersNewButtonClick(self):
        self.uic1.cbActiveCustomer.setEnabled(True)
        self.CustomersButtonEvent(True)
        self.uic1.txtFullName.setFocus()

    def CustomersOkButtonClick(self):
         # Add new card  function
         #get data from textfield
        if (insert_data_customers(self)):
            self.CustomersButtonEvent(False)
            load_data_customers(self)
        

    def CustomersCancelButtonClick(self):
        self.CustomersButtonEvent(False)

    def CustomersDisableButtonClick(self):
        CustomerId = self.uic1 #get on table
            #run database to disable that customer

    #End of Card type tab event

    # show text
    def onCell(self):
        row = self.uic1.tblGuest.currentRow()
        list = []
        for i in range(self.uic1.tblGuest.columnCount()):
            out = self.uic1.tblGuest.item(row,i).text()
            list.append(out)
        data = list
        self.show_data(data)

    def show_data(self, data):
        self.uic1.txtCardIdGuest.setText(data[1])
        self.uic1.txtCarLicenseGuest.setText(data[2])

    #Hide OK and Cancel button  
    def HideOkAndCancelButton(self):
        self.uic1.btnCustomerRegisOK.setVisible(False)
        self.uic1.btnCustomerOK.setVisible(False)
        self.uic1.btnCustomerRegisCancel.setVisible(False)
        self.uic1.btnCustomerCancel.setVisible(False)

    
    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())