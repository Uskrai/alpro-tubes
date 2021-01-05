from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QHBoxLayout, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator
from .modul_group import ModulGroup
from .line_edit import LineEdit

class ModulWidget(  QGroupBox ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._button = {}

        # membuat layout
        self.layout = QVBoxLayout( self )
        self._button_layout = QHBoxLayout()

        # membuat widget rata di atas
        self.layout.setAlignment( Qt.AlignTop )

        # group buat modul
        self._modul_group = ModulGroup( self )

        # add button
        self.add_button( "Add", self._modul_group.add_widget )
        self.add_button( "Clear Value", self._modul_group.clear_value )
        self.add_button( "Remove", self._modul_group.pop_widget )
        self.add_button( "Clear Table", self._modul_group.clear_widget )

        # input pembulatan
        self._rounding = LineEdit( "Pembulatan", self )
        self._rounding.setPlaceholderText( "Pembulatan" )
        self._rounding.setValidator( QIntValidator() )
        self._rounding.textChanged.connect( self.set_rounding )
        self._button_layout.addWidget( self._rounding )

        self._modul = None

        # nambah item ke layout
        self.layout.addLayout( self._button_layout )
        self.layout.addWidget( self._modul_group )

    # ganti pembulatan
    def set_rounding( self ):
        rounding = self._rounding.text()
        if rounding == "":
            rounding = 10 ** 10
        self._modul_group.set_rounding( int( rounding ) )

    # nambah tombol
    def add_button( self, name, connect_func ):
        self._button[name] = QPushButton( name, self )
        self._button_layout.addWidget( self._button[name], 1 )
        self._button[name].clicked.connect( connect_func )

    # ngeset modul
    def set_modul( self, modul ):
        if self._modul == modul:
            return

        self._modul = modul
        self._modul_group.clear_widget()
        self._modul_group.set_modul( modul )
        self._modul_group.add_widget()
