from PyQt5.QtWidgets import QLineEdit, QToolTip

class LineEdit( QLineEdit ):
    def __init__( self, name, parent=None ):
        super().__init__( "" , parent )
        self._name = name
        self._option = {}
        self._calc = lambda value : 0
        self.round = 10 ** 10

        self._tool_tip = QToolTip

    def get_name( self ):
        return self._name

    def set_option( self, option : dict ):
        self._option = option
        self.setWhatsThis( option["deskripsi"] )

    def set_calculation( self, func ):
        self._calc = func

    def set_rounding( self, val ):
        self.round = val

    def calc_value( self, value ):
        result = self._calc( value )
        self.setText( str( round( result, self.round ) ) )
        return result

    def focusInEvent( self, event ):
        self._tool_tip.hideText()

    def enterEvent( self, event ):
        pos = event.globalPos()
        self._tool_tip.showText( pos, self.whatsThis(), self )

    def leaveEvent( self, event ):
        self._tool_tip.hideText()
