from typing import Callable
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from base.interfaces import InterfacesBase
from gui.common.line_edit_group import LineEditGroup
from gui.common.line_edit import LineEdit

class InterfacesGUI( InterfacesBase ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._user_input : LineEditGroup
        self._user_output : LineEditGroup

    def get_name( self ):
        return self._modul_name

    def set_name( self, name ):
        self._modul_name = name

    def set_input( self, user_input : LineEditGroup ):
        self._user_input = user_input

    def set_output( self, user_output : LineEditGroup ):
        self._user_output = user_output

    def _add_getter( self, name, options : dict ):
        line_edit = LineEdit( name )
        line_edit.set_option( options )

        if options["func"] == float:
            validator = QDoubleValidator( line_edit )
            validator.setNotation( QDoubleValidator.StandardNotation )
            line_edit.setValidator( validator )
        elif options["func"] == int:
            line_edit.setValidator( QIntValidator( line_edit ) )

        self._user_input.add_line_edit( line_edit )

    def add_func( self, name, func : Callable[ [dict], None ], **options ):
        line = LineEdit(name)
        line.set_option( options )
        line.set_calculation( func )

        line.setValidator( QDoubleValidator( line ) )

        line.setReadOnly( True )

        self._user_output.add_line_edit( line )
