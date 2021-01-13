from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtCore
from base.modul import Modul

class ModulButton( QPushButton ):
    clicked = QtCore.pyqtSignal( object )

    def __init__( self, name, parent=None ):
        super().__init__( name, parent )
        self._name : str
        self._modul : Modul

    def set_modul( self,  modul ):
        if issubclass( modul, Modul ):
            self._modul = modul

    def get_modul( self ):
        return self._modul

    def hitButton( self, event ):
        self.clicked.emit( self._modul )
        return False
