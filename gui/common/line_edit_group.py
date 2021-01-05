from PyQt5.QtWidgets import QGroupBox
from PyQt5.QtCore import Qt, pyqtSignal
from gui.common.form_v_layout import FormVLayout
from gui.common.line_edit import LineEdit

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
            item.set_rounding( val )

    def add_line_edit( self, item : LineEdit ):
        item.textChanged.connect( self.text_change_event )
        if item.get_name() in self._line_edit:
            temp = self._line_edit[ item.get_name() ]
            if isinstance( temp, list ):
                self._line_edit[ item.get_name() ].append( temp )
            elif issubclass( LineEdit, type(temp) ):
                temp_list = [ temp, item ]
                self._line_edit[ item.get_name() ] = temp_list
        else:
            self._line_edit[ item.get_name() ] = item

        self.layout.addWidget( item.get_name(), item, self._row, self._col )

        self._row += 1

        if self._row == self._row_limit:
            self._row = 0
            self._col += 1

    def text_change_event( self ):
        value = {}
        for name, key in self._line_edit.items():
            if isinstance( key, LineEdit ):
                value[name] = self.parse_text( key.text() )
            elif isinstance( key, list ):
                value[name] = []
                for i in key:
                    value[name].append( self.parse_text( i.text() ) )

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
            if issubclass( LineEdit, type(key) ):
                key.calc_value( value )
            elif isinstance( key, list ):
                for item in key:
                    item.calc_value( value )

    def clear_value( self ):
        for key in self._line_edit.values():
            if issubclass( LineEdit, type(key) ):
                key.setText( "" )
            if isinstance( key, list ):
                for item in key:
                    item.setText( "" )

        self.text_change_event()
