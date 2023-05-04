# -*- coding: utf-8 -*-
"""
    @Created : Wed Feb 16 10:51:10 2022
    @author  : ---
    @desc    : Face expression recognition
"""
# import packages
import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
from PyQt5.QtGui import QPixmap
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtCore import QSize
import glob
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QDialog, QDialogButtonBox, QLabel, QVBoxLayout
import threading
import numpy as np
from PyQt5.QtCore import QEventLoop

import os
import glob
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout
import cv2
import os


from PyQt5.QtWidgets import QToolBar
from PyQt5.QtWidgets import QMainWindow, QToolBar, QWidget
from mtcnn.mtcnn import MTCNN
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMessageBox, QDialog, QMainWindow, QApplication
from PyQt5.QtGui import QIcon
#from tes1 import *

from datetime import datetime

import bleedfacedetector as fd
import sqlite3
import os
import time
import os
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QMainWindow, QToolBar, QListWidget, QListWidgetItem
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class AppWelcome(QMainWindow):
    # parameterized constructor
    def __init__(self):
        super(AppWelcome, self).__init__()
        loadUi(
            "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/ui/AppWelcome.ui", self)
        self.btnLogin.clicked.connect(self.gotoLoginForm)
        self.btnAccount.clicked.connect(self.gotoCreateAccountForm)

    def gotoLoginForm(self):
        login = LoginForm()
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def gotoCreateAccountForm(self):
        create = CreateAccount()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)


class LoginForm(QMainWindow):
    # parameterized constructor
    def __init__(self):
        super(LoginForm, self).__init__()
        loadUi(
            "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/ui/LoginForm.ui", self)
        # set the title
        self.setWindowTitle("Login")
        self.mainform = MainWindow()
        ##self.setWindowFlags(Qt.FramelessWindowHint)
        ##self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showDateTime)
        self.timer.start(1000)
        self.txtPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnBack.clicked.connect(self.gotoWelcomeForm)
        self.btnUserLogin.clicked.connect(self.checkLoginStatus)
        self.label_Create.mousePressEvent = self.gotoCreateAccount

    def gotoWelcomeForm(self):
        welcome = AppWelcome()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def showDateTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dddd, MMMM yyyy [hh:mm:ss]')
        self.lblLoginTimer.setText(timeDisplay)

    def gotoCreateAccount(self, event):
        create = CreateAccount()
        widget.addWidget(create)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def emptyField(self):
        self.txtUserName.setText("")
        self.txtPassword.setText("")

    def showLoginForm(self):
        widget.show()

    def hideLoginForm(self):
        widget.hide()

    def showMainWindow(self):
        self.mainform.show()

    def hideMainWindow(self):
        self.mainform.hide()

    def event(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)

    def checkLoginStatus(self):
        txtIDUser = self.txtUserName.text()
        txtPassUser = self.txtPassword.text()

        if len(txtIDUser) == 0 or len(txtPassUser) == 0:
            QMessageBox.warning(self, "Warning Message",
                                "Please, you need to input all fields.")

        else:
            conn = sqlite3.connect(
                "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/db/db_analisis.db")
            cur = conn.cursor()
            try:
                query = 'SELECT password FROM tbl_login WHERE username =\''+txtIDUser+"\'"
                cur.execute(query)
                result_pass = cur.fetchone()[0]  # get array index pertama
                if result_pass == txtPassUser:
                    print("Successfully logged in.")
                    QMessageBox.information(
                        self, "Infomation Message", "Welcome to this Analisis Face Expression System.")

                    self.emptyField()
                    self.hideLoginForm()
                    self.showMainWindow()

                else:
                    QMessageBox.warning(
                        self, "Warning Message", "Hi, we found invalid username or password.")
            except:
                QMessageBox.warning(
                    self, "Warning Message", "Please, check you username and password again.")


