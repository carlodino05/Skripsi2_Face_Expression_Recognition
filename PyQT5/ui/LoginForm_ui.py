# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\Documents\Alox\Computer Vision\Skripsi2\PyQT5\ui\LoginForm.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(690, 460)
        main.setMinimumSize(QtCore.QSize(690, 460))
        main.setMaximumSize(QtCore.QSize(690, 460))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setWindowOpacity(1.0)
        main.setStyleSheet("")
        self.bgWelcome = QtWidgets.QWidget(main)
        self.bgWelcome.setStyleSheet("QWidget#bgWelcome{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 0, 255, 0.8), stop:1 rgba(255, 255, 255, 255));\n"
" \n"
"}")
        self.bgWelcome.setObjectName("bgWelcome")
        self.loginFrame = QtWidgets.QFrame(self.bgWelcome)
        self.loginFrame.setGeometry(QtCore.QRect(280, 40, 381, 381))
        self.loginFrame.setStyleSheet("QWidget#loginFrame{\n"
"  background: rgba(222, 222, 222, 0.7);\n"
"  border-top-right-radius: 7px;\n"
"  border-bottom-right-radius: 7px;\n"
"  border-top:2px solid rgba(0, 0, 0, 0);\n"
"  border-top-color:rgba(46, 82, 101, 255);\n"
"  border-bottom:2px solid rgba(0, 0, 0, 0);\n"
"  border-bottom-color:rgba(46, 82, 101, 255);\n"
"  border-right:2px solid rgba(0, 0, 0, 0);\n"
"  border-right-color:rgba(46, 82, 101, 255);\n"
"}\n"
"\n"
"QWidget#loginFrame:hover {\n"
"  background: rgba(255, 255, 255, 0.7);\n"
"  border-top:2px solid rgba(0, 0, 0, 0);\n"
"  border-top-color:rgba(99, 0, 0, 255);\n"
"  border-bottom:2px solid rgba(0, 0, 0, 0);\n"
"  border-bottom-color:rgba(99, 0, 0, 255);\n"
"  border-right:2px solid rgba(0, 0, 0, 0);\n"
"  border-right-color:rgba(99, 0, 0, 255);\n"
"}\n"
"")
        self.loginFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.loginFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.loginFrame.setLineWidth(5)
        self.loginFrame.setMidLineWidth(2)
        self.loginFrame.setObjectName("loginFrame")
        self.btnUserLogin = QtWidgets.QPushButton(self.loginFrame)
        self.btnUserLogin.setGeometry(QtCore.QRect(190, 270, 171, 61))
        self.btnUserLogin.setStyleSheet("QWidget#btnUserLogin {\n"
"  background-color: rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #555555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QWidget#btnUserLogin:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(50, 100, 0, 219), stop:1 rgba(47, 124, 247, 219));\n"
"  color: white;\n"
"}")
        self.btnUserLogin.setObjectName("btnUserLogin")
        self.btnBack = QtWidgets.QPushButton(self.loginFrame)
        self.btnBack.setGeometry(QtCore.QRect(20, 270, 161, 61))
        self.btnBack.setStyleSheet("QWidget#btnBack {\n"
"  background-color: rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #555555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times New Roman\";\n"
"\n"
"}\n"
"\n"
"QWidget#btnBack:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(50, 100, 0, 219), stop:1 rgba(47, 124, 247, 219));\n"
"  color: white;\n"
"}")
        self.btnBack.setObjectName("btnBack")
        self.lblWelcome = QtWidgets.QLabel(self.loginFrame)
        self.lblWelcome.setGeometry(QtCore.QRect(20, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setStyleSheet("QWidget#lblWelcome{\n"
"    font: 9pt \"Georgia\";\n"
"    font: 75 30pt \"Garamond\";\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color:rgb(139, 0, 140);\n"
"    border-radius: 5px;\n"
"}")
        self.lblWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWelcome.setObjectName("lblWelcome")
        self.lblLoginTimer = QtWidgets.QLabel(self.loginFrame)
        self.lblLoginTimer.setGeometry(QtCore.QRect(10, 90, 361, 16))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblLoginTimer.setFont(font)
        self.lblLoginTimer.setStyleSheet("color: rgb(0, 0, 0);\n"
"font: 8pt \"Times New Roman\";\n"
"background: rgba(255, 255, 255, 0.0);")
        self.lblLoginTimer.setAlignment(QtCore.Qt.AlignCenter)
        self.lblLoginTimer.setObjectName("lblLoginTimer")
        self.txtUserName = QtWidgets.QLineEdit(self.loginFrame)
        self.txtUserName.setGeometry(QtCore.QRect(20, 130, 341, 51))
        self.txtUserName.setStyleSheet("QWidget#txtUserName {\n"
"  background-color: rgb(240, 255, 242);\n"
"  color: black;\n"
"  border: 2px solid #747474;\n"
"  border-radius:10px;\n"
"  font: 15pt \"Times New Roman\";\n"
"  padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"QWidget#txtUserName:hover {\n"
"  background-color: rgb(201, 255, 210);\n"
"  color: black;\n"
"}\n"
"    ")
        self.txtUserName.setObjectName("txtUserName")
        self.txtPassword = QtWidgets.QLineEdit(self.loginFrame)
        self.txtPassword.setGeometry(QtCore.QRect(20, 200, 341, 51))
        self.txtPassword.setStyleSheet("QWidget#txtPassword {\n"
" background-color: rgb(240, 255, 242);\n"
"  color: black;\n"
"  border: 2px solid #747474;\n"
"  border-radius:10px;\n"
"  font: 15pt \"Times New Roman\";\n"
"  padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"QWidget#txtPassword:hover {\n"
" background-color: rgb(201, 255, 210);\n"
"  color: black;\n"
"}\n"
"    ")
        self.txtPassword.setObjectName("txtPassword")
        self.label_2 = QtWidgets.QLabel(self.loginFrame)
        self.label_2.setGeometry(QtCore.QRect(70, 350, 121, 21))
        self.label_2.setStyleSheet("font: 75 10pt \"Times New Roman\";")
        self.label_2.setObjectName("label_2")
        self.label_Create = QtWidgets.QLabel(self.loginFrame)
        self.label_Create.setGeometry(QtCore.QRect(180, 350, 111, 21))
        self.label_Create.setTextFormat(QtCore.Qt.RichText)
        self.label_Create.setObjectName("label_Create")
        self.frameImage = QtWidgets.QLabel(self.bgWelcome)
        self.frameImage.setGeometry(QtCore.QRect(30, 20, 251, 421))
        self.frameImage.setStyleSheet("QWidget#frameImage {\n"
"background-image: url(C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/icons/bg.jpg); \n"
"background-repeat: no-repeat; \n"
"background-position: center;\n"
"border-radius: 20px;\n"
"border:2px solid rgba(0, 0, 0, 0);\n"
"border-top-color:rgba(46, 82, 101, 255);\n"
"border-left-color:rgba(46, 82, 101, 255);\n"
"border-right-color:rgba(46, 82, 101, 255);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n"
"padding-bottom:7px;\n"
"}\n"
"")
        self.frameImage.setText("")
        self.frameImage.setObjectName("frameImage")
        self.frameCover = QtWidgets.QFrame(self.bgWelcome)
        self.frameCover.setGeometry(QtCore.QRect(30, 20, 251, 421))
        self.frameCover.setStyleSheet("QWidget#frameCover {\n"
" background-color: rgba(0, 0, 0, 0.2);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QWidget#frameCover:hover {\n"
"  background-color: rgba(0, 0, 0, 0.0);\n"
"}\n"
"")
        self.frameCover.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameCover.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameCover.setObjectName("frameCover")
        main.setCentralWidget(self.bgWelcome)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Login"))
        self.btnUserLogin.setText(_translate("main", "Login"))
        self.btnBack.setText(_translate("main", "Back"))
        self.lblWelcome.setText(_translate("main", "Welcome Back !!!"))
        self.lblLoginTimer.setText(_translate("main", "Please Login"))
        self.txtUserName.setPlaceholderText(_translate("main", "Input User Name"))
        self.txtPassword.setPlaceholderText(_translate("main", "Input Your Password"))
        self.label_2.setText(_translate("main", "Not registered? "))
        self.label_Create.setText(_translate("main", "<html><head/><body><p align=\"center\"><span style=\" text-decoration: underline; color:#0055ff;\">Create an Account</span></p></body></html>"))

