# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\asus\Documents\Alox\Computer Vision\Skripsi2\PyQT5\ui\AnalisisMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1182, 782)
        Form.setMinimumSize(QtCore.QSize(690, 460))
        Form.setMaximumSize(QtCore.QSize(1920, 1080))
        self.Background = QtWidgets.QWidget(Form)
        self.Background.setGeometry(QtCore.QRect(0, 0, 1181, 801))
        self.Background.setStyleSheet("QWidget#Background{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 0, 255, 0.8), stop:1 rgba(255, 255, 255, 255));\n"
" \n"
"}")
        self.Background.setObjectName("Background")
        self.camera = QtWidgets.QFrame(self.Background)
        self.camera.setGeometry(QtCore.QRect(160, 30, 871, 741))
        self.camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.camera.setObjectName("camera")
        self.listWidget = QtWidgets.QListWidget(self.Background)
        self.listWidget.setGeometry(QtCore.QRect(10, 21, 141, 761))
        self.listWidget.setObjectName("listWidget")
        self.Refresh = QtWidgets.QPushButton(self.Background)
        self.Refresh.setGeometry(QtCore.QRect(40, 30, 75, 23))
        self.Refresh.setObjectName("Refresh")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.Background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(1030, 30, 160, 741))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.Open_cam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Open_cam.setObjectName("Open_cam")
        self.verticalLayout.addWidget(self.Open_cam)
        self.Click_photo = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Click_photo.setObjectName("Click_photo")
        self.verticalLayout.addWidget(self.Click_photo)
        self.Open_folder = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Open_folder.setObjectName("Open_folder")
        self.verticalLayout.addWidget(self.Open_folder)
        self.Setting_cam = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.Setting_cam.setObjectName("Setting_cam")
        self.verticalLayout.addWidget(self.Setting_cam)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Refresh.setText(_translate("Form", "Refresh"))
        self.Open_cam.setText(_translate("Form", "Open Cam"))
        self.Click_photo.setText(_translate("Form", "Photo"))
        self.Open_folder.setText(_translate("Form", "Open Folder"))
        self.Setting_cam.setText(_translate("Form", "Setting Camera"))

