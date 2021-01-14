from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from gui.common.line_edit import LineEdit

class LineEditWidget( QWidget ):
    def __init__( self, parent = None, option : dict = None ):
        super().__init__( parent )
        self._option : dict

        self._label = QLabel( "", self )
        self._line_edit_prefix = QLabel( "", self )
        self._line_edit = LineEdit( "", self )
        self._line_edit_postfix = QLabel( "", self )

        self.layout = QVBoxLayout( self )
        self.layout.setAlignment( Qt.AlignHCenter )

        list_line_edit = [
            self._line_edit_prefix,
            self._line_edit,
            self._line_edit_postfix
        ]

        self._name = ""

        self._line_edit_layout = QHBoxLayout()
        self._line_edit_layout.setAlignment( Qt.AlignCenter )
        for i in list_line_edit:
            i.setSizePolicy( QSizePolicy.Minimum, QSizePolicy.Minimum )
            self._line_edit_layout.addWidget( i )

        self._line_edit.setSizePolicy( QSizePolicy.Expanding, QSizePolicy.Minimum )

        self.layout.addWidget( self._label )
        self.layout.addLayout ( self._line_edit_layout )

        self.set_option( option )

    def get_line_edit( self ):
        return self._line_edit

    def get_name( self ):
        return self._name

    def _check_empty( self, item ):
        if item.text() == "":
            item.hide()
        else:
            item.show()

    def set_option( self, option : dict ):

        self._option = option

        if option is not None:
            self._name = option["name"]

            label_text = option["name"]
            if option["brief"] != "":
                label_text += "  ("  + option["brief"] + ")"

            self._label.setText( label_text )
            self._line_edit.setReadOnly( option["read_only"] )
            self._line_edit_prefix.setText( option["prefix"] )
            self._line_edit_postfix.setText( option["postfix"] )

            validator = None
            if option["func"] == int:
                validator = QIntValidator()

            elif option["func"] == float:
                validator = QDoubleValidator()
                validator.setNotation( QDoubleValidator.StandardNotation )

            if validator is not None:
                self._line_edit.setValidator( validator )

            self._line_edit.set_option( option )

        self._check_empty( self._line_edit_prefix )
        self._check_empty( self._line_edit_postfix )
