"""Add all camera image acquisition code here."""
# from PyQt4.QtGui import QObject
from PyQt4.QtCore import QSignalMapper, QString, SIGNAL, SLOT, QObject
from PyQt4.QtCore import pyqtSignal, QTimer

import numpy as np
import cv2


class Camera(QObject):
    """Base class for all camera objects."""

    imageAcquired = pyqtSignal(object)

    def __init__(self, parent=None):
        super(Camera, self).__init__(parent)


class SimulatedCamera(Camera):

    def __init__(self, parent=None):
        super(SimulatedCamera, self).__init__(parent)
        timer = QTimer(self)
        timer.setInterval(500)
        timer.start()
        timer.timeout.connect(self.getImage)
        # timer.stop()

    def getImage(self):
        x = np.arange(256.)
        y = np.arange(256.)
        x, y = np.meshgrid(x, y)
        wx = np.random.randn()*10 + 30
        wy = np.random.randn()*10 + 30
        cx = np.random.randn()*10 + 128
        cy = np.random.randn()*10 + 128
        dat = np.exp(-(((x-cx)/wx)**2 + ((y-cy)/wy)**2))
        dat += np.random.randn(256., 256.)*0.1
        self.imageAcquired.emit(dat)


class WebCam(Camera):

    def __init__(self, parent=None):
        super(WebCam, self).__init__(parent)
        self.cap_device = cv2.VideoCapture(0)
        timer = QTimer(self)
        timer.setInterval(100)
        timer.start()
        timer.timeout.connect(self.getImage)
        # timer.stop()

    def getImage(self):
        x = np.arange(256.)
        y = np.arange(256.)
        x, y = np.meshgrid(x, y)
        wx = np.random.randn()*10 + 30
        wy = np.random.randn()*10 + 30
        cx = np.random.randn()*10 + 128
        cy = np.random.randn()*10 + 128
        dat = np.exp(-(((x-cx)/wx)**2 + ((y-cy)/wy)**2))
        dat += np.random.randn(256., 256.)*0.1
        ret, frame = self.cap_device.read()
        print('done')
        if ret is True:
            self.imageAcquired.emit(frame[:, :, 0].T)


