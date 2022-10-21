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
        self.wgTab.setGeometry(QtCore.QRect(10, 10, 911, 691))
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
        self.txtCardUser = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardUser.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardUser.setFont(font)
        self.txtCardUser.setReadOnly(True)
        self.txtCardUser.setObjectName("txtCardUser")
        self.lblCardCreator = QtWidgets.QLabel(self.wgCard)
        self.lblCardCreator.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblCardCreator.setObjectName("lblCardCreator")
        self.lblCardCarLicense = QtWidgets.QLabel(self.wgCard)
        self.lblCardCarLicense.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblCardCarLicense.setObjectName("lblCardCarLicense")
        self.lblCardUser = QtWidgets.QLabel(self.wgCard)
        self.lblCardUser.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblCardUser.setObjectName("lblCardUser")
        self.btnCardNew = QtWidgets.QPushButton(self.wgCard)
        self.btnCardNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnCardNew.setObjectName("btnCardNew")
        self.tblCard = QtWidgets.QTableWidget(self.wgCard)
        self.tblCard.setGeometry(QtCore.QRect(10, 320, 891, 341))
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
        self.txtCardCreator = QtWidgets.QLineEdit(self.wgCard)
        self.txtCardCreator.setEnabled(False)
        self.txtCardCreator.setGeometry(QtCore.QRect(160, 160, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardCreator.setFont(font)
        self.txtCardCreator.setReadOnly(True)
        self.txtCardCreator.setObjectName("txtCardCreator")
        self.wgTab.addTab(self.wgCard, "")
        self.wgPark = QtWidgets.QWidget()
        self.wgPark.setObjectName("wgPark")
        self.txtParkNoS = QtWidgets.QLineEdit(self.wgPark)
        self.txtParkNoS.setGeometry(QtCore.QRect(150, 70, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtParkNoS.setFont(font)
        self.txtParkNoS.setReadOnly(True)
        self.txtParkNoS.setObjectName("txtParkNoS")
        self.lblParkArea = QtWidgets.QLabel(self.wgPark)
        self.lblParkArea.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblParkArea.setObjectName("lblParkArea")
        self.lblParkAvailable = QtWidgets.QLabel(self.wgPark)
        self.lblParkAvailable.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblParkAvailable.setObjectName("lblParkAvailable")
        self.tblPark = QtWidgets.QTableWidget(self.wgPark)
        self.tblPark.setGeometry(QtCore.QRect(10, 320, 891, 341))
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
        self.txtParkCreator = QtWidgets.QLineEdit(self.wgPark)
        self.txtParkCreator.setEnabled(False)
        self.txtParkCreator.setGeometry(QtCore.QRect(150, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtParkCreator.setFont(font)
        self.txtParkCreator.setReadOnly(True)
        self.txtParkCreator.setObjectName("txtParkCreator")
        self.lblParkCreator = QtWidgets.QLabel(self.wgPark)
        self.lblParkCreator.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblParkCreator.setObjectName("lblParkCreator")
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
        self.txtCarLogCreator = QtWidgets.QLineEdit(self.wgCarLog)
        self.txtCarLogCreator.setGeometry(QtCore.QRect(220, 260, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCarLogCreator.setFont(font)
        self.txtCarLogCreator.setReadOnly(True)
        self.txtCarLogCreator.setObjectName("txtCarLogCreator")
        self.lblCarLogCreator = QtWidgets.QLabel(self.wgCarLog)
        self.lblCarLogCreator.setGeometry(QtCore.QRect(10, 260, 201, 41))
        self.lblCarLogCreator.setObjectName("lblCarLogCreator")
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
        self.wgTab.addTab(self.wgCarLog, "")
        self.wgUser = QtWidgets.QWidget()
        self.wgUser.setObjectName("wgUser")
        self.lblUserCreator = QtWidgets.QLabel(self.wgUser)
        self.lblUserCreator.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.lblUserCreator.setObjectName("lblUserCreator")
        self.lblUserFullName = QtWidgets.QLabel(self.wgUser)
        self.lblUserFullName.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblUserFullName.setObjectName("lblUserFullName")
        self.lblUserPersonalId = QtWidgets.QLabel(self.wgUser)
        self.lblUserPersonalId.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblUserPersonalId.setObjectName("lblUserPersonalId")
        self.tblUser = QtWidgets.QTableWidget(self.wgUser)
        self.tblUser.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblUser.setObjectName("tblUser")
        self.tblUser.setColumnCount(0)
        self.tblUser.setRowCount(0)
        self.btnUserDisable = QtWidgets.QPushButton(self.wgUser)
        self.btnUserDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnUserDisable.setObjectName("btnUserDisable")
        self.txtUserFullName = QtWidgets.QLineEdit(self.wgUser)
        self.txtUserFullName.setGeometry(QtCore.QRect(160, 10, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtUserFullName.setFont(font)
        self.txtUserFullName.setReadOnly(True)
        self.txtUserFullName.setObjectName("txtUserFullName")
        self.txtUserPersonalId = QtWidgets.QLineEdit(self.wgUser)
        self.txtUserPersonalId.setGeometry(QtCore.QRect(160, 60, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtUserPersonalId.setFont(font)
        self.txtUserPersonalId.setReadOnly(True)
        self.txtUserPersonalId.setObjectName("txtUserPersonalId")
        self.btnUserNew = QtWidgets.QPushButton(self.wgUser)
        self.btnUserNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnUserNew.setObjectName("btnUserNew")
        self.txtUserCreator = QtWidgets.QLineEdit(self.wgUser)
        self.txtUserCreator.setEnabled(False)
        self.txtUserCreator.setGeometry(QtCore.QRect(160, 210, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtUserCreator.setFont(font)
        self.txtUserCreator.setReadOnly(True)
        self.txtUserCreator.setObjectName("txtUserCreator")
        self.lblUserPhoneNumber = QtWidgets.QLabel(self.wgUser)
        self.lblUserPhoneNumber.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblUserPhoneNumber.setObjectName("lblUserPhoneNumber")
        self.lblUserEmail = QtWidgets.QLabel(self.wgUser)
        self.lblUserEmail.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblUserEmail.setObjectName("lblUserEmail")
        self.txtUserPhoneNumber = QtWidgets.QLineEdit(self.wgUser)
        self.txtUserPhoneNumber.setGeometry(QtCore.QRect(160, 110, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtUserPhoneNumber.setFont(font)
        self.txtUserPhoneNumber.setReadOnly(True)
        self.txtUserPhoneNumber.setObjectName("txtUserPhoneNumber")
        self.txtUserEmail = QtWidgets.QLineEdit(self.wgUser)
        self.txtUserEmail.setGeometry(QtCore.QRect(160, 160, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtUserEmail.setFont(font)
        self.txtUserEmail.setReadOnly(True)
        self.txtUserEmail.setObjectName("txtUserEmail")
        self.btnUserOK = QtWidgets.QPushButton(self.wgUser)
        self.btnUserOK.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnUserOK.setObjectName("btnUserOK")
        self.btnUserCancel = QtWidgets.QPushButton(self.wgUser)
        self.btnUserCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnUserCancel.setObjectName("btnUserCancel")
        self.wgTab.addTab(self.wgUser, "")
        self.wgCardType = QtWidgets.QWidget()
        self.wgCardType.setObjectName("wgCardType")
        self.tblCardType = QtWidgets.QTableWidget(self.wgCardType)
        self.tblCardType.setGeometry(QtCore.QRect(10, 340, 891, 341))
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
        self.lblCardTypeCreator = QtWidgets.QLabel(self.wgCardType)
        self.lblCardTypeCreator.setGeometry(QtCore.QRect(20, 140, 201, 41))
        self.lblCardTypeCreator.setObjectName("lblCardTypeCreator")
        self.txtCardTypeCreator = QtWidgets.QLineEdit(self.wgCardType)
        self.txtCardTypeCreator.setEnabled(False)
        self.txtCardTypeCreator.setGeometry(QtCore.QRect(170, 140, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtCardTypeCreator.setFont(font)
        self.txtCardTypeCreator.setReadOnly(True)
        self.txtCardTypeCreator.setObjectName("txtCardTypeCreator")
        self.wgTab.addTab(self.wgCardType, "")
        self.wgStaff = QtWidgets.QWidget()
        self.wgStaff.setObjectName("wgStaff")
        self.txtStaffUserName = QtWidgets.QLineEdit(self.wgStaff)
        self.txtStaffUserName.setGeometry(QtCore.QRect(160, 20, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtStaffUserName.setFont(font)
        self.txtStaffUserName.setReadOnly(True)
        self.txtStaffUserName.setObjectName("txtStaffUserName")
        self.lblStaffPassword = QtWidgets.QLabel(self.wgStaff)
        self.lblStaffPassword.setGeometry(QtCore.QRect(10, 60, 201, 41))
        self.lblStaffPassword.setObjectName("lblStaffPassword")
        self.lblStaffFullName = QtWidgets.QLabel(self.wgStaff)
        self.lblStaffFullName.setGeometry(QtCore.QRect(10, 110, 201, 41))
        self.lblStaffFullName.setObjectName("lblStaffFullName")
        self.tblStaff = QtWidgets.QTableWidget(self.wgStaff)
        self.tblStaff.setGeometry(QtCore.QRect(10, 320, 891, 341))
        self.tblStaff.setObjectName("tblStaff")
        self.tblStaff.setColumnCount(0)
        self.tblStaff.setRowCount(0)
        self.btnStaffDisable = QtWidgets.QPushButton(self.wgStaff)
        self.btnStaffDisable.setGeometry(QtCore.QRect(560, 60, 211, 41))
        self.btnStaffDisable.setObjectName("btnStaffDisable")
        self.txtStaffPassword = QtWidgets.QLineEdit(self.wgStaff)
        self.txtStaffPassword.setGeometry(QtCore.QRect(160, 70, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtStaffPassword.setFont(font)
        self.txtStaffPassword.setReadOnly(True)
        self.txtStaffPassword.setObjectName("txtStaffPassword")
        self.lblStaffUserName = QtWidgets.QLabel(self.wgStaff)
        self.lblStaffUserName.setGeometry(QtCore.QRect(10, 10, 201, 41))
        self.lblStaffUserName.setObjectName("lblStaffUserName")
        self.txtStaffFullName = QtWidgets.QLineEdit(self.wgStaff)
        self.txtStaffFullName.setGeometry(QtCore.QRect(160, 120, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtStaffFullName.setFont(font)
        self.txtStaffFullName.setReadOnly(True)
        self.txtStaffFullName.setObjectName("txtStaffFullName")
        self.btnStaffNew = QtWidgets.QPushButton(self.wgStaff)
        self.btnStaffNew.setGeometry(QtCore.QRect(560, 10, 211, 41))
        self.btnStaffNew.setObjectName("btnStaffNew")
        self.lblStaffPersonalId = QtWidgets.QLabel(self.wgStaff)
        self.lblStaffPersonalId.setGeometry(QtCore.QRect(10, 160, 201, 41))
        self.lblStaffPersonalId.setObjectName("lblStaffPersonalId")
        self.lblStaffAddress = QtWidgets.QLabel(self.wgStaff)
        self.lblStaffAddress.setGeometry(QtCore.QRect(10, 210, 201, 41))
        self.lblStaffAddress.setObjectName("lblStaffAddress")
        self.txtStaffPersonalId = QtWidgets.QLineEdit(self.wgStaff)
        self.txtStaffPersonalId.setGeometry(QtCore.QRect(160, 170, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtStaffPersonalId.setFont(font)
        self.txtStaffPersonalId.setReadOnly(True)
        self.txtStaffPersonalId.setObjectName("txtStaffPersonalId")
        self.txtStaffAddress = QtWidgets.QLineEdit(self.wgStaff)
        self.txtStaffAddress.setGeometry(QtCore.QRect(160, 220, 311, 41))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.txtStaffAddress.setFont(font)
        self.txtStaffAddress.setReadOnly(True)
        self.txtStaffAddress.setObjectName("txtStaffAddress")
        self.btnStaffOK = QtWidgets.QPushButton(self.wgStaff)
        self.btnStaffOK.setGeometry(QtCore.QRect(560, 117, 93, 41))
        self.btnStaffOK.setObjectName("btnStaffOK")
        self.btnStaffCancel = QtWidgets.QPushButton(self.wgStaff)
        self.btnStaffCancel.setGeometry(QtCore.QRect(680, 120, 93, 41))
        self.btnStaffCancel.setObjectName("btnStaffCancel")
        self.wgTab.addTab(self.wgStaff, "")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 932, 26))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow1)
        self.wgTab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow"))
        self.lblCardCreator.setText(_translate("MainWindow1", "Created by"))
        self.lblCardCarLicense.setText(_translate("MainWindow1", "Car License"))
        self.lblCardUser.setText(_translate("MainWindow1", "User"))
        self.btnCardNew.setText(_translate("MainWindow1", "New"))
        self.btnCardDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblCardId.setText(_translate("MainWindow1", "Card Id"))
        self.btnCardOk.setText(_translate("MainWindow1", "OK"))
        self.btnCardCancel.setText(_translate("MainWindow1", "Cancel"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCard), _translate("MainWindow1", "Card Registered"))
        self.lblParkArea.setText(_translate("MainWindow1", "Area"))
        self.lblParkAvailable.setText(_translate("MainWindow1", "Available"))
        self.btnParkDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblParkNoS.setText(_translate("MainWindow1", "Number Of Slot"))
        self.btnParkNew.setText(_translate("MainWindow1", "New"))
        self.btnParkOK.setText(_translate("MainWindow1", "OK"))
        self.btnParkCancel.setText(_translate("MainWindow1", "Cancel"))
        self.lblParkCreator.setText(_translate("MainWindow1", "Created by"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgPark), _translate("MainWindow1", "Parks"))
        self.lblCardLogCardId.setText(_translate("MainWindow1", "Card Id"))
        self.lblCarLogDate.setText(_translate("MainWindow1", "DateTime"))
        self.lblCarLogType.setText(_translate("MainWindow1", "In/Out"))
        self.lblCarLogCarNumber.setText(_translate("MainWindow1", "License Plates"))
        self.lblCarLogCreator.setText(_translate("MainWindow1", "Created by"))
        self.lblCarLogArea.setText(_translate("MainWindow1", "Area"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCarLog), _translate("MainWindow1", "Car Log"))
        self.lblUserCreator.setText(_translate("MainWindow1", "Created by"))
        self.lblUserFullName.setText(_translate("MainWindow1", "Full Name"))
        self.lblUserPersonalId.setText(_translate("MainWindow1", "Personal Id"))
        self.btnUserDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnUserNew.setText(_translate("MainWindow1", "New"))
        self.lblUserPhoneNumber.setText(_translate("MainWindow1", "Phone Number"))
        self.lblUserEmail.setText(_translate("MainWindow1", "Email"))
        self.btnUserOK.setText(_translate("MainWindow1", "OK"))
        self.btnUserCancel.setText(_translate("MainWindow1", "Cancel"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgUser), _translate("MainWindow1", "Users"))
        self.btnCardTypeOK.setText(_translate("MainWindow1", "OK"))
        self.btnCardTypeNew.setText(_translate("MainWindow1", "New"))
        self.btnCardTypeDisable.setText(_translate("MainWindow1", "Disable"))
        self.btnCardTypeCancel.setText(_translate("MainWindow1", "Cancel"))
        self.lblCardTypeCardId.setText(_translate("MainWindow1", "Card Id"))
        self.lblCardType.setText(_translate("MainWindow1", "Card Type"))
        self.lblCardTypeCreator.setText(_translate("MainWindow1", "Created by"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgCardType), _translate("MainWindow1", "Card Type"))
        self.lblStaffPassword.setText(_translate("MainWindow1", "Password"))
        self.lblStaffFullName.setText(_translate("MainWindow1", "Full Name"))
        self.btnStaffDisable.setText(_translate("MainWindow1", "Disable"))
        self.lblStaffUserName.setText(_translate("MainWindow1", "UserName"))
        self.btnStaffNew.setText(_translate("MainWindow1", "New"))
        self.lblStaffPersonalId.setText(_translate("MainWindow1", "Personal Id"))
        self.lblStaffAddress.setText(_translate("MainWindow1", "Address"))
        self.btnStaffOK.setText(_translate("MainWindow1", "OK"))
        self.btnStaffCancel.setText(_translate("MainWindow1", "Cancel"))
        self.wgTab.setTabText(self.wgTab.indexOf(self.wgStaff), _translate("MainWindow1", "Staffs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow1 = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(MainWindow1)
    MainWindow1.show()
    sys.exit(app.exec_())
