# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\Documents\Alox\Computer Vision\Skripsi2\PyQT5\ui\CreateAccount.ui'
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
        self.CreateAccountFrame = QtWidgets.QFrame(self.bgWelcome)
        self.CreateAccountFrame.setGeometry(QtCore.QRect(280, 40, 381, 381))
        self.CreateAccountFrame.setStyleSheet("QWidget#CreateAccountFrame{\n"
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
"QWidget#CreateAccountFrame:hover {\n"
"  background: rgba(255, 255, 255, 0.7);\n"
"  border-top:2px solid rgba(0, 0, 0, 0);\n"
"  border-top-color:rgba(99, 0, 0, 255);\n"
"  border-bottom:2px solid rgba(0, 0, 0, 0);\n"
"  border-bottom-color:rgba(99, 0, 0, 255);\n"
"  border-right:2px solid rgba(0, 0, 0, 0);\n"
"  border-right-color:rgba(99, 0, 0, 255);\n"
"}\n"
"")
        self.CreateAccountFrame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.CreateAccountFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.CreateAccountFrame.setLineWidth(5)
        self.CreateAccountFrame.setMidLineWidth(2)
        self.CreateAccountFrame.setObjectName("CreateAccountFrame")
        self.btnAccount = QtWidgets.QPushButton(self.CreateAccountFrame)
        self.btnAccount.setGeometry(QtCore.QRect(190, 270, 171, 61))
        self.btnAccount.setStyleSheet("QWidget#btnAccount {\n"
"  background-color: rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #555555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QWidget#btnAccount:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(50, 100, 0, 219), stop:1 rgba(47, 124, 247, 219));\n"
"  color: white;\n"
"}")
        self.btnAccount.setObjectName("btnAccount")
        self.btnBack = QtWidgets.QPushButton(self.CreateAccountFrame)
        self.btnBack.setGeometry(QtCore.QRect(20, 270, 161, 61))
        self.btnBack.setStyleSheet("QWidget#btnBack {\n"
" background-color: rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #555555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QWidget#btnBack:hover {\n"
"  background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(50, 100, 0, 219), stop:1 rgba(47, 124, 247, 219));\n"
"  color: white;\n"
"}")
        self.btnBack.setObjectName("btnBack")
        self.lblWelcome = QtWidgets.QLabel(self.CreateAccountFrame)
        self.lblWelcome.setGeometry(QtCore.QRect(20, 20, 341, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(30)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setStyleSheet("QWidget#lblWelcome{\n"
"    font: 9pt \"Georgia\";\n"
"    font: 75 30pt \"Times New Roman\";\n"
"    \n"
"    color: rgb(255, 255, 255);\n"
"    \n"
"    background-color: rgb(144, 39, 245);\n"
"    border-radius: 7px;\n"
"}")
        self.lblWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWelcome.setObjectName("lblWelcome")
        self.lblLoginTimer = QtWidgets.QLabel(self.CreateAccountFrame)
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
        self.new_username = QtWidgets.QLineEdit(self.CreateAccountFrame)
        self.new_username.setGeometry(QtCore.QRect(20, 130, 341, 51))
        self.new_username.setStyleSheet("QWidget#new_username {\n"
" background-color: rgb(240, 255, 242);\n"
"  color: black;\n"
"  border: 2px solid #747474;\n"
"  border-radius:10px;\n"
"  font: 15pt \"Times New Roman\";\n"
"  padding-left: 6px;\n"
"\n"
"}\n"
"\n"
"QWidget#txtUserName:hover {\n"
" background-color: rgb(201, 255, 210);\n"
"  color: black;\n"
"}")
        self.new_username.setObjectName("new_username")
        self.new_password = QtWidgets.QLineEdit(self.CreateAccountFrame)
        self.new_password.setGeometry(QtCore.QRect(20, 200, 341, 51))
        self.new_password.setStyleSheet("QWidget#new_password {\n"
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
        self.new_password.setObjectName("new_password")
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
        main.setWindowTitle(_translate("main", "Create New Account"))
        self.btnAccount.setText(_translate("main", "Create Account"))
        self.btnBack.setText(_translate("main", "Back"))
        self.lblWelcome.setText(_translate("main", "Create Account"))
        self.lblLoginTimer.setText(_translate("main", "Please Login"))
        self.new_username.setPlaceholderText(_translate("main", "Input New Username"))
        self.new_password.setPlaceholderText(_translate("main", "Input New Password"))

