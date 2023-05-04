from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtMultimedia import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QLabel
import sys
from datetime import datetime
class CameraUI(QDialog):
    def __init__(self):
        super().__init__()

        # inisialisasi kamera, viewfinder, dan image capture
        self.camera = QCamera()
        self.viewfinder = QCameraViewfinder()
        self.capture_button = QPushButton('Capture')
        self.capture_button.clicked.connect(self.capture_image)
        self.image_capture = QCameraImageCapture(self.camera)

        # atur tata letak UI
        layout = QVBoxLayout()
        layout.addWidget(self.viewfinder)
        layout.addWidget(self.capture_button)
        self.setLayout(layout)
        
    def start_camera(self):
        self.camera.setViewfinder(self.viewfinder)
        self.camera.start()

    def stop_camera(self):
        self.camera.stop()

    def capture_image(self):
        timestamp = QDateTime.currentDateTime().toString('yyMMdd-hhmmss')
        self.image_capture.capture(f'{timestamp}.jpg')

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Escape:
            self.close()
            
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = CameraUI()
    ui.show()
    ui.start_camera()
    sys.exit(app.exec_())
