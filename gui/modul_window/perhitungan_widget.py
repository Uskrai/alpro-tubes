from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import pyqtSignal
from base.modul import Modul
from gui.interfaces import InterfacesGUI
from gui.common.line_edit_group import LineEditGroup

class PerhitunganWidget( QGroupBox ):
    do_remove_widget = pyqtSignal( object )

    def __init__( self, parent=None, modul : Modul = None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None
        self.button = {}

        self.layout = QHBoxLayout( self )
        self.setLayout( self.layout )

        self._interfaces = InterfacesGUI("")

        self._user_input = LineEditGroup( self )
        self._user_input.set_row_limit( 2 )
        self._user_input.changed.connect( self.text_change_event )
        self._user_input.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Preferred )

        self._user_output = LineEditGroup( self )
        self._user_output.set_row_limit( 2 )
        self._user_output.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Preferred )

        self._interfaces.set_input( self._user_input )
        self._interfaces.set_output( self._user_output )

        self._button_layout = QVBoxLayout()

        self.add_button( "Clear", self.clear_value )
        self.add_button( "Remove", self.remove_widget )

        self.layout.addWidget( self._user_input )
        self.layout.addWidget( self._user_output )
        self.layout.addLayout( self._button_layout )

        self.set_modul( modul )

    def set_rounding( self, val ):
        self._user_output.set_rounding( val )
        self._user_input.text_change_event()

    def add_button( self, name, connect_func ):
        self.button[name] = QPushButton( name )
        self._button_layout.addWidget( self.button[name] )
        self.button[name].setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Minimum )
        self.button[name].adjustSize()
        self.button[name].clicked.connect( connect_func )

    def set_modul( self, modul ):
        if self._modul is not modul:
            self._modul = modul
            self._interfaces.set_name( modul.name )

            modul.init_formula( self._interfaces )

    def text_change_event( self, value ):
        self._user_output.calc_value( value )

    def clear_value( self ):
        self._user_input.clear_value()

    def remove_widget( self ):
        self.do_remove_widget.emit( self )
