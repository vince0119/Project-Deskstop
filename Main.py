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
from AddNew import insert_data_customer_regis, insert_data_guest_regis, insert_data_customers, insert_car_log
# from CheckExist import _car_log, check_CardId_Customer_Registered,check_CardId_Guest_Registered,check_Customer
import keyboard
from liveRead import OpenCamera
import Validation
from CheckDisable import Disable_Customer, Disable_Customer_regis, Disable_Guest_regis
import CheckExist

Way = "In"
CardId="OIMKMLA"
CarLicense="29E23467"
Date=""


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)
    def __init__(self, index):
        self.index = index
        super(VideoThread, self).__init__()
    def clearGlobal(self,message):
        global  Way,Message,Date,CardId,CarLicense  
        
        Way =""
        Date=""
        CardId=""
        CarLicense="" 
        print(message) 
    def run(self):
        cap = cv2.VideoCapture(self.index,cv2.CAP_DSHOW)
        
        while cap.isOpened():
            ret, cv_img = cap.read()
           
            if ret:
                self.change_pixmap_signal.emit(cv_img)
            global Way,Date,CardId,CarLicense  
            
           
            if self.index==0:
               if (Date!="" and Way=="In"):
                    cv2.imwrite("./Carlog/"+Date+"-Front-In",cv_img)
                    self.clearGlobal("1In")
            if self.index==1:
                if (Date!="" and Way=="Out"):
                    cv2.imwrite("./Carlog/"+Date+"-Front-Out",cv_img)
                    self.clearGlobal("1Out")
            if self.index==2:
                if (Way=="In"):
                    # CarLicense=OpenCamera(cv_img)
                    if (Validation.ValidCarLicense(CarLicense)):
                        resultCustomer =CheckExist.check_CardId_Customer_Registered(self,CardId,0)
                        if(resultCustomer ==[] ):
                            resultGuest=CheckExist.check_CardId_Guest_Registered(self,CardId,0)
                            if(resultGuest!=[]):
                                self.clearGlobal("0In")
                            else:
                                guestLastId=insert_data_guest_regis(self,CardId,CarLicense)
                                if(guestLastId!= -1):
                                    CarLogLastId = insert_car_log(self,guestLastId,0,0)
                                    if(CarLogLastId != -1):
                                        result = CheckExist.Get_Date_Car_log_by_id(id)
                                        print('abc',result)
                                        if (result!=[]):
                                            Date = result[2]
                                            if (Date != ""):
                                                cv2.imwrite("./Carlog/"+Date+"-Back-In",cv_img)
                                            else:
                                                self.clearGlobal("0In")
                                        else:
                                            self.clearGlobal("0In")
                                else:
                                    self.clearGlobal("0In")
                        else:
                            lastCarLog= CheckExist.get_last_Car_log_by_regisId(resultCustomer[0],1)
                            if(lastCarLog==[]):
                                CarLogLastId =insert_car_log(self,resultCustomer[0],0,1)
                                if(CarLogLastId!=-1):
                                    result= CheckExist.Get_Date_Car_log_by_id(CarLogLastId)
                                    if (result!=[]):
                                        Date=result[2]
                                        if (Date != ""):
                                            cv2.imwrite("./Carlog/"+Date+"-Back-In",cv_img)
                                        else: 
                                            self.clearGlobal("0In")
                                    else: 
                                            self.clearGlobal("0In")
                                else: 
                                    self.clearGlobal("0In")
                            else:
                                self.clearGlobal("0In")
                    else:
                        self.clearGlobal("0In")
            if self.index==3:
                if (Way=="Out"):
                    # CarLicense=OpenCamera(cv_img)
                    if (Validation.ValidCarLicense(CarLicense)):
                        resultCustomer =CheckExist.check_CardId_Customer_Registered(self,CardId,0)
                        if(resultCustomer ==[] ):
                            resultGuest=CheckExist.check_CardId_Guest_Registered(self,CardId,0)
                            if(resultGuest==[]):
                                self.clearGlobal("0Out")
                            else:
                                if (Disable_Guest_regis(self,resultGuest[0])):
                                    CarLogLastId = insert_car_log(self,resultGuest[0],1,0)
                                    if(CarLogLastId!=-1):
                                        result = CheckExist.Get_Date_Car_log_by_id(self,id)
                                        if(result!=[]):
                                            Date =result[2]
                                            if (Date != ""):
                                                cv2.imwrite("./Carlog/"+Date+"-Back-Out",cv_img)
                                            else: 
                                                self.clearGlobal("0Out")
                                        else: 
                                                self.clearGlobal("0Out")        
                                else:
                                    self.clearGlobal("0Out")

                                        
                        else:
                            lastCarLog= CheckExist.get_last_Car_log_by_regisId(resultCustomer[0],1)
                            if(lastCarLog==[]):
                                CarLogLastId =insert_car_log(self,resultCustomer[0],1,1)
                                if(CarLogLastId!=-1):
                                    result= CheckExist.Get_Date_Car_log_by_id(CarLogLastId)
                                    if (result!=[]):
                                        Date = result[2]
                                        if (Date != ""):
                                            cv2.imwrite("./Carlog/"+Date+"-Back-Out",cv_img)
                                        else: 
                                            self.clearGlobal("0Out")
                                    else: 
                                        self.clearGlobal("0Out")
                                else: 
                                    self.clearGlobal("0Out")
                            else:
                                self.clearGlobal("0Out")
                    else:
                        self.clearGlobal("0Out")

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
        self.thread2=VideoThread(2)
        self.thread3=VideoThread(3)
        # connect its signal to the update_image slot
        self.thread0.change_pixmap_signal.connect(self.update_image_front_in)
        self.thread1.change_pixmap_signal.connect(self.update_image_front_out)
        self.thread2.change_pixmap_signal.connect(self.update_image_back_in)
        self.thread3.change_pixmap_signal.connect(self.update_image_back_out)
        self.threads.append(self.thread0)
        self.threads.append(self.thread1)
        self.threads.append(self.thread2)
        self.threads.append(self.thread3)
        # start the thread
        for slot in self.threads:
            slot.start()
        self.uic.btnTable.clicked.connect(self.showScreen)
        
        
    
        
    def closeEvent(self):
        self.thread0.stop()
        self.thread1.stop()
        
   
    def showScreen(self):


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

        self.uic1.btnGuestRegisDisable.clicked.connect(self.GuestDisableButtonclick)

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

    #Start of Guest tab Event
    
       

        
    def GuestDisableButtonclick(self):
        row = self.uic1.tblGuest.currentRow()
        id = self.uic1.tblGuest.item(row,0).text()
        if(Disable_Guest_regis(self, id)):
            load_data_guest_regis(self)
        else:
            print('fail')


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
        if (data[3]=='0'):
            self.uic1.btnGuestRegisDisable.setEnabled(False)
        else:
            self.uic1.btnGuestRegisDisable.setEnabled(True)



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
        row = self.uic1.tblCustomerRegis.currentRow()
        id = self.uic1.tblCustomerRegis.item(row,0).text()
        # print('true',)
        if(Disable_Customer_regis(self, id)):
            load_data_customer_regis(self)
        else:
            print('fail')
    
    # customer regis table click
    def onCellCustomerRegis(self):

        self.CustomerRegisteredCancelButtonClick()

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
        row = self.uic1.tblCustomer.currentRow()
        id = self.uic1.tblCustomer.item(row,0).text()
        # print('true',)
        if(Disable_Customer(self, id)):
            load_data_customers(self)
        else:
            print('fail')
        

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
        if (data[4]=='0'):
            self.uic1.btnCustomerDisable.setEnabled(False)
        else:
            self.uic1.btnCustomerDisable.setEnabled(True)


    #Hide OK and Cancel button  
    def HideOkAndCancelButton(self):
        self.uic1.btnCustomerRegisOK.setVisible(False)
        self.uic1.btnCustomerOK.setVisible(False)
        self.uic1.btnCustomerRegisCancel.setVisible(False)
        self.uic1.btnCustomerCancel.setVisible(False)

    
    #Image captured show
    @pyqtSlot(np.ndarray)
    def update_image_front_in(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamFrontIn.setPixmap(qt_img)
    def update_image_front_out(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamFrontOut.setPixmap(qt_img)
    def update_image_back_out(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamBackOut.setPixmap(qt_img)
    def update_image_back_in(self, cv_img):
        qt_img = self.convert_cv_qt(cv_img)
        self.uic.CamBackIn.setPixmap(qt_img)
    
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

