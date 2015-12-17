from PyQt4 import uic
from pyqtgraph.dockarea import DockArea, Dock
from PyQt4.QtGui import QScrollArea, QAction, QMainWindow
from PyQt4.QtCore import QSignalMapper, QString, SIGNAL, SLOT
import os

from ipbec.widgets import ImageView, ImageBrowser, Fitter, RoiEditor, Plot1d
from beamprofiler import cameras


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

        self.camera = cameras.Camera()

        self.createDocks()

    def setWindowTitle(self, newTitle=''):
        """Prepend IP-BEC to all window titles."""
        title = 'Beam Profiler:'+newTitle
        super(MainWindow, self).setWindowTitle(title)

    def createDocks(self):
        """Create all dock widgets and add them to DockArea."""
        self.image_view = ImageView(self.settings, self)
        self.image_view.setImage(self.camera.getImage())

        self.roi_editor_h = RoiEditor(self.settings,
                                      self.image_view, self, name='ROIH',
                                      pen=(1, 9), axis=1)
        self.roi_editor_v = RoiEditor(self.settings,
                                      self.image_view, self, name='ROIV',
                                      pen=(1, 1), axis=0)
        self.roi_editor_int = RoiEditor(self.settings,
                                        self.image_view, self, name='ROI Int',
                                        pen=(1, 2), axis=1)
        self.roi_plot_h = Plot1d(parent=self, title='ROI H')
        self.roi_plot_v = Plot1d(parent=self, title='ROI V')

        # self.analyzer = Analyzer(self.settings, parent=self)

        # Create docks for all widgets
        self.dock_image_view = Dock('Image View', widget=self.image_view)
        # self.dock_image_browser = Dock('Image Browser',
        #                                widget=self.image_browser)
        # self.dock_fitter = Dock('Fitter', widget=self.fitter)
        self.dock_roi_h = Dock('ROIH', widget=self.roi_editor_h)
        self.dock_roi_v = Dock('ROIV', widget=self.roi_editor_v)
        self.dock_roi_int = Dock('ROI Int', widget=self.roi_editor_int)

        self.dock_roi_plot_h = Dock('ROIH Plot', widget=self.roi_plot_h)
        self.dock_roi_plot_v = Dock('ROIV Plot', widget=self.roi_plot_v)
        # self.dock_analyzer = Dock('Analyze', widget=self.analyzer)

        self.dock_area.addDock(self.dock_image_view, position='top')
        self.dock_area.addDock(self.dock_roi_h, position='bottom',
                               relativeTo=self.dock_image_view)
        self.dock_area.addDock(self.dock_roi_v, position='below',
                               relativeTo=self.dock_roi_h)
        self.dock_area.addDock(self.dock_roi_int, position='below',
                               relativeTo=self.dock_roi_v)
        self.dock_area.addDock(self.dock_roi_plot_h, position='below',
                               relativeTo=self.dock_image_view)
        self.dock_area.addDock(self.dock_roi_plot_v, position='right',
                               relativeTo=self.dock_roi_plot_h)
        # self.dock_area.addDock(self.dock_analyzer, position='top',
        #                        relativeTo=self.dock_image_browser)
