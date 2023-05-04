# import packages
import sys
import cv2
import numpy as np
import re
#import os
#os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = 'C:/path/to/qt/plugins/platforms'

from PyQt5.QtWidgets import QMainWindow, QToolBar, QHBoxLayout, QWidget
from matplotlib import pyplot
from matplotlib.patches import Rectangle
from matplotlib.patches import Circle
from mtcnn.mtcnn import MTCNN
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QTextCursor
from PyQt5.QtWidgets import QApplication, QTextBrowser, QWidget, QVBoxLayout, QLabel

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *

from PyQt5.uic import loadUi
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QDateTime
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QMessageBox, QDialog, QMainWindow, QApplication
from PyQt5.QtGui import QIcon
#from tes1 import *
from PIL import Image
from datetime import datetime

import bleedfacedetector as fd
import sqlite3
import os
import time

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Setting window geometry and title
        self.setGeometry(100, 100, 800, 600)
        self.setWindowTitle("Camera")

        # Setting background color
        self.setStyleSheet("background-color: lightgray;")

        # Creating viewfinder to show camera output
        self.viewfinder = QCameraViewFinder()
        self.viewfinder.setFixedSize(640, 480)
        self.setCentralWidget(self.viewfinder)

        # Creating a tool bar to hold the camera control buttons
        toolbar = QToolBar("Camera Tool Bar")
        toolbar.setMovable(False)
        self.addToolBar(toolbar)

        # Creating the "Open Camera" button
        open_camera_button = QAction(QIcon('open_camera.png'), "Open Camera", self)
        open_camera_button.setStatusTip("Open Camera")
        open_camera_button.triggered.connect(self.open_camera)
        toolbar.addAction(open_camera_button)

        # Creating the "Take Picture" button
        take_picture_button = QAction(QIcon('take_picture.png'), "Take Picture", self)
        take_picture_button.setStatusTip("Take Picture")
        take_picture_button.triggered.connect(self.take_picture)
        toolbar.addAction(take_picture_button)

        # Creating the "Choose Folder" button
        choose_folder_button = QAction(QIcon('choose_folder.png'), "Choose Folder", self)
        choose_folder_button.setStatusTip("Choose Folder")
        choose_folder_button.triggered.connect(self.choose_folder)
        toolbar.addAction(choose_folder_button)

        # Creating the "Download" button
        download_button = QAction(QIcon('download.png'), "Download", self)
        download_button.setStatusTip("Download")
        download_button.triggered.connect(self.download_picture)
        toolbar.addAction(download_button)

        # Creating the preview image label
        self.preview_image = QLabel(self)
        self.preview_image.setAlignment(Qt.AlignCenter)
        self.preview_image.setText("No Image Preview")
        self.preview_image.setFixedSize(320, 240)

        # Creating a layout to hold the preview image and the toolbar
        layout = QHBoxLayout()
        layout.addWidget(self.preview_image)
        layout.addWidget(toolbar)

        # Creating a widget to hold the layout and setting it as the central widget
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def open_camera(self):
        # Code to open camera
        pass

    def take_picture(self):
        # Code to take picture and show preview image
        pass

    def choose_folder(self):
        # Code to choose folder for saving pictures
        pass

    def download_picture(self):
        # Code to download picture
        pass
