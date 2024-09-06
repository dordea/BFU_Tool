import requests
import cv2
from PIL import Image
from io import BytesIO
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QImage
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QByteArray, QBuffer, QIODevice
import sys
from PyQt6 import QtCore, QtGui, QtWidgets

def generate_fake_person_image():
    url = "https://thispersondoesnotexist.com"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Deschidem imaginea folosind PIL
        image = Image.open(BytesIO(response.content))
        
        # Convertim imaginea PIL într-un QImage
        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.OpenModeFlag.WriteOnly)
        image.save(buffer, "JPEG")
        buffer.close()

        qimage = QImage()
        qimage.loadFromData(byte_array, "JPEG")
        
        # Convertim QImage la QPixmap
        pixmap = QPixmap.fromImage(qimage)
    
        return pixmap
    else:
        return None