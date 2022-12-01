from ast import List
import datetime
import sys
import cv2
import numpy as np
from PyQt5 import QtGui
from PyQt5.QtCore import QThread,pyqtSignal,Qt, pyqtSlot,QThread
from PyQt5.QtGui import QPixmap

from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView,QWidget

from MainUI import Ui_MainWindow
from TableUI import Ui_MainWindow1
# from liveRead import plate_Detection, OpenCamera
from Crud import load_data_car_log, load_data_customer_regis, load_data_customers, load_data_guest_regis
from AddNew import insert_data_customer_regis, insert_data_guest_regis, insert_data_customers
from CheckExist import _car_log, check_CardId_Customer_Registered,check_CardId_Guest_Registered,check_Customer

import keyboard
import liveRead

from CheckDisable import Disable_Guest


Status = "In"
class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self, index):
        self.index = index
        super(VideoThread, self).__init__()
    def run(self):
        cap = cv2.VideoCapture(self.index)
        
        while cap.isOpened():
            ret, cv_img = cap.read()
           
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            global Status  
            
            now ="today"  
            if self.index==0:
                if  Status=="In":
                    CarLicense = liveRead.OpenCamera(cv_img)
                    print(CarLicense)
                    # Status="None"
                if(keyboard.is_pressed("x")):
                    
                    cv2.imwrite('./image_log/in-'+now+'.jpg',cv_img)
            if self.index==1:
                if(keyboard.is_pressed("z")):
                    cv2.imwrite("./image_log/out-.jpg",cv_img)
        cap.release()

    def stop(self):
        self.terminate()
        
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self)
        
        self.threads: List[VideoThread] =[]
        self.thread0 = VideoThread(0)
        self.thread1=VideoThread(1)
        # connect its signal to the update_image slot
        self.thread0.change_pixmap_signal.connect(self.update_image_in)
        self.thread1.change_pixmap_signal.connect(self.update_image_out)
        self.threads.append(self.thread1)
        self.threads.append(self.thread0)
        # start the thread
        for slot in self.threads:
            slot.start()
        self.uic.btnTable.clicked.connect(self.showScreen)
        
        
    def closeEvent(self):
        self.thread0.stop()
        self.thread1.stop()
        
    def read():
        global Status
        Status="In"
    def showScreen(self):

        self.closeEvent()

        self.sub_win = QMainWindow()
        self.uic1 = Ui_MainWindow1()
        self.uic1.setupUi(self.sub_win)
        self.sub_win.show()

        self.HideOkAndCancelButton()
        
        #Car log tab button controller
        # self.uic1.btnLoadDataCar.clicked.connect(_car_log)
        self.uic1.btnLoadDataCar.clicked.connect(lambda: load_data_car_log(self))
        self.uic1.tblCarLog.clicked.connect(self.onCellCarLog)
        self.uic1.tblCarLog.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)


       

        #Guest Registered tab button controller

        self.uic1.btnGuestRegisDisable.clicked.connect(lambda: Disable_Guest(self))

        self.uic1.tblGuest.clicked.connect(self.onCellGuest)
        self.uic1.tblGuest.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.uic1.btnLoadDataGuest.clicked.connect(lambda: load_data_guest_regis(self))
 
        #Customer Registered button controller
        self.uic1.btnCustomerRegisNew.clicked.connect(self.CustomerRegisNewButtonClick)
        self.uic1.btnCustomerRegisDisable.clicked.connect(self.CustomerRegisDisableButtonClick)
        self.uic1.btnCustomerRegisOK.clicked.connect(self.CustomerRegisOkButtonClick)

        self.uic1.btnCustomerRegisCancel.clicked.connect(self.CustomersCancelButtonClick)
        self.uic1.tblCustomerRegis.clicked.connect(self.onCellCustomerRegis)
        self.uic1.tblCustomerRegis.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
        self.uic1.btnLoadDataCustomerRegis.clicked.connect(lambda: load_data_customer_regis(self))

        #Customers tab button controller
        self.uic1.btnCustomerNew.clicked.connect(self.CustomersNewButtonClick)
        self.uic1.btnCustomerOK.clicked.connect(self.CustomersOkButtonClick)
        self.uic1.btnCustomerCancel.clicked.connect(self.CustomersCancelButtonClick)
        self.uic1.btnCustomerDisable.clicked.connect(self.CustomersDisableButtonClick)
        self.uic1.tblCustomer.clicked.connect(self.onCellCustomer)
        self.uic1.tblCustomer.horizontalHeader().setSectionResizeMode(0, QHeaderView.ResizeToContents)
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
        self.uic1.txtDisableByCarLicense.setReadOnly(not _isEditing)
        self.uic1.txtDisableByCarLicense.setText("")

        
    def GuestDisableButtonclick(self):
        status = self.uic1.btnGuestRegisDisable.text()
        if status == "Disable" :
            self.uic1.btnGuestRegisDisable.setText("Enable")
        else:
            self.uic1.btnGuestRegisDisable.setText("Disable")


    # guest table click
    def onCellGuest(self):
        row = self.uic1.tblGuest.currentRow()
        list = []
        for i in range(self.uic1.tblGuest.columnCount()):
            out = self.uic1.tblGuest.item(row,i).text()
            list.append(out)
        data = list
        self.show_data_Guest(data)

    def show_data_Guest(self, data):
        self.uic1.txtDisableByCarLicense.setText(data[2])



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
        self.uic1.txtCardIDCustomer.setText("") 
        self.uic1.txtCustomerId.setText("")
        self.uic1.txtCarLicenseCustomer.setText("")
        self.uic1.txtCarColor.setText("")
        self.uic1.txtCarModel.setText("")


    def CustomerRegisNewButtonClick(self):
        self.CustomerRegisButtonEnvent(True)
        self.uic1.txtCardIDCustomer.setFocus()
        
    def CustomerRegisOkButtonClick(self):
         # Add new Customer function
         #get data from textfield
        if (insert_data_customer_regis(self)):
            self.CustomerRegisButtonEnvent(False)
            load_data_customer_regis(self)
        

    def CustomerRegisteredCancelButtonClick(self):
        self.CustomerRegisButtonEnvent(False)

    def CustomerRegisDisableButtonClick(self):
        status = self.uic1.btnCustomerRegisDisable.text()
        if status == "Disable" :
            self.uic1.btnCustomerRegisDisable.setText("Enable")
        else:
            self.uic1.btnCustomerRegisDisable.setText("Disable")
    
    # customer regis table click
    def onCellCustomerRegis(self):

        self.CustomerCancelButtonClick()

        row = self.uic1.tblCustomerRegis.currentRow()
        list = []
        for i in range(self.uic1.tblCustomerRegis.columnCount()):
            out = self.uic1.tblCustomerRegis.item(row,i).text()
            list.append(out)
        data = list
        self.show_data_CustomerRegis(data)

    def show_data_CustomerRegis(self, data):
        self.uic1.txtCardIDCustomer.setText(data[1])
        self.uic1.txtCustomerId.setText(data[2])
        self.uic1.txtCarLicenseCustomer.setText(data[3])
        self.uic1.txtCarColor.setText(data[4])
        self.uic1.txtCarModel.setText(data[5])
    #End of Customer tab Event

    #Start of Customers tab Event 
    def CustomersButtonEvent(self, _isEditing):
        self.uic1.btnCustomerOK.setVisible(_isEditing)
        self.uic1.btnCustomerDisable.setEnabled(False)
        self.uic1.btnCustomerCancel.setVisible(_isEditing)
        self.uic1.txtFullName.setReadOnly(not _isEditing)
        self.uic1.txtPersonalID.setReadOnly(not _isEditing)
        self.uic1.txtRoom.setReadOnly(not _isEditing)
        self.uic1.txtFullName.setText("")
        self.uic1.txtPersonalID.setText("")
        self.uic1.txtRoom.setText("")

    def CustomersNewButtonClick(self):
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
    def onCellCustomer(self):

        self.CustomersCancelButtonClick()

        row = self.uic1.tblCustomer.currentRow()
        list = []
        for i in range(self.uic1.tblCustomer.columnCount()):
            out = self.uic1.tblCustomer.item(row,i).text()
            list.append(out)
        data = list
        self.show_data_Customer(data)

    def show_data_Customer(self, data):
        self.uic1.txtFullName.setText(data[1])
        self.uic1.txtPersonalID.setText(data[2])
        self.uic1.txtRoom.setText(data[3])

    #Hide OK and Cancel button  
    def HideOkAndCancelButton(self):
        self.uic1.btnCustomerRegisOK.setVisible(False)
        self.uic1.btnCustomerOK.setVisible(False)
        self.uic1.btnCustomerRegisCancel.setVisible(False)
        self.uic1.btnCustomerCancel.setVisible(False)

    
    #Image captured show
    @pyqtSlot(np.ndarray)
    def update_image_in(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamIn.setPixmap(qt_img)
    def update_image_out(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamOut.setPixmap(qt_img)
    
    def convert_cv_qt(self, cv_img):
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(640, 480, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)

    

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())

