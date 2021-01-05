from PyQt5.QtWidgets import QGroupBox, QVBoxLayout
from PyQt5.QtCore import pyqtSignal, Qt
from .modul_button import ModulButton

class ButtonWidget( QGroupBox ):
    clicked = pyqtSignal( object )
    def __init__( self, content : set ):
        super().__init__( content )

        self.layout = QVBoxLayout()
        self.layout.setAlignment( Qt.AlignTop )
        self.setLayout( self.layout )

        self._modul = {}
        self._button = []

    def set_modul( self, list_modul ):
        self._modul = list_modul
        self._button.clear()

        for name, value in list_modul.items():
            button = ModulButton( name, self )
            button.set_modul( value )
            button.clicked.connect(  self.onButtonClicked )
            self.layout.addWidget( button )
            self._button.append( button )

    def onButtonClicked( self, modul ):
        self.clicked.emit( modul )