class CreateAccount(QMainWindow):
    # parameterized constructor
    def __init__(self):
        super(CreateAccount, self).__init__()
        loadUi(
            "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/ui/CreateAccount.ui", self)
        # set the title
        self.setWindowTitle("CreateAccount")
        self.mainform = MainWindow()
        ##self.setWindowFlags(Qt.FramelessWindowHint)
        ##self.setAttribute(Qt.WA_TranslucentBackground)
        self.timer = QTimer()
        self.timer.timeout.connect(self.showDateTime)
        self.timer.start(1000)
        self.new_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.btnBack.clicked.connect(self.gotoWelcomeForm)
        self.btnAccount.clicked.connect(self.createAccountStatus)

    def gotoWelcomeForm(self):
        welcome = AppWelcome()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def showDateTime(self):
        time = QDateTime.currentDateTime()
        timeDisplay = time.toString('dddd, MMMM yyyy [hh:mm:ss]')
        self.lblLoginTimer.setText(timeDisplay)

    def emptyField(self):
        self.txtUserName.setText("")
        self.txtPassword.setText("")

    def showCreateNewAccount(self):
        widget.show()

    def hideCreateNewAccount(self):
        widget.hide()

    def showLoginForm(self):
        widget.show()

    def showMainWindow(self):
        self.mainform.show()

    def hideMainWindow(self):
        self.mainform.hide()

    def event(self, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if event.key() in (QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
                self.focusNextPrevChild(True)
        return super().event(event)

    def createAccountStatus(self):
        username = self.new_username.text()
        password = self.new_password.text()

        if len(username) == 0 or len(password) == 0:
            QMessageBox.warning(self, "Warning Message",
                                "Please, you need to input all fields.")
        else:
            conn = sqlite3.connect(
                "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/db/db_analisis.db")
            cur = conn.cursor()

            user_info = [username, password]
            cur.execute(
                'INSERT INTO tbl_login (username, password) VALUES (?,?)', user_info)

            conn.commit()
            conn.close()

            login = LoginForm()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


class MainWindow(QMainWindow):
    # parameterized constructor
    def __init__(self):
        super(MainWindow, self).__init__()

        # setting geometry
        self.setGeometry(100, 100, 1000, 1000)

        # setting style sheet
        self.setStyleSheet(
            "QToolBar {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 0, 255, 0.8), stop:1 rgba(255, 255, 255, 255));} QToolBar::separator {background-color: white;}")

        # getting available cameras
        self.available_camera = QCameraInfo.availableCameras()

        # if no camera found
        if not self.available_camera:
            #exit the code
            sys.exit()

        # setting window title
        self.setWindowTitle("Analisis Cam")

        self.tampung_ekspresi = []
        self.tampung_mata = []
        self.hasil_otomatis = []
        # path to save
        self.save_path = "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/data_Wajah/"

        # path to save otomat
        self.save_otomat = "C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/otomatis/"
        #creating a QCameraViewfinder object
        self.viewfinder = QCameraViewfinder(self)

        # showing this viewfinder
        self.viewfinder.show()

        # making it central widget of main window
        self.setCentralWidget(self.viewfinder)

        # creating a tool bar
        toolbar = QToolBar("Camera Tool Bar")

        # Create timer
        self.timer = QTimer()
        # add toolbar to main window
        self.addToolBar(toolbar)

        # path icon
        path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/icons/'

        # creating a photo action to take photo
        #click_action = QAction(QIcon(path+'scanner--arrow.png'), "Take Photo", self)

        icon_otomatis = QIcon(
            QPixmap(path + 'clock.png').scaled(QSize(70, 70)))
        otomatis_action = QAction(icon_otomatis, "Atur Waktu Inteval", self)
        otomatis_action.setToolTip("Set Timer")
        otomatis_action.triggered.connect(self.otomatis)
        toolbar.addAction(otomatis_action)

        # creating action for open cam
        #open_cam_action = QAction(QIcon(QPixmap(path+'camera-black.png')).pixmap(QSize(30, 30)), "Open Cam", self)
        icon_open_cam = QIcon(
            QPixmap(path+'unlocked.png').scaled(QSize(70, 70)))
        open_cam_action = QAction(icon_open_cam, "Open Cam", self)
        open_cam_action.setToolTip("Open Cam")
        open_cam_action.triggered.connect(self.open_cam)
        toolbar.addAction(open_cam_action)

        # Mengambil widget QToolButton dari QAction
        #open_cam_widget = toolbar.widgetForAction(open_cam_action)
        # set style sheet to make the icon background round
        #open_cam_widget.setStyleSheet("QToolButton { border-radius: 10px; background-color: #ffffff; padding:20px; } \ QToolButton::hover { border: 2px solid black; }")

        icon_click = QIcon(QPixmap(path+'camera.png'))
        icon1 = icon_click.pixmap(100, 100)
        click_action = QAction(QIcon(icon1), "Take Photo", self)
        click_action.setStatusTip("This will capture picture")
        click_action.setToolTip("Capture picture")
        click_action.triggered.connect(self.click_photo)
        toolbar.addAction(click_action)

        # mengambil widget QToolButton dari QAction
        click_action_widget = toolbar.widgetForAction(click_action)
        # set style sheet to make the icon background round
        click_action_widget.setStyleSheet(
            "QToolButton { border-radius: 10px; background-color: #ffffff; padding:20px; } \ QToolButton::hover { border: 2px solid black; }")

        # similarly creating action for changin save folder
        #change_folder_action = QAction(QIcon(path+'folder.png'), "Change save location", self)
        icon_change_folder = QIcon(
            QPixmap(path + 'folder.png').scaled(QSize(100, 100)))
        change_folder_action = QAction(
            icon_change_folder, "Change Save Location", self)
        change_folder_action.setStatusTip(
            "Change folder where picture will be saved.")
        change_folder_action.setToolTip("Change save location")
        change_folder_action.triggered.connect(self.change_folder)
        toolbar.addAction(change_folder_action)

        #setting_cam = QAction(QIcon(path+'films.png'), 'change cam' ,self)
        #setting_cam.setStatusTip('This will change cam')

        # creating a combo box for selecting camera
        icon_select_cam = QIcon(
            QPixmap(path+'gear.png').scaled(QSize(100, 100)))
        select_cam_action = QAction(icon_select_cam, "Select Camera", self)
        select_cam_action.setToolTip("Select Camera")
        select_cam_action.triggered.connect(self.show_camera_selector)
        toolbar.addAction(select_cam_action)

        # add spacer to the toolbar
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        toolbar.addWidget(spacer)

        # set the toolbar properties
        toolbar.setMovable(True)
        toolbar.setFloatable(False)

        self.addToolBar(Qt.RightToolBarArea, toolbar)

        #self.setWindowTitle("Preview Image")
        #self.setGeometry(100, 100, 500, 500)

        # create QListWidget
        self.image_list = QListWidget(self)
        self.setCentralWidget(self.image_list)

        # add images to QListWidget
        self.add_images_to_list()
        #self.load_images()

        # create left toolbar
        left_toolbar = QToolBar("Left Toolbar", self)
        self.addToolBar(Qt.LeftToolBarArea, left_toolbar)

        # add refresh action to toolbar
        refresh_action = QAction(
            QIcon(path+"arrow-circle-225.png"), "Refresh", self)
        refresh_action.triggered.connect(self.load_images)
        left_toolbar.addAction(refresh_action)

        # add QListWidget to left toolbar
        left_toolbar.addWidget(self.image_list)

        # create file system event handler
        self.event_handler = FileSystemEventHandler()
        self.event_handler.on_created = self.add_images_to_list
        self.event_handler.on_modified = self.add_images_to_list

        # create observer and start watching the folder
        self.observer = Observer()
        self.observer.schedule(
            self.event_handler, self.folder_path, recursive=True)
        self.observer.start()

        self.akhir = []

        # creating a new toolbar to hold the first toolbar and an empty widget
        right_toolbar = QToolBar()
        # create a vertical layout for the toolbars
        right_toolbar.resize(100, 100)
        # add empty widget to push first toolbar to the left
        right_toolbar.addWidget(QWidget())

        # add a separator to push the next widget to the right
        right_toolbar.addSeparator()

        # add a spacer widget to push the next widget to the center
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_toolbar.addWidget(spacer)

        # add first toolbar to second toolbar
        right_toolbar.addWidget(toolbar)

        # add a toolbar break to the status bar
        self.addToolBarBreak()

        # add second toolbar to status bar
        self.addToolBar(Qt.RightToolBarArea, right_toolbar)
        right_layout = QVBoxLayout()
        # set the margins to 0 to avoid extra space
        right_toolbar.setContentsMargins(0, 0, 0, 0)
        right_toolbar.addWidget(toolbar)
        right_toolbar.setLayout(right_layout)
        right_toolbar.setOrientation(Qt.Vertical)

        # setting tool bar stylesheet
        toolbar.setStyleSheet(
            "QToolBar {background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(5, 0, 255, 0.8), stop:1 rgba(255, 255, 255, 255));} QToolBar::separator {background-color: white;}")

        # membuat QToolBar dan menambahkan item toolbar
        toolbar = QToolBar()
        toolbar.addAction(QAction("", self))
        toolbar.addAction(QAction("", self))
        toolbar.addAction(QAction("", self))

        # membuat QToolBar dan menambahkan toolbar vertikal
        vertical_toolbar = QToolBar()

        vertical_toolbar.addWidget(toolbar)

        self.addToolBarBreak()
        # add a spacer widget to push the next widget to the center
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        right_toolbar.addWidget(spacer)

        # membuat QToolBar dan menambahkan item toolbar
        toolbar = QToolBar()
        toolbar.addAction(QAction("", self))
        toolbar.addAction(QAction("", self))
        toolbar.addAction(QAction("", self))

        # membuat QToolBar dan menambahkan toolbar vertikal
        vertical_toolbar = QToolBar()
        vertical_toolbar.setOrientation(Qt.Vertical)
        vertical_toolbar.addWidget(toolbar)

    def otomatis(self):
        # Create dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Analisa Otomatis")
        dialog_layout = QVBoxLayout(dialog)
        # Set the size of the dialog box's window0
        dialog.resize(50, 100)

        # create label
        label = QLabel(dialog)
        label.setText(
            "Analisa otomatis wajah mahasiswa dengan menggunakan interval waktu.")
        dialog_layout.addWidget(label)

        # create button for closing the dialog
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        ok_button = button_box.button(
            QDialogButtonBox.Ok)  # get the cancel button
        ok_button.setText("Start")  # set the text label to "Start"
        cancel_button = button_box.button(
            QDialogButtonBox.Cancel)  # get the cancel button
        cancel_button.setText("Stop")  # set the text label to "Stop"

        button_box.rejected.connect(self.stop_timer)
        dialog_layout.addWidget(button_box)

        # Connect slot for "Ok" button
        button_box.accepted.connect(self.start_timer)
        dialog.exec_()

    # function to start the timer and capture image every 5 seconds
    # and generate pie chart after 15 minutes
    def start_timer(self):
        minutes = 0
        seconds = 0
        total_time = 900  # 15 minutes in seconds
        running = True  # timer is running
        results = []  # list to store analysis results

        while running:
            print(f"Time elapsed: {minutes} minutes {seconds} seconds")
            time.sleep(1)  # wait one second
            seconds += 1

            if seconds % 900 == 0:    
                print("Capturing image...")
                self.otomat_photo()  # perform analysis on current photo

            if seconds % 10800 == 0:
                running = False

                self.generate_pie_chart(predictions=self.tampung_ekspresi)
                
                print("All detected emotions:", self.tampung_ekspresi)

                print("Timer stopped.")
                break

            if seconds == 60:
                minutes += 1
                seconds = 0

        return f"Total time elapsed: {minutes} minutes {seconds} seconds"

    # stop time
    def stop_timer(self):
        global running
        running = False
        self.generate_pie_chart(predictions=self.tampung_ekspresi)
        #self.generate_pie_chart_sleepy()

    def create_folder_new1(self):
        folder_name = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        folder_path = os.path.join(self.save_otomat, folder_name)
        i = 1
        while os.path.exists(folder_path):
            folder_path = os.path.join(self.save_otomat, f"{folder_name}_{i}")
            i += 1
        os.makedirs(folder_path)
        return folder_path

    
    def load_images(self):

        # clear existing items from QListWidget
        self.image_list.clear()

        # add images to QListWidget
        self.folder_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/otomatis'

        # get the most recently modified subdirectory
        subdirs = [os.path.join(self.folder_path, name) for name in os.listdir(
            self.folder_path) if os.path.isdir(os.path.join(self.folder_path, name))]
        latest_subdir = max(subdirs, key=os.path.getmtime)

        # get all image files in the most recently modified subdirectory
        files = [os.path.join(latest_subdir, f) for f in os.listdir(
            latest_subdir) if f.endswith('.jpg')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        # add the most recently modified image files to the list widget
        for file in files:
            item = QListWidgetItem()
            pixmap = QPixmap(file).scaledToWidth(200)
            item.setIcon(QIcon(pixmap))
            item.setText(os.path.basename(file))
            # store file path in item data
            item.setData(Qt.UserRole, file)
            self.image_list.addItem(item)

    def add_images_to_list(self):

        # clear existing items from QListWidget
        self.image_list.clear()

        # add images to QListWidget
        self.folder_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/otomatis'

        # get the most recently modified subdirectory
        subdirs = [os.path.join(self.folder_path, name) for name in os.listdir(
            self.folder_path) if os.path.isdir(os.path.join(self.folder_path, name))]
        latest_subdir = max(subdirs, key=os.path.getmtime)

        # get all image files in the most recently modified subdirectory
        files = [os.path.join(latest_subdir, f) for f in os.listdir(
            latest_subdir) if f.endswith('.jpg')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        # add the most recently modified image files to the list widget
        for file in files:
            item = QListWidgetItem()
            pixmap = QPixmap(file).scaledToWidth(200)
            item.setIcon(QIcon(pixmap))
            item.setText(os.path.basename(file))
            # store file path in item data
            item.setData(Qt.UserRole, file)
            self.image_list.addItem(item)
        self.image_list.itemDoubleClicked.connect(self.show_fullscreen_image)

    def show_camera_selector(self):
        # create dialog
        dialog = QDialog(self)
        dialog.setWindowTitle("Select Camera")
        dialog_layout = QVBoxLayout(dialog)

        # create label
        label = QLabel(dialog)
        label.setText("Select Camera")
        dialog_layout.addWidget(label)

        # create combo box for selecting camera
        camera_selector = QComboBox(dialog)
        camera_selector.addItems([camera.description()
                                 for camera in self.available_camera])
        dialog_layout.addWidget(camera_selector)

        # create button for closing the dialog
        button_box = QDialogButtonBox(
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel, dialog)
        button_box.accepted.connect(dialog.accept)
        button_box.rejected.connect(dialog.reject)
        dialog_layout.addWidget(button_box)

        # show dialog
        result = dialog.exec_()
        if result == QDialog.Accepted:
            # handle camera selection
            selected_camera = camera_selector.currentText()
            self.camera = selected_camera  # set selected camera as default camera
            print("Selected camera:", selected_camera)

    def load_images(self):

        # clear existing items from QListWidget
        self.image_list.clear()

        # add images to QListWidget
        self.folder_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/emotion'

        # get the most recently modified subdirectory
        subdirs = [os.path.join(self.folder_path, name) for name in os.listdir(
            self.folder_path) if os.path.isdir(os.path.join(self.folder_path, name))]
        latest_subdir = max(subdirs, key=os.path.getmtime)

        # get all image files in the most recently modified subdirectory
        files = [os.path.join(latest_subdir, f) for f in os.listdir(
            latest_subdir) if f.endswith('.jpg')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        # add the most recently modified image files to the list widget
        for file in files:
            item = QListWidgetItem()
            pixmap = QPixmap(file).scaledToWidth(200)
            item.setIcon(QIcon(pixmap))
            item.setText(os.path.basename(file))
            # store file path in item data
            item.setData(Qt.UserRole, file)
            self.image_list.addItem(item)

    def add_images_to_list(self):

        # clear existing items from QListWidget
        self.image_list.clear()

        # add images to QListWidget
        self.folder_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/emotion'

        # get the most recently modified subdirectory
        subdirs = [os.path.join(self.folder_path, name) for name in os.listdir(
            self.folder_path) if os.path.isdir(os.path.join(self.folder_path, name))]
        latest_subdir = max(subdirs, key=os.path.getmtime)

        # get all image files in the most recently modified subdirectory
        files = [os.path.join(latest_subdir, f) for f in os.listdir(
            latest_subdir) if f.endswith('.jpg')]
        files.sort(key=lambda x: os.path.getmtime(x), reverse=True)

        # add the most recently modified image files to the list widget
        for file in files:
            item = QListWidgetItem()
            pixmap = QPixmap(file).scaledToWidth(200)
            item.setIcon(QIcon(pixmap))
            item.setText(os.path.basename(file))
            # store file path in item data
            item.setData(Qt.UserRole, file)
            self.image_list.addItem(item)
        self.image_list.itemDoubleClicked.connect(self.show_fullscreen_image)

    def show_image(self, item):
        # get file path from item data
        file_path = item.data(Qt.UserRole)

        # create image viewer widget
        image_viewer = ImageViewer(file_path)
        image_viewer.show()

    def show_fullscreen_image(self, item):
        file_path = item.data(Qt.UserRole)  # get file path from item data
        image = QPixmap(file_path).scaled(
            1000, 1000, aspectRatioMode=Qt.KeepAspectRatio)

        # create dialog
        dialog = QDialog(self)
        dialog.setWindowTitle(file_path)
        dialog_layout = QVBoxLayout(dialog)

        # create label with image
        label = QLabel(dialog)
        label.setPixmap(image)
        dialog_layout.addWidget(label)

        # show dialog
        dialog.exec_()

    def update_preview(self):
        for widget in self.preview_widget.children():
            widget.deleteLater()
        for foldername in glob.glob(self.image_folder + "/*"):
            if os.path.isdir(foldername):
                for filename in glob.glob(os.path.join(foldername, "*.jpg")):
                    pixmap = QPixmap(filename)
                    label = QLabel(self.preview_widget)
                    label.setPixmap(pixmap.scaledToWidth(200))
                    label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                    self.preview_layout.addWidget(label)
        self.preview_layout.addStretch()

    def select_camera(self, i):

        # getting the selected camera
        self.camera = QCamera(self.available_camera[i])

        self.viewfinder1 = QCameraViewfinder(self)
        self.viewfinder1.show()
        # making it central widget of main window
        self.setCentralWidget(self.viewfinder1)
        # setting view finder to the camera
        self.camera.setViewfinder(self.viewfinder1)

        # setting capture mode to the camera
        #self.camera.setCaptureMode(QCamera.CaptureStillImage)

        # if any error occur show the alert
        self.camera.error.connect(lambda: self.lert(self.camera.errorString()))

        # start the camera
        self.camera.start()

        # creating a QCameraImageCapture object
        self.capture = QCameraImageCapture(self.camera)

        # showing alert if error occur
        self.capture.error.connect(
            lambda error_msg, error, msg: self.alert(msg))

        # connect imageSaved otomatis signal to slot
        #self.capture.imageSaved.connect(self.handle_image_saved1)

        # connect imageSaved signal to slot
        self.capture.imageSaved.connect(self.handle_image_saved)

        # getting current camera name

        self.current_camera_name = self.available_camera[i].description()

        # initial save sequence
        self.save_seq = 0
        #self.capture.imageCaptured.connect(self.mata_mengantuk)

    def init_emotion(self, model='C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/model/emotion-ferplus-8.onnx'):
        global net, emotions

        emotions = ['Neutral', 'Happy', 'Surprise',
                    'Sad', 'Anger', 'Disgust', 'Fear', 'Contempt']

        net = cv2.dnn.readNetFromONNX(model)

    def detect_emotion1(self, image_path, faces, folder_path):
        # load classifier for eye detection
        eye_cascade1 = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml")
        eye_cascade2 = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

        img = cv2.imread(image_path)
        aug_img = cv2.convertScaleAbs(img, alpha=1.5, beta=50)
        if img is not None:
            faces = fd.ssd_detect(aug_img)
            padding = 3
            count_img = 0

            prediction_tuple = ""
            prediction_tuple1 = ""
            predictions = []

            for face in faces:
                # inisialisasi variabel sleepy untuk setiap wajah
                sleepy = ''
                x, y, w, h = face
                # draw rectangle around face
                cv2.rectangle(img, (x-padding, y-padding),
                              (x+w+padding, y+h+padding), (255, 0, 0), 2)

                # crop face region
                face = aug_img[y-padding:y+h+padding, x-padding:x+w+padding]

                # preprocess face image
                gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #gray = cv2.equalizeHist(gray)
                #gray = cv2.GaussianBlur(gray, (5, 5), 0)

                # detect eyes
                eyes1 = eye_cascade1.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

                eyes2 = eye_cascade2.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

                resized_face = cv2.resize(gray, (64, 64))

                processed_face = resized_face.reshape(1, 1, 64, 64)

                net.setInput(processed_face.astype(np.float32))
                output = net.forward()

                expanded = np.exp(output - np.max(output))
                probablities = expanded / expanded.sum()

                prob = np.squeeze(probablities)

                predicted_emotion = emotions[prob.argmax()]

                # check if both eyes are detected
                if len(eyes1) == 1 or len(eyes2) == 1 and len(eyes1) == 2 or len(eyes2) == 2:
                    # both eyes detected, draw rectangles around both eyes
                    for (ex, ey, ew, eh) in eyes1:
                        cv2.rectangle(face, (ex-padding, ey-padding),
                                      (ex+ew+padding, ey+eh+padding), (0, 255, 0), 2)

                    for (ex, ey, ew, eh) in eyes2:
                        cv2.rectangle(face, (ex-padding, ey-padding),
                                      (ex+ew+padding, ey+eh+padding), (0, 255, 0), 2)
                        
                     # Set path untuk menyimpan gambar hasil deteksi pada folder baru
                    filename = os.path.basename(image_path)
                    name, ext = os.path.splitext(filename)
                    save_folder = os.path.join(folder_path)
                    save_path = os.path.join(
                        save_folder, f"{name}_{predicted_emotion}_{count_img}_full image{ext}")
                    cv2.imwrite(save_path, img)
                    # menyimpan file
                    save_folder2 = os.path.join(folder_path)
                    os.makedirs(save_folder2, exist_ok=True)
                    save_path2 = os.path.join(
                        save_folder2, f"{name}_{predicted_emotion}_{count_img}{ext}")
                    cv2.imwrite(save_path2, face)
                    prediction_tuple = (predicted_emotion)
                    self.tampung_ekspresi.append(prediction_tuple)
                    
                else:
                    # set sleepy if no eye is detected
                    sleepy = "Sleepy"
                    
                    # Set path untuk menyimpan gambar hasil deteksi pada folder baru
                    filename = os.path.basename(image_path)
                    name, ext = os.path.splitext(filename)
                    save_folder = os.path.join(folder_path)
                    save_path = os.path.join(
                        save_folder, f"{name}_{sleepy}_{count_img}_full image{ext}")
                    cv2.imwrite(save_path, img)
                    # menyimpan file
                    save_folder2 = os.path.join(folder_path)
                    os.makedirs(save_folder2, exist_ok=True)
                    save_path2 = os.path.join(
                        save_folder2, f"{name}_{sleepy}_{count_img}{ext}")
                    cv2.imwrite(save_path2, face)
                    prediction_tuple1 = (sleepy)
                    self.tampung_ekspresi.append(prediction_tuple1)
                    
                cv2.putText(img, '{}'.format(self.tampung_ekspresi), (x, y+h+(1*20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (60, 20, 220), 1, cv2.LINE_AA)

                count_img = count_img + 1

            # Generate pie chart
            classes = set(predictions)
            percentages = [predictions.count(label) for label in classes]
            self.show_pie_chart(classes, percentages)
            #self.save_to_database(classes, percentages)
            return img
        else:
            print("Error: Failed to read image.")
            return None

    def detect_emotion2(self, image_path, faces, folder_path):
        # load classifier for eye detection
        eye_cascade1 = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye.xml")
        eye_cascade2 = cv2.CascadeClassifier(
            cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")

        img = cv2.imread(image_path)
        aug_img = cv2.convertScaleAbs(img, alpha=1.5, beta=50)
        if img is not None:
            faces = fd.ssd_detect(aug_img)
            padding = 3
            count_img = 0

            prediction_tuple = ""
            prediction_tuple1 = ""
            predictions = []

            for face in faces:
                # inisialisasi variabel sleepy untuk setiap wajah
                sleepy = ''
                x, y, w, h = face
                # draw rectangle around face
                cv2.rectangle(img, (x-padding, y-padding),
                              (x+w+padding, y+h+padding), (255, 0, 0), 2)

                # crop face region
                face = aug_img[y-padding:y+h+padding, x-padding:x+w+padding]

                # preprocess face image
                gray = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                #gray = cv2.equalizeHist(gray)
                #gray = cv2.GaussianBlur(gray, (5, 5), 0)

                # detect eyes
                eyes1 = eye_cascade1.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

                eyes2 = eye_cascade2.detectMultiScale(
                    gray, scaleFactor=1.1, minNeighbors=5, minSize=(20, 20), flags=cv2.CASCADE_SCALE_IMAGE)

                resized_face = cv2.resize(gray, (64, 64))

                processed_face = resized_face.reshape(1, 1, 64, 64)

                net.setInput(processed_face.astype(np.float32))
                output = net.forward()

                expanded = np.exp(output - np.max(output))
                probablities = expanded / expanded.sum()

                prob = np.squeeze(probablities)

                predicted_emotion = emotions[prob.argmax()]

                # check if both eyes are detected
                if len(eyes1) == 1 or len(eyes2) == 1 and len(eyes1) == 2 or len(eyes2) == 2:
                    # both eyes detected, draw rectangles around both eyes
                    for (ex, ey, ew, eh) in eyes1:
                        cv2.rectangle(face, (ex-padding, ey-padding),
                                      (ex+ew+padding, ey+eh+padding), (0, 255, 0), 2)

                    for (ex, ey, ew, eh) in eyes2:
                        cv2.rectangle(face, (ex-padding, ey-padding),
                                      (ex+ew+padding, ey+eh+padding), (0, 255, 0), 2)
                    # Set path untuk menyimpan gambar hasil deteksi pada folder baru
                    filename = os.path.basename(image_path)
                    name, ext = os.path.splitext(filename)
                    save_folder = os.path.join(folder_path)
                    save_path = os.path.join(
                        save_folder, f"{name}_{predicted_emotion}_{count_img}_full image{ext}")
                    cv2.imwrite(save_path, img)
                    # menyimpan file
                    save_folder2 = os.path.join(folder_path)
                    os.makedirs(save_folder2, exist_ok=True)
                    save_path2 = os.path.join(
                        save_folder2, f"{name}_{predicted_emotion}_{count_img}{ext}")
                    cv2.imwrite(save_path2, face)
                    prediction_tuple = (predicted_emotion)
                    predictions.append(prediction_tuple)
                else:
                    # set sleepy if no eye is detected
                    sleepy = "Sleepy"
                    # Set path untuk menyimpan gambar hasil deteksi pada folder baru
                    filename = os.path.basename(image_path)
                    name, ext = os.path.splitext(filename)
                    save_folder = os.path.join(folder_path)
                    save_path = os.path.join(
                        save_folder, f"{name}_{sleepy}_{count_img}_full image{ext}")
                    cv2.imwrite(save_path, img)
                    # menyimpan file
                    save_folder2 = os.path.join(folder_path)
                    os.makedirs(save_folder2, exist_ok=True)
                    save_path2 = os.path.join(
                        save_folder2, f"{name}_{sleepy}_{count_img}{ext}")
                    cv2.imwrite(save_path2, face)
                    prediction_tuple1 = (sleepy)
                    predictions.append(prediction_tuple1)

                cv2.putText(img, '{}'.format(predictions), (x, y+h+(1*20)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (60, 20, 220), 1, cv2.LINE_AA)

                
                count_img = count_img + 1

            # Generate pie chart
            classes = set(predictions)
            percentages = [predictions.count(label) for label in classes]
            self.show_pie_chart(classes, percentages)
            
            return img
        else:
            print("Error: Failed to read image.")
            return None


    def generate_pie_chart(self, predictions):
        classes = set(predictions)
        percentages = [predictions.count(label) for label in classes]
        self.show_pie_chart(classes, percentages)

    # Untuk menampilkan pie chart
    def show_pie_chart(self):
        if len(self.tampung_ekspresi) == 0:
            QMessageBox.warning(
                self, "Warning", "Tidak ada gambar yang diproses")
            return

        classes = self.emotion_dict.values()
        percentages = [0] * len(classes)

        # count the number of predictions for each class
        for pred in self.tampung_ekspresi:
            pred_idx = pred.argmax()
            percentages[pred_idx] += 1

        # calculate percentage for each class
        percentages = [p / len(self.tampung_ekspresi)
                       * 100 for p in percentages]

        # create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # create matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # create toolbar and status bar
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        close_button = QPushButton("Close Report")
        close_button.clicked.connect(self.on_close)
        main_layout.addWidget(close_button)
        # download pie chart
        download_action = QPushButton("Download Report")
        download_action.clicked.connect(self.download_pie_chart)
        main_layout.addWidget(download_action)

        # set central widget and show
        self.setCentralWidget(main_widget)
        main_widget.resize(600, 600)
        self.show()

        # create pie chart
        ax = self.figure.add_subplot(111)
        ax.pie(percentages, labels=classes, autopct='%1.1f%%')

        # add label to each slice
        for i, pie_wedge in enumerate(ax.patches):
            # calculate the percentage of people in the class
            percent = percentages[i]
            num = int(round(percent / 100 * len(self.tampung_ekspresi)))

            # create label
            label = "{}\n{} orang".format(classes[i], num)

            x, y = pie_wedge.center
            theta1, theta2 = pie_wedge.theta1, pie_wedge.theta2
            r = 0.9 * pie_wedge.r
            x_label = x + r * np.cos(np.pi/35 * (theta1 + theta2)/2)
            y_label = y + r * np.sin(np.pi/35 * (theta1 + theta2)/2)
            bbox_props = dict(boxstyle="round",
                              facecolor="wheat", alpha=0.5, pad=0.5)

            ax.text(x_label, y_label, label, ha='left',
                    va='top', bbox=bbox_props)

        self.canvas.draw()

        # connect close event to canvas
        self.canvas.mpl_connect('close_event', self.on_close)

    # Untuk menampilkan pie chart

    def show_pie_chart(self, classes, percentages):
        classes = list(classes)
        # calculate the number of people in each class
        num_people = [int(round(p * 100 / 100)) for p in percentages]

        # create main widget and layout
        main_widget = QWidget(self)
        main_layout = QVBoxLayout(main_widget)

        # create matplotlib figure and canvas
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        main_layout.addWidget(self.canvas)

        # create toolbar and status bar
        self.toolbar = QToolBar(self)
        self.addToolBar(self.toolbar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)
        close_button = QPushButton("Close Report")
        close_button.clicked.connect(self.on_close)
        main_layout.addWidget(close_button)
        # download pie chart
        download_action = QPushButton("Download Report")
        download_action.clicked.connect(self.download_pie_chart)
        main_layout.addWidget(download_action)

        # set central widget and show
        self.setCentralWidget(main_widget)
        main_widget.resize(600, 600)
        self.show()

        # create pie chart
        ax = self.figure.add_subplot(111)
        ax.pie(percentages, labels=classes, autopct='%1.1f%%')

        # add label to each slice
        for i, pie_wedge in enumerate(ax.patches):
            # calculate the percentage of people in the class
            percent = num_people[i] / len(classes) * 100
            num = num_people[i]

            # create label
            label = "{}\n{} orang".format(classes[i], num)

            x, y = pie_wedge.center
            theta1, theta2 = pie_wedge.theta1, pie_wedge.theta2
            r = 0.9 * pie_wedge.r
            x_label = x + r * np.cos(np.pi/35 * (theta1 + theta2)/2)
            y_label = y + r * np.sin(np.pi/35 * (theta1 + theta2)/2)
            bbox_props = dict(boxstyle="round",
                              facecolor="wheat", alpha=0.5, pad=0.5)

            ax.text(x_label, y_label, label, ha='left',
                    va='top', bbox=bbox_props)

        self.canvas.draw()

        # connect close event to canvas
        self.canvas.mpl_connect('close_event', self.on_close)

    def download_pie_chart(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Pie Chart", "untitled.pdf", "PDF (*.pdf)")
        if file_path:
            self.figure.savefig(file_path)
            QMessageBox.information(
                self, "Download Pie Chart", "Pie Chart downloaded successfully!")

    # menutup pie chart dan menjalankan kamera baru
    def on_close(self, event):
        self.canvas.close()

        self.select_camera(0)

        # create a new instance of QCameraViewFinder
        self.viewfinder = QCameraViewfinder(self)

        # set the viewfinder to the camera object
        self.camera.setViewfinder(self.viewfinder)

        # start the camera
        self.camera.start()

        # add the viewfinder widget to the main window
        self.setCentralWidget(self.viewfinder)

    # Untuk membuat directory per date
    def create_folder(self):
        now = datetime.now()
        folder_name = now.strftime("%Y-%m-%d_%H-%M-%S")
        folder_path = os.path.join(
            'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/emotion/', folder_name)

        #while os.path.exists(folder_path):
        #   folder_name += '_1'
        #    folder_path = os.path.join(
        #   'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/emotion/', folder_name)

        os.makedirs(folder_path)

        return folder_path

    def create_folder_new(self):
        now = datetime.now()
        folder_name = now.strftime("Otomatis-%Y-%m-%d_%H-%M-%S")
        folder_path_otomatis = os.path.join(
            'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/emotion/', folder_name)

        #os.makedirs(folder_path_otomatis)

        return folder_path_otomatis

    def otomat_photo(self):
        self.capture = QCameraImageCapture(self.camera)
        # set filename with timestamp
        filename = f"analysis_face_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.jpg"
        image_path = os.path.join(self.save_otomat, filename)

        # remove existing image file if it exists
        if os.path.exists(image_path):
            os.remove(image_path)
            print("Existing image file removed.")

        # capture photo from camera
        self.capture.capture(os.path.join(self.save_otomat, filename))

        loop = QEventLoop()
        self.capture.imageCaptured.connect(loop.quit)
        loop.exec_()

        # save result of face analysis to self.tampung_ekspresi
        result = self.handle_image_saved_otomat(image_path)

        print(f"New image file saved: {image_path}")
        self.lihat_emosi()

        # check if the image has been saved
        if os.path.exists(image_path):
            print("Gambar berhasil tersimpan pada path: ", image_path)

        else:
            print("Gagal menyimpan gambar pada path: ", image_path)

    def lihat_emosi(self):
        if len(self.tampung_ekspresi) == 0:
            print("Tidak ada data emosi yang tersedia")
        else:
            for i, emosi in enumerate(self.tampung_ekspresi):
                print(f"Emosi ke-{i+1}: {emosi}")

    def click_photo(self, image_path):

        # capture the image and save it on the save path
        image_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/data_Wajah/analysis_face.jpg'

        # menghapus file gambar
        if os.path.exists(image_path):
            os.remove(image_path)
            print("File gambar utama berhasil dihapus.")

        else:
            print("File gambar utama tidak ditemukan.")

        # capture photo from camere
        self.capture.capture(os.path.join(
            self.save_path, "%s.jpg" % ("analysis_face")))

    def handle_image_saved_otomat(self, image_path):

        # Jalankan fungsi expression detection

        if os.path.exists(image_path):
            self.init_emotion()
            folder_path1 = self.create_folder_new()
            pixels = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
            detector = MTCNN()
            result1 = detector.detect_faces(pixels)
            result_image = self.detect_emotion1(
                image_path, result1, folder_path1)
            masuk_folder = cv2.imwrite(image_path, result_image)
        else:
            print(f"Image file {image_path} not found.")

    def handle_image_saved(self, image_path):

        print("FILE ALLREACY SAVED.")
        image_path = 'C:/Users/asus/Documents/Alox/Computer Vision/Skripsi2/PyQT5/data_Wajah/analysis_face.jpg'
        print(image_path)

        # Jalankan fungsi expression detection

        if os.path.exists(image_path):
            self.init_emotion()
            folder_path = self.create_folder()
            pixels = cv2.cvtColor(cv2.imread(image_path), cv2.COLOR_BGR2RGB)
            detector = MTCNN()
            result = detector.detect_faces(pixels)
            result_image = self.detect_emotion2(
                image_path, result, folder_path)
            masuk_folder = cv2.imwrite(image_path, result_image)
        else:
            print(f"Image file {image_path} not found.")

    def open_cam(self):
        self.open_cam = self.select_camera(0)

    def change_folder(self):

        # open the dialog to select path
        path = QFileDialog.getExistingDirectory(self, "Picture Location", "")

        # if path is selected
        if path:

            # update the path
            self.save_path = path

            # update the sequence
            self.save_seq = 0

    # method for alerts

    def alert(self, msg):
        # error message
        error = QErrorMessage(self)

        # setting text to the error message
        error.showMessage(msg)

    def showMainWindow(self):
        widget.show()

    def showLoginForm(self):
        widget.show()

    def hideLoginForm(self):
        widget.hide()

    def hidevideoCapture(self):
        widget.hide()

    def closeEvent(self, event):
        close = QMessageBox()
        close.setWindowTitle("Exit")
        close.setText("Are you sure want to close this Application?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            self.camera.stop()
            #event.accept()
            self.showLoginForm()

            #widget.setCurrentIndex(widget.currentIndex()+1);
        else:
            event.ignore()


class ImageViewer(QWidget):

    def __init__(self, file_path):
        super().__init__()

        # create label to display the image
        self.image_label = QLabel(self)
        self.image_label.setAlignment(Qt.AlignCenter)
        self.setFixedSize(800, 800)

        # load the image from file
        pixmap = QPixmap(file_path)
        self.image_label.setPixmap(pixmap)


if __name__ == '__main__':
    # Create application
    app = QApplication(sys.argv)

    # Create object
    welcome = AppWelcome()

    # Working with multiple forms/screens (swich screen).
    widget = QtWidgets.QStackedWidget()

    # Add widget
    widget.addWidget(welcome)
    widget.setFixedHeight(460)
    widget.setFixedWidth(690)
    #widget.setWindowOpacity(0.5)
    # set window title in Python PyQt5
    widget.setWindowTitle('Face Analysis App')
    widget.setWindowIcon(QtGui.QIcon('./icons/logo.png'))
    widget.show()

    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
