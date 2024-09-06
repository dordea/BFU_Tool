import cv2
from rembg import remove
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt6.QtGui import QPixmap, QImage
import sys
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtCore import QByteArray, QBuffer, QIODevice
from PyQt6 import QtCore, QtGui, QtWidgets

def cv2_to_pixmap_alternative(cv_img):
    # Încercăm să codificăm imaginea în format PNG (poate fi și JPG, dar PNG păstrează transparența)
    success, encoded_image = cv2.imencode('.png', cv_img)
    if not success:
        return None
    
    # Convertim imaginea codificată într-un QByteArray
    data = QByteArray(encoded_image.tobytes())
    
    # Folosim QBuffer pentru a crea un QPixmap din QByteArray
    buffer = QBuffer(data)
    buffer.open(QIODevice.OpenModeFlag.ReadOnly)
    pixmap = QPixmap()
    pixmap.loadFromData(buffer.data())
    
    return pixmap
def remove_background(image_path):
    # Load the image
    image = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)
    
    # Remove the background
    output = remove(image)
    #cv2.imwrite("output.png", output)
    
    # Convert the output to a QPixmap
    pixmap = cv2_to_pixmap_alternative(output)
    

    return pixmap

