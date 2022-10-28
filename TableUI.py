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
        MainWindow1.resize(932, 755)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.wgTab = QtWidgets.QTabWidget(self.centralwidget)
        self.wgTab.setGeometry(QtCore.QRect(10, 10, 911, 701))
        self.wgTab.setObjectName("wgTab")
        self.wgCard = QtWidgets.QWidget()
        self.wgCard.setObjectName("wgCard")
        self.txtCardId = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardId.setEnabled(True)
        self.txtCardId.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardId.setFont(font)
        self.txtCardId.setReadOnly(True)
        self.txtCardId.setObjectName("txtCardId")
        self.txtCardCustomerId = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardCustomerId.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardCustomerId.setFont(font)
        self.txtCardCustomerId.setReadOnly(True)
        self.txtCardCustomerId.setObjectName("txtCardCustomerId")
        self.lblCardCarLicense = QtWidgets.QLabel(self.wgCard)
        self.lblCardCarLicense.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCardCarLicense.setObjectName("lblCardCarLicense")
        self.lblCardCustomerId = QtWidgets.QLabel(self.wgCard)
        self.lblCardCustomerId.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCardCustomerId.setObjectName("lblCardCustomerId")
        self.btnCardNew = QtWidgets.QPushButton(self.wgCard)
        self.btnCardNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnCardNew.setObjectName("btnCardNew")
        self.tblCard = QtWidgets.QTableWidget(self.wgCard)
        self.tblCard.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblCard.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCard.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCard.setObjectName("tblCard")
        self.tblCard.setColumnCount(0)
        self.tblCard.setRowCount(0)
        self.btnCardDisable = QtWidgets.QPushButton(self.wgCard)
        self.btnCardDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnCardDisable.setObjectName("btnCardDisable")
        self.lblCardId = QtWidgets.QLabel(self.wgCard)
        self.lblCardId.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCardId.setObjectName("lblCardId")
        self.txtCardCarNumber = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardCarNumber.setGeometry(QtCore.QRect(160, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardCarNumber.setFont(font)
        self.txtCardCarNumber.setReadOnly(True)
        self.txtCardCarNumber.setObjectName("txtCardCarNumber")
        self.btnCardOk = QtWidgets.QPushButton(self.wgCard)
        self.btnCardOk.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnCardOk.setObjectName("btnCardOk")
        self.btnCardCancel = QtWidgets.QPushButton(self.wgCard)
        self.btnCardCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnCardCancel.setObjectName("btnCardCancel")
        self.btnLoadDataCard = QtWidgets.QPushButton(self.wgCard)
        self.btnLoadDataCard.setGeometry(QtCore.QRect(620, 170, 93, 41))
        self.btnLoadDataCard.setObjectName("btnLoadDataCard")
        self.wgTab.addTab(self.wgCard, "")
        self.wgPark = QtWidgets.QWidget()
        self.wgPark.setObjectName("wgPark")
        self.txtParkNo = QtWidgets.QLineEdit(self.wgPark)
        self.txtParkNo.setGeometry(QtCore.QRect(150, 70, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtParkNo.setFont(font)
        self.txtParkNo.setReadOnly(True)
        self.txtParkNo.setObjectName("txtParkNo")
        self.lblParkArea = QtWidgets.QLabel(self.wgPark)
        self.lblParkArea.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblParkArea.setObjectName("lblParkArea")
        self.lblParkAvailable = QtWidgets.QLabel(self.wgPark)
        self.lblParkAvailable.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblParkAvailable.setObjectName("lblParkAvailable")
        self.tblPark = QtWidgets.QTableWidget(self.wgPark)
        self.tblPark.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblPark.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblPark.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblPark.setObjectName("tblPark")
        self.tblPark.setColumnCount(0)
        self.tblPark.setRowCount(0)
        self.btnParkDisable = QtWidgets.QPushButton(self.wgPark)
        self.btnParkDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnParkDisable.setObjectName("btnParkDisable")
        self.txtParkAvailable = QtWidgets.QLineEdit(self.wgPark)
        self.txtParkAvailable.setGeometry(QtCore.QRect(150, 120, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtParkAvailable.setFont(font)
        self.txtParkAvailable.setReadOnly(True)
        self.txtParkAvailable.setObjectName("txtParkAvailable")
        self.lblParkNoS = QtWidgets.QLabel(self.wgPark)
        self.lblParkNoS.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblParkNoS.setObjectName("lblParkNoS")
        self.btnParkNew = QtWidgets.QPushButton(self.wgPark)
        self.btnParkNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnParkNew.setObjectName("btnParkNew")
        self.txtParkArea = QtWidgets.QLineEdit(self.wgPark)
        self.txtParkArea.setGeometry(QtCore.QRect(150, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtParkArea.setFont(font)
        self.txtParkArea.setReadOnly(True)
        self.txtParkArea.setObjectName("txtParkArea")
        self.btnParkOK = QtWidgets.QPushButton(self.wgPark)
        self.btnParkOK.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnParkOK.setObjectName("btnParkOK")
        self.btnParkCancel = QtWidgets.QPushButton(self.wgPark)
        self.btnParkCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnParkCancel.setObjectName("btnParkCancel")
        self.btnLoadDataPark = QtWidgets.QPushButton(self.wgPark)
        self.btnLoadDataPark.setGeometry(QtCore.QRect(620, 170, 93, 41))
        self.btnLoadDataPark.setObjectName("btnLoadDataPark")
        self.wgTab.addTab(self.wgPark, "")
        self.wgCarLog = QtWidgets.QWidget()
        self.wgCarLog.setObjectName("wgCarLog")
        self.txtCarLogCarNumber = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLogCarNumber.setGeometry(QtCore.QRect(220, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLogCarNumber.setFont(font)
        self.txtCarLogCarNumber.setReadOnly(True)
        self.txtCarLogCarNumber.setObjectName("txtCarLogCarNumber")
        self.lblCardLogCardId = QtWidgets.QLabel(self.wgCarLog)
        self.lblCardLogCardId.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCardLogCardId.setObjectName("lblCardLogCardId")
        self.lblCarLogDate = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogDate.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCarLogDate.setObjectName("lblCarLogDate")
        self.lblCarLogType = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogType.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblCarLogType.setObjectName("lblCarLogType")
        self.tblCarLog = QtWidgets.QTableWidget(self.wgCarLog)
        self.tblCarLog.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblCarLog.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCarLog.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCarLog.setObjectName("tblCarLog")
        self.tblCarLog.setColumnCount(0)
        self.tblCarLog.setRowCount(0)
        self.txtCarLogDate = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLogDate.setGeometry(QtCore.QRect(220, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLogDate.setFont(font)
        self.txtCarLogDate.setReadOnly(True)
        self.txtCarLogDate.setObjectName("txtCarLogDate")
        self.lblCarLogCarNumber = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogCarNumber.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCarLogCarNumber.setObjectName("lblCarLogCarNumber")
        self.txtCarLogType = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLogType.setGeometry(QtCore.QRect(220, 160, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLogType.setFont(font)
        self.txtCarLogType.setReadOnly(True)
        self.txtCarLogType.setObjectName("txtCarLogType")
        self.txtCarLogCardId = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLogCardId.setGeometry(QtCore.QRect(220, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLogCardId.setFont(font)
        self.txtCarLogCardId.setReadOnly(True)
        self.txtCarLogCardId.setObjectName("txtCarLogCardId")
        self.txtCarLoArea = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLoArea.setGeometry(QtCore.QRect(220, 210, 121, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLoArea.setFont(font)
        self.txtCarLoArea.setText("")
        self.txtCarLoArea.setReadOnly(True)
        self.txtCarLoArea.setObjectName("txtCarLoArea")
        self.lblCarLogArea = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogArea.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.lblCarLogArea.setObjectName("lblCarLogArea")
        self.btnLoadDataCar = QtWidgets.QPushButton(self.wgCarLog)
        self.btnLoadDataCar.setGeometry(QtCore.QRect(680, 10, 93, 41))
        self.btnLoadDataCar.setObjectName("btnLoadDataCar")
        self.wgTab.addTab(self.wgCarLog, "")
        self.wgCustomer = QtWidgets.QWidget()
        self.wgCustomer.setObjectName("wgCustomer")
        self.lblCustomerFullName = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerFullName.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblCustomerFullName.setObjectName("lblCustomerFullName")
        self.lblCustomerPersonalId = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerPersonalId.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCustomerPersonalId.setObjectName("lblCustomerPersonalId")
        self.tblCustomer = QtWidgets.QTableWidget(self.wgCustomer)
        self.tblCustomer.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblCustomer.setObjectName("tblCustomer")
        self.tblCustomer.setColumnCount(0)
        self.tblCustomer.setRowCount(0)
        self.btnCustomerDisable = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnCustomerDisable.setObjectName("btnCustomerDisable")
        self.txtCustomerFullName = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCustomerFullName.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCustomerFullName.setFont(font)
        self.txtCustomerFullName.setReadOnly(True)
        self.txtCustomerFullName.setObjectName("txtCustomerFullName")
        self.txtCustomerPersonalId = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCustomerPersonalId.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCustomerPersonalId.setFont(font)
        self.txtCustomerPersonalId.setReadOnly(True)
        self.txtCustomerPersonalId.setObjectName("txtCustomerPersonalId")
        self.btnCustomerNew = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnCustomerNew.setObjectName("btnCustomerNew")
        self.btnCustomerOK = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerOK.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnCustomerOK.setObjectName("btnCustomerOK")
        self.btnCustomerCancel = QtWidgets.QPushButton(self.wgCustomer)
        self.btnCustomerCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnCustomerCancel.setObjectName("btnCustomerCancel")
        self.btnLoadDataCustomer = QtWidgets.QPushButton(self.wgCustomer)
        self.btnLoadDataCustomer.setGeometry(QtCore.QRect(620, 170, 93, 41))
        self.btnLoadDataCustomer.setObjectName("btnLoadDataCustomer")
        self.txtCustomerRoom = QtWidgets.QLineEdit(self.wgCustomer)
        self.txtCustomerRoom.setGeometry(QtCore.QRect(160, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCustomerRoom.setFont(font)
        self.txtCustomerRoom.setText("")
        self.txtCustomerRoom.setReadOnly(True)
        self.txtCustomerRoom.setObjectName("txtCustomerRoom")
        self.lblCustomerRoom = QtWidgets.QLabel(self.wgCustomer)
        self.lblCustomerRoom.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCustomerRoom.setObjectName("lblCustomerRoom")
        self.wgTab.addTab(self.wgCustomer, "")
        self.wgCardType = QtWidgets.QWidget()
        self.wgCardType.setObjectName("wgCardType")
        self.tblCardType = QtWidgets.QTableWidget(self.wgCardType)
        self.tblCardType.setGeometry(QtCore.QRect(10, 340, 891, 341))
        self.tblCardType.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tblCardType.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tblCardType.setObjectName("tblCardType")
        self.tblCardType.setColumnCount(0)
        self.tblCardType.setRowCount(0)
        self.btnCardTypeOK = QtWidgets.QPushButton(self.wgCardType)
        self.btnCardTypeOK.setGeometry(QtCore.QRect(560, 137, 93, 41))
        self.btnCardTypeOK.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.btnCardTypeOK.setObjectName("btnCardTypeOK")
        self.btnCardTypeNew = QtWidgets.QPushButton(self.wgCardType)
        self.btnCardTypeNew.setGeometry(QtCore.QRect(560, 30, 211, 41))
        self.btnCardTypeNew.setObjectName("btnCardTypeNew")
        self.btnCardTypeDisable = QtWidgets.QPushButton(self.wgCardType)
        self.btnCardTypeDisable.setGeometry(QtCore.QRect(560, 80, 211, 41))
        self.btnCardTypeDisable.setObjectName("btnCardTypeDisable")
        self.btnCardTypeCancel = QtWidgets.QPushButton(self.wgCardType)
        self.btnCardTypeCancel.setGeometry(QtCore.QRect(680, 140, 93, 41))
        self.btnCardTypeCancel.setObjectName("btnCardTypeCancel")
        self.txtCardTypeCardId = QtWidgets.QLineEdit(self.wgCardType)
        self.txtCardTypeCardId.setEnabled(True)
        self.txtCardTypeCardId.setGeometry(QtCore.QRect(170, 40, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardTypeCardId.setFont(font)
        self.txtCardTypeCardId.setReadOnly(True)
        self.txtCardTypeCardId.setObjectName("txtCardTypeCardId")
        self.lblCardTypeCardId = QtWidgets.QLabel(self.wgCardType)
        self.lblCardTypeCardId.setGeometry(QtCore.QRect(20, 40, 201, 41))
        self.lblCardTypeCardId.setObjectName("lblCardTypeCardId")
        self.lblCardType = QtWidgets.QLabel(self.wgCardType)
        self.lblCardType.setGeometry(QtCore.QRect(20, 90, 201, 41))
        self.lblCardType.setObjectName("lblCardType")
        self.cbCardType = QtWidgets.QComboBox(self.wgCardType)
        self.cbCardType.setGeometry(QtCore.QRect(170, 90, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.cbCardType.setFont(font)
        self.cbCardType.setEditable(False)
        self.cbCardType.setObjectName("cbCardType")
        self.btnLoadDataCardType = QtWidgets.QPushButton(self.wgCardType)
        self.btnLoadDataCardType.setGeometry(QtCore.QRect(620, 190, 93, 41))
        self.btnLoadDataCardType.setObjectName("btnLoadDataCardType")
        self.wgTab.addTab(self.wgCardType, "")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow1)
        self.wgTab.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "Database Manager"))
        self.lblCardCarLicense.setText(_translate("MainWindow1", "Car License"))
        self.lblCardCustomerId.setText(_translate("MainWindow1", "Customer Id"))
        self.btnCardNew.setText(_translate("MainWindow1", "New"))
        self.btnCardDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblCardId.setText(_translate("MainWindow1", "Card Id"))
        self.btnCardOk.setText(_translate("MainWindow1", "OK"))
        self.btnCardCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataCard.setText(_translate("MainWindow1", "Load Data"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCard), _translate("MainWindow1", "Card Registered"))
        self.lblParkArea.setText(_translate("MainWindow1", "Area"))
        self.lblParkAvailable.setText(_translate("MainWindow1", "Available"))
        self.btnParkDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblParkNoS.setText(_translate("MainWindow1", "Number Of Slot"))
        self.btnParkNew.setText(_translate("MainWindow1", "New"))
        self.btnParkOK.setText(_translate("MainWindow1", "OK"))
        self.btnParkCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataPark.setText(_translate("MainWindow1", "Load Data"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgPark), _translate("MainWindow1", "Parks"))
        self.lblCardLogCardId.setText(_translate("MainWindow1", "Card Id"))
        self.lblCarLogDate.setText(_translate("MainWindow1", "DateTime"))
        self.lblCarLogType.setText(_translate("MainWindow1", "In/Out"))
        self.lblCarLogCarNumber.setText(_translate("MainWindow1", "License Plates"))
        self.lblCarLogArea.setText(_translate("MainWindow1", "Area"))
        self.btnLoadDataCar.setText(_translate("MainWindow1", "Load Data"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCarLog), _translate("MainWindow1", "Car Log"))
        self.lblCustomerFullName.setText(_translate("MainWindow1", "Full Name"))
        self.lblCustomerPersonalId.setText(_translate("MainWindow1", "Personal Id"))
        self.btnCustomerDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnCustomerNew.setText(_translate("MainWindow1", "New"))
        self.btnCustomerOK.setText(_translate("MainWindow1", "OK"))
        self.btnCustomerCancel.setText(_translate("MainWindow1", "Cancel"))
        self.btnLoadDataCustomer.setText(_translate("MainWindow1", "Load Data"))
        self.lblCustomerRoom.setText(_translate("MainWindow1", "Room"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCustomer), _translate("MainWindow1", "Users"))
        self.btnCardTypeOK.setText(_translate("MainWindow1", "OK"))
        self.btnCardTypeNew.setText(_translate("MainWindow1", "New"))
        self.btnCardTypeDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnCardTypeCancel.setText(_translate("MainWindow1", "Cancel"))
        self.lblCardTypeCardId.setText(_translate("MainWindow1", "Card Id"))
        self.lblCardType.setText(_translate("MainWindow1", "Card Type"))
        self.btnLoadDataCardType.setText(_translate("MainWindow1", "Load Data"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCardType), _translate("MainWindow1", "Card Type"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
