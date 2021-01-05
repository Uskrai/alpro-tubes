from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from .modul_group import ModulGroup

class ModulWidget(  QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = QVBoxLayout( self )

        self._button_layout = QHBoxLayout()
        self.layout.addLayout( self._button_layout )

        self.layout.setAlignment( Qt.AlignTop )

        self._modul_group = ModulGroup( self )
        self.layout.addWidget( self._modul_group )

        self._button = {}

        self.add_button( "Add", self._modul_group.add_modul )
        self.add_button( "Clear Value", self._modul_group.clear_value )
        self.add_button( "Remove", self._modul_group.pop_modul )
        self.add_button( "Clear Table", self._modul_group.clear_modul )

        self._modul = None

    def add_button( self, name, connect_func ):
        self._button[name] = QPushButton( name, self )
        self._button_layout.addWidget( self._button[name] )
        self._button[name].clicked.connect( connect_func )

    def set_modul( self, modul ):
        self._modul = modul
        self._modul_group.clear_modul()
        self._modul_group.set_modul( modul )
        self._modul_group.add_modul()
