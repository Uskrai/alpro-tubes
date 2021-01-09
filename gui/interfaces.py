from typing import Callable
from PyQt5.QtWidgets import QBoxLayout
from base.interfaces import InterfacesBase
from gui.common.line_edit_widget import LineEditWidget

class InterfacesGUI( InterfacesBase ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self._user_input : QBoxLayout
        self._user_output : QBoxLayout

    def get_name( self ):
        return self._modul_name

    def set_name( self, name ):
        self._modul_name = name

    def set_input( self, input_layout : QBoxLayout ):
        self._user_input = input_layout

    def set_output( self, output_layout : QBoxLayout ):
        self._user_output = output_layout

    def prepare_option( self, name, option ):
        option["name"] = name
        option.setdefault("read_only", False )

        option.setdefault("func",None)
        option.setdefault("prefix", "" )
        option.setdefault("postfix", "" )
        option.setdefault("deskripsi","")
        option.setdefault("brief","")

    def _add_getter( self, name, options : dict ):
        self.prepare_option( name, options )

        line_edit = LineEditWidget( None, options )
        line_edit.set_option( options )

        self._user_input.add_line_edit( line_edit )

    def add_func( self, name, func : Callable[ [dict], None ], **options ):
        self.prepare_option( name, options )
        options["read_only"] = True

        line = LineEditWidget( None, options )
        line.get_line_edit().set_calculation( func )
        self._user_output.add_line_edit( line )
