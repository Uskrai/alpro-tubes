from PyQt5.QtWidgets import QGroupBox, QHBoxLayout
from base.modul import Modul
from .interfaces import InterfacesGUI
from .line_edit_group import LineEditGroup

class PerhitunganWidget( QGroupBox ):

    def __init__( self, parent=None, modul : Modul = None ):
        super().__init__( parent )
        self._modul : Modul
        self._modul = None

        self.layout = QHBoxLayout( self )
        self.setLayout( self.layout )

        self._interfaces = InterfacesGUI("")

        self._user_input = LineEditGroup( self )
        self._user_input.set_column_limit( 3 )
        self._user_input.changed.connect( self.text_change_event )

        self._user_output = LineEditGroup( self )
        self._user_output.set_column_limit( 2 )

        self._interfaces.set_input( self._user_input )
        self._interfaces.set_output( self._user_output )

        self.layout.addWidget( self._user_input, 3 )
        self.layout.addWidget( self._user_output, 1 )

        self.set_modul( modul )

    def set_modul( self, modul ):
        if self._modul is not modul:
            self._modul = modul
            self._interfaces.set_name( modul.name )

            modul.get_value( self._interfaces )

    def text_change_event( self, value ):
        self._user_output.calc_value( value )
