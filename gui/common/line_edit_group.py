from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtCore import Qt, pyqtSignal
from gui.common.form_v_layout import FormVLayout
from gui.common.line_edit_widget import LineEditWidget

class LineEditGroup( QGroupBox ):
    changed = pyqtSignal( dict )

    def __init__( self, parent=None ):
        super().__init__( parent )
        self.layout = FormVLayout( self )
        self.layout.setAlignment( Qt.AlignTop)

        self._line_edit = {}

        self._row = 0
        self._col = 0

        self._row_limit = -1
        self._column_limit = -1

    def set_cell_limit( self, row, col ):
        self.set_column_limit( col )
        self.set_row_limit( row )

    def set_column_limit( self, col ):
        self._column_limit = col

    def set_row_limit( self, row ):
        self._row_limit = row

    def set_rounding( self, val ):
        for item in self._line_edit.values():
            item.get_line_edit().set_rounding( val )

    def add_line_edit( self, item : LineEditWidget ):
        item.get_line_edit().textChanged.connect( self.text_change_event )
        self._line_edit[ item.get_name() ] = item
        self.layout.addWidget( item.get_name(), item, self._row, self._col )

        self._row += 1

        if self._row == self._row_limit:
            self._row = 0
            self._col += 1

    def text_change_event( self ):
        value = {}
        for name, key in self._line_edit.items():
            value[name] = self.parse_text( key.get_line_edit().text() )

        self.changed.emit( value )


    def parse_text( self, text : str ):
        if text == "":
            return 0

        text = text.replace( ",", "" )

        if "." in text:
            return float( text )

        return int( text )

    def calc_value( self, value ):
        for key in self._line_edit.values():
            value[key.get_name()] = key.get_line_edit().calc_value( value )

    def clear_value( self ):
        for key in self._line_edit.values():
            key.get_line_edit().setText( "" )

        self.text_change_event()
