"""Add all camera image acquisition code here."""

import numpy as np


class Camera(object):
    """Base class for all camera objects."""
    def __init__(self):
        super(Camera, self).__init__()

    def getImage(self):
        x = np.arange(256.)
        y = np.arange(256.)
        x, y = np.meshgrid(x, y)
        return np.exp(-((x-128.)**2 + (y-128.)**2)/50.**2)
