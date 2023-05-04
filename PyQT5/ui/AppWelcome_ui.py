# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\Documents\Alox\Computer Vision\Skripsi2\PyQT5\ui\AppWelcome.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(690, 470)
        main.setMinimumSize(QtCore.QSize(690, 470))
        main.setMaximumSize(QtCore.QSize(690, 480))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main.setWindowIcon(icon)
        main.setStyleSheet("")
        self.bgWelcome = QtWidgets.QWidget(main)
        self.bgWelcome.setStyleSheet("QWidget#bgWelcome{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 0, 255, 0.8), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"}")
        self.bgWelcome.setObjectName("bgWelcome")
        self.lblWelcome = QtWidgets.QLabel(self.bgWelcome)
        self.lblWelcome.setGeometry(QtCore.QRect(10, 90, 671, 71))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(40)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lblWelcome.setFont(font)
        self.lblWelcome.setStyleSheet("QWidget#lblWelcome{\n"
"    font: 9pt \"Georgia\";\n"
"    font: 75 40pt \"Times New Roman\";\n"
"    color: rgb(255, 255, 255);\n"
"}")
        self.lblWelcome.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWelcome.setObjectName("lblWelcome")
        self.lblWelcome_2 = QtWidgets.QLabel(self.bgWelcome)
        self.lblWelcome_2.setGeometry(QtCore.QRect(0, 160, 691, 21))
        self.lblWelcome_2.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 12pt \"Times New Roman\";")
        self.lblWelcome_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lblWelcome_2.setObjectName("lblWelcome_2")
        self.btnLogin = QtWidgets.QPushButton(self.bgWelcome)
        self.btnLogin.setGeometry(QtCore.QRect(240, 230, 211, 41))
        self.btnLogin.setStyleSheet("QWidget#btnLogin {\n"
"  background-color:rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #55555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times new Roman\";\n"
"}\n"
"\n"
"QWidget#btnLogin:hover {\n"
"  background-color: rgb(148, 0, 211);\n"
"  color: white;\n"
"}")
        self.btnLogin.setObjectName("btnLogin")
        self.btnAccount = QtWidgets.QPushButton(self.bgWelcome)
        self.btnAccount.setGeometry(QtCore.QRect(240, 290, 211, 41))
        self.btnAccount.setStyleSheet("QWidget#btnAccount {\n"
"  background-color:rgb(0, 0, 139);\n"
"  color: white;\n"
"  border: 2px solid #55555;\n"
"  border-radius:10px;\n"
"  font: 75 12pt \"Times New Roman\";\n"
"}\n"
"\n"
"QWidget#btnAccount:hover {\n"
"  background-color:rgb(148, 0, 211);\n"
"  color: white;\n"
"}")
        self.btnAccount.setObjectName("btnAccount")
        main.setCentralWidget(self.bgWelcome)
        self.menubar = QtWidgets.QMenuBar(main)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 690, 26))
        self.menubar.setObjectName("menubar")
        main.setMenuBar(self.menubar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "Face Analisis System"))
        self.lblWelcome.setText(_translate("main", "Welcome Lecturer!"))
        self.lblWelcome_2.setText(_translate("main", "Sign in or create new account."))
        self.btnLogin.setText(_translate("main", "Log In"))
        self.btnAccount.setText(_translate("main", "Create New Account"))

import res_rc
