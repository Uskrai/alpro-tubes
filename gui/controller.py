import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt
from base.controller import ControllerBase
from gui.main_window.main_widget import MainWidget

class ControllerGUI(  ControllerBase, ):
    def __init__( self ):
        super().__init__()
        self.app = QApplication( sys.argv )

        self._window = QMainWindow()
        self._window.setWindowTitle("Rumus fisdas")
        self._window.setWindowState( Qt.WindowMaximized )

        self._widgets = MainWidget( self._window )
        self._window.setCentralWidget( self._widgets )
        self._label = []
        self._label_tree = {}
        self._modul = {}

    def start(self, modul : dict ):
        self._modul = modul
        self._widgets.set_modul( modul )
        self._widgets.start()

        self._window.setCentralWidget( self._widgets )
        self._window.show()
        self.app.exec_()
