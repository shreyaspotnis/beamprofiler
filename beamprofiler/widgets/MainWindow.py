from PyQt4 import uic
from pyqtgraph.dockarea import DockArea, Dock
from PyQt4.QtGui import QScrollArea, QAction, QMainWindow
from PyQt4.QtCore import QSignalMapper, QString, SIGNAL, SLOT
import os


class MainWindow(QMainWindow):
    """Where all the action happens."""

    def __init__(self, settings):
        super(MainWindow, self).__init__()
        self.settings = settings
        # self.setupUi(self)

        # MainWindow is a collection of widgets in their respective docks.
        # We make DockArea our central widget
        self.dock_area = DockArea()
        self.setCentralWidget(self.dock_area)
        self.setWindowTitle('')

    def setWindowTitle(self, newTitle=''):
        """Prepend IP-BEC to all window titles."""
        title = 'Beam Profiler:'+newTitle
        super(MainWindow, self).setWindowTitle(title)
