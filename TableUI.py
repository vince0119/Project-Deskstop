# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Table.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow1(object):
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(935, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.wgTab = QtWidgets.QTabWidget(self.centralwidget)
        self.wgTab.setGeometry(QtCore.QRect(10, 10, 911, 701))
        self.wgTab.setObjectName("wgTab")
        self.wgCarLog = QtWidgets.QWidget()
        self.wgCarLog.setObjectName("wgCarLog")
        self.txtRegisteredId = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtRegisteredId.setGeometry(QtCore.QRect(220, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtRegisteredId.setFont(font)
        self.txtRegisteredId.setReadOnly(True)
        self.txtRegisteredId.setObjectName("txtRegisteredId")
        self.lblCarLogType = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogType.setGeometry(QtCore.QRect(10, 120, 201, 41))
        self.lblCarLogType.setObjectName("lblCarLogType")
        self.tblCarLog = QtWidgets.QTableWidget(self.wgCarLog)
        self.tblCarLog.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblCarLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCarLog.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCarLog.setObjectName("tblCarLog")
        self.tblCarLog.setColumnCount(4)
        self.tblCarLog.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCarLog.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCarLog.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCarLog.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCarLog.setHorizontalHeaderItem(3, item)
        self.tblCarLog.horizontalHeader().setDefaultSectionSize(150)
        self.lblCarLogCarNumber = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogCarNumber.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCarLogCarNumber.setObjectName("lblCarLogCarNumber")
        self.btnLoadDataCar = QtWidgets.QPushButton(self.wgCarLog)
        self.btnLoadDataCar.setGeometry(QtCore.QRect(680, 10, 93, 41))
        self.btnLoadDataCar.setObjectName("btnLoadDataCar")
        self.cbCarLogStatus = QtWidgets.QComboBox(self.wgCarLog)
        self.cbCarLogStatus.setEnabled(False)
        self.cbCarLogStatus.setGeometry(QtCore.QRect(220, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.cbCarLogStatus.setFont(font)
        self.cbCarLogStatus.setEditable(True)
        self.cbCarLogStatus.setObjectName("cbCarLogStatus")
        self.cbCarLogStatus.addItem("")
        self.cbCarLogStatus.addItem("")
        self.lblCarLogCarNumber_2 = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogCarNumber_2.setGeometry(QtCore.QRect(10, 180, 201, 41))
        self.lblCarLogCarNumber_2.setObjectName("lblCarLogCarNumber_2")
        self.txtCarLicense = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLicense.setGeometry(QtCore.QRect(220, 180, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLicense.setFont(font)
        self.txtCarLicense.setReadOnly(True)
        self.txtCarLicense.setObjectName("txtCarLicense")
        self.wgTab.addTab(self.wgCarLog, "")
        self.wgCard = QtWidgets.QWidget()
        self.wgCard.setObjectName("wgCard")
        self.txtCardIdGuest = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardIdGuest.setEnabled(True)
        self.txtCardIdGuest.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardIdGuest.setFont(font)
        self.txtCardIdGuest.setReadOnly(True)
        self.txtCardIdGuest.setObjectName("txtCardIdGuest")
        self.txtCarLicenseGuest = QtWidgets.QLineEdit(self.wgCard)
        self.txtCarLicenseGuest.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLicenseGuest.setFont(font)
        self.txtCarLicenseGuest.setReadOnly(True)
        self.txtCarLicenseGuest.setObjectName("txtCarLicenseGuest")
        self.lblCardCustomerId = QtWidgets.QLabel(self.wgCard)
        self.lblCardCustomerId.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCardCustomerId.setObjectName("lblCardCustomerId")
        self.btnGuestNew = QtWidgets.QPushButton(self.wgCard)
        self.btnGuestNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnGuestNew.setObjectName("btnGuestNew")
        self.tblGuest = QtWidgets.QTableWidget(self.wgCard)
        self.tblGuest.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblGuest.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblGuest.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblGuest.setObjectName("tblGuest")
        self.tblGuest.setColumnCount(5)
        self.tblGuest.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblGuest.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGuest.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGuest.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGuest.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblGuest.setHorizontalHeaderItem(4, item)
        self.tblGuest.horizontalHeader().setDefaultSectionSize(150)
        self.btnGuestDisable = QtWidgets.QPushButton(self.wgCard)
        self.btnGuestDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnGuestDisable.setObjectName("btnGuestDisable")
        self.lblCardId = QtWidgets.QLabel(self.wgCard)
        self.lblCardId.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCardId.setObjectName("lblCardId")
        self.btnGuestOk = QtWidgets.QPushButton(self.wgCard)
        self.btnGuestOk.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnGuestOk.setObjectName("btnGuestOk")
        self.btnGuestCancel = QtWidgets.QPushButton(self.wgCard)
        self.btnGuestCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnGuestCancel.setObjectName("btnGuestCancel")
        self.btnLoadDataGuest = QtWidgets.QPushButton(self.wgCard)
        self.btnLoadDataGuest.setGeometry(QtCore.QRect(620, 170, 93, 41))
        self.btnLoadDataGuest.setObjectName("btnLoadDataGuest")
        self.wgTab.addTab(self.wgCard, "")
        self.wgCustomer = QtWidgets.QWidget()
        self.wgCustomer.setObjectName("wgCustomer")
        self.lblCustomerFullName = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerFullName.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCustomerFullName.setObjectName("lblCustomerFullName")
        self.lblCustomerPersonalId = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerPersonalId.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCustomerPersonalId.setObjectName("lblCustomerPersonalId")
        self.tblCustomerRegis = QtWidgets.QTableWidget(self.wgCustomer)
        self.tblCustomerRegis.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblCustomerRegis.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCustomerRegis.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCustomerRegis.setObjectName("tblCustomerRegis")
        self.tblCustomerRegis.setColumnCount(8)
        self.tblCustomerRegis.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomerRegis.setHorizontalHeaderItem(7, item)
        self.tblCustomerRegis.horizontalHeader().setDefaultSectionSize(120)
        self.btnCustomerRegisDisable = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerRegisDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnCustomerRegisDisable.setObjectName("btnCustomerRegisDisable")
        self.txtCardIDCustomer = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCardIDCustomer.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardIDCustomer.setFont(font)
        self.txtCardIDCustomer.setReadOnly(True)
        self.txtCardIDCustomer.setObjectName("txtCardIDCustomer")
        self.txtCustomerId = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCustomerId.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCustomerId.setFont(font)
        self.txtCustomerId.setReadOnly(True)
        self.txtCustomerId.setObjectName("txtCustomerId")
        self.btnCustomerRegisNew = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerRegisNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnCustomerRegisNew.setObjectName("btnCustomerRegisNew")
        self.btnCustomerRegisOK = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerRegisOK.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnCustomerRegisOK.setObjectName("btnCustomerRegisOK")
        self.btnCustomerRegisCancel = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerRegisCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnCustomerRegisCancel.setObjectName("btnCustomerRegisCancel")
        self.btnLoadDataCustomerRegis = QtWidgets.QPushButton(self.wgCustomer)
        self.btnLoadDataCustomerRegis.setGeometry(QtCore.QRect(620, 170, 93, 41))
        self.btnLoadDataCustomerRegis.setObjectName("btnLoadDataCustomerRegis")
        self.txtCarLicenseCustomer = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCarLicenseCustomer.setGeometry(QtCore.QRect(160, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLicenseCustomer.setFont(font)
        self.txtCarLicenseCustomer.setText("")
        self.txtCarLicenseCustomer.setReadOnly(True)
        self.txtCarLicenseCustomer.setObjectName("txtCarLicenseCustomer")
        self.lblCustomerPersonalId_2 = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerPersonalId_2.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCustomerPersonalId_2.setObjectName("lblCustomerPersonalId_2")
        self.txtCarColor = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCarColor.setGeometry(QtCore.QRect(160, 160, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarColor.setFont(font)
        self.txtCarColor.setText("")
        self.txtCarColor.setReadOnly(True)
        self.txtCarColor.setObjectName("txtCarColor")
        self.lblCustomerPersonalId_3 = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerPersonalId_3.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblCustomerPersonalId_3.setObjectName("lblCustomerPersonalId_3")
        self.txtCarModel = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCarModel.setGeometry(QtCore.QRect(160, 210, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarModel.setFont(font)
        self.txtCarModel.setText("")
        self.txtCarModel.setReadOnly(True)
        self.txtCarModel.setObjectName("txtCarModel")
        self.lblCustomerPersonalId_4 = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerPersonalId_4.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.lblCustomerPersonalId_4.setObjectName("lblCustomerPersonalId_4")
        self.txtSearchCustomer = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtSearchCustomer.setGeometry(QtCore.QRect(480, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtSearchCustomer.setFont(font)
        self.txtSearchCustomer.setReadOnly(True)
        self.txtSearchCustomer.setObjectName("txtSearchCustomer")
        self.txtSearchCardID = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtSearchCardID.setGeometry(QtCore.QRect(700, 270, 181, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtSearchCardID.setFont(font)
        self.txtSearchCardID.setReadOnly(True)
        self.txtSearchCardID.setObjectName("txtSearchCardID")
        self.wgTab.addTab(self.wgCustomer, "")
        self.wgCardType = QtWidgets.QWidget()
        self.wgCardType.setObjectName("wgCardType")
        self.tblCustomer = QtWidgets.QTableWidget(self.wgCardType)
        self.tblCustomer.setGeometry(QtCore.QRect(10, 340, 891, 341))
        self.tblCustomer.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCustomer.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCustomer.setObjectName("tblCustomer")
        self.tblCustomer.setColumnCount(5)
        self.tblCustomer.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomer.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomer.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomer.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomer.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tblCustomer.setHorizontalHeaderItem(4, item)
        self.btnCustomerOK = QtWidgets.QPushButton(self.wgCardType)
        self.btnCustomerOK.setGeometry(QtCore.QRect(560, 137, 93, 41))
        self.btnCustomerOK.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnCustomerOK.setObjectName("btnCustomerOK")
        self.btnCustomerNew = QtWidgets.QPushButton(self.wgCardType)
        self.btnCustomerNew.setGeometry(QtCore.QRect(560, 30, 211, 41))
        self.btnCustomerNew.setObjectName("btnCustomerNew")
        self.btnCustomerDisable = QtWidgets.QPushButton(self.wgCardType)
        self.btnCustomerDisable.setGeometry(QtCore.QRect(560, 80, 211, 41))
        self.btnCustomerDisable.setObjectName("btnCustomerDisable")
        self.btnCustomerCancel = QtWidgets.QPushButton(self.wgCardType)
        self.btnCustomerCancel.setGeometry(QtCore.QRect(680, 140, 93, 41))
        self.btnCustomerCancel.setObjectName("btnCustomerCancel")
        self.btnLoadDataCustomer = QtWidgets.QPushButton(self.wgCardType)
        self.btnLoadDataCustomer.setGeometry(QtCore.QRect(620, 190, 93, 41))
        self.btnLoadDataCustomer.setObjectName("btnLoadDataCustomer")
        self.txtFullName = QtWidgets.QLineEdit(self.wgCardType)
        self.txtFullName.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtFullName.setFont(font)
        self.txtFullName.setReadOnly(True)
        self.txtFullName.setObjectName("txtFullName")
        self.lblCustomerFullName_3 = QtWidgets.QLabel(self.wgCardType)
        self.lblCustomerFullName_3.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCustomerFullName_3.setObjectName("lblCustomerFullName_3")
        self.txtPersonalID = QtWidgets.QLineEdit(self.wgCardType)
        self.txtPersonalID.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtPersonalID.setFont(font)
        self.txtPersonalID.setReadOnly(True)
        self.txtPersonalID.setObjectName("txtPersonalID")
        self.lblCustomerFullName_4 = QtWidgets.QLabel(self.wgCardType)
        self.lblCustomerFullName_4.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCustomerFullName_4.setObjectName("lblCustomerFullName_4")
        self.txtRoom = QtWidgets.QLineEdit(self.wgCardType)
        self.txtRoom.setGeometry(QtCore.QRect(160, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtRoom.setFont(font)
        self.txtRoom.setReadOnly(True)
        self.txtRoom.setObjectName("txtRoom")
        self.lblCustomerFullName_5 = QtWidgets.QLabel(self.wgCardType)
        self.lblCustomerFullName_5.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCustomerFullName_5.setObjectName("lblCustomerFullName_5")
        self.wgTab.addTab(self.wgCardType, "")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 935, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow1)
        self.wgTab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Database Manager"))
        self.lblCarLogType.setText(_translate("MainWindow1", "Status"))
        self.tblCarLog.setSortingEnabled(True)
        item = self.tblCarLog.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow1", "ID"))
        item = self.tblCarLog.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow1", "Registered ID"))
        item = self.tblCarLog.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow1", "Date"))
        item = self.tblCarLog.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow1", "Status"))
        self.lblCarLogCarNumber.setText(_translate("MainWindow1", "Registered ID"))
        self.btnLoadDataCar.setText(_translate("MainWindow1", "Load Data"))
        self.cbCarLogStatus.setItemText(0, _translate("MainWindow1", "IN"))
        self.cbCarLogStatus.setItemText(1, _translate("MainWindow1", "OUT"))
        self.lblCarLogCarNumber_2.setText(_translate("MainWindow1", "Car License"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCarLog), _translate("MainWindow1", "Car Log"))
        self.lblCardCustomerId.setText(_translate("MainWindow1", "Car License"))
        self.btnGuestNew.setText(_translate("MainWindow1", "New"))
        self.tblGuest.setSortingEnabled(True)
        item = self.tblGuest.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow1", "ID"))
        item = self.tblGuest.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow1", "Card ID"))
        item = self.tblGuest.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow1", "Car License"))
        item = self.tblGuest.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow1", "Active"))
        item = self.tblGuest.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow1", "Create Date"))
        self.btnGuestDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblCardId.setText(_translate("MainWindow1", "Card Id"))
        self.btnGuestOk.setText(_translate("MainWindow1", "OK"))
        self.btnGuestCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataGuest.setText(_translate("MainWindow1", "Load Data"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCard), _translate("MainWindow1", "Guest Registered"))
        self.lblCustomerFullName.setText(_translate("MainWindow1", "Card ID"))
        self.lblCustomerPersonalId.setText(_translate("MainWindow1", "Customer ID"))
        item = self.tblCustomerRegis.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow1", "Id"))
        item = self.tblCustomerRegis.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow1", "Card ID"))
        item = self.tblCustomerRegis.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow1", "Customer ID"))
        item = self.tblCustomerRegis.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow1", "Car License"))
        item = self.tblCustomerRegis.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow1", "Car Color"))
        item = self.tblCustomerRegis.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow1", "Car Model"))
        item = self.tblCustomerRegis.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow1", "Active"))
        item = self.tblCustomerRegis.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow1", "Created Date"))
        self.btnCustomerRegisDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnCustomerRegisNew.setText(_translate("MainWindow1", "New"))
        self.btnCustomerRegisOK.setText(_translate("MainWindow1", "OK"))
        self.btnCustomerRegisCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataCustomerRegis.setText(_translate("MainWindow1", "Load Data"))
        self.lblCustomerPersonalId_2.setText(_translate("MainWindow1", "Car License"))
        self.lblCustomerPersonalId_3.setText(_translate("MainWindow1", "Car Color"))
        self.lblCustomerPersonalId_4.setText(_translate("MainWindow1", "Car Model"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCustomer), _translate("MainWindow1", "Customer Registered"))
        item = self.tblCustomer.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow1", "ID"))
        item = self.tblCustomer.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow1", "FullName"))
        item = self.tblCustomer.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow1", "Personal ID"))
        item = self.tblCustomer.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow1", "Room"))
        item = self.tblCustomer.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow1", "Active"))
        self.btnCustomerOK.setText(_translate("MainWindow1", "OK"))
        self.btnCustomerNew.setText(_translate("MainWindow1", "New"))
        self.btnCustomerDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnCustomerCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataCustomer.setText(_translate("MainWindow1", "Load Data"))
        self.lblCustomerFullName_3.setText(_translate("MainWindow1", "Full Name"))
        self.lblCustomerFullName_4.setText(_translate("MainWindow1", "Personal ID"))
        self.lblCustomerFullName_5.setText(_translate("MainWindow1", "Room"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCardType), _translate("MainWindow1", "Customers"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
