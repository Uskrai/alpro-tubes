from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from .modul_group import ModulGroup

class ModulWidget(  QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = QVBoxLayout( self )

        self._button_layout = QHBoxLayout()
        self.layout.addLayout( self._button_layout )

        self._add_button = QPushButton( "Add", self )
        self._clear_value_button = QPushButton( "Clear Value", self )
        self._remove_button = QPushButton( "Remove", self )
        self._clear_modul_button = QPushButton( "Clear Table", self )

        self._button_layout.addWidget( self._add_button )
        self._button_layout.addWidget( self._clear_value_button )
        self._button_layout.addWidget( self._remove_button )
        self._button_layout.addWidget( self._clear_modul_button )

        self.layout.setAlignment( Qt.AlignTop )

        self._modul_group = ModulGroup( self )
        self.layout.addWidget( self._modul_group )

        self._add_button.clicked.connect( self._modul_group.add_modul )
        self._remove_button.clicked.connect( self._modul_group.pop_modul )
        self._clear_modul_button.clicked.connect( self._modul_group.clear_modul )
        self._clear_value_button.clicked.connect( self._modul_group.clear_value )

        self._modul = None

    def set_modul( self, modul ):
        self._modul = modul
        self._modul_group.clear_modul()
        self._modul_group.set_modul( modul )
        self._modul_group.add_modul()
