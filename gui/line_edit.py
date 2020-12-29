from PyQt5.QtWidgets import QLineEdit

class LineEdit( QLineEdit ):
    def __init__( self, name, parent=None ):
        super().__init__( "" , parent )
        self._name = name
        self._option = {}
        self._calc = lambda value : 0

    def get_name( self ):
        return self._name

    def set_option( self, option : dict ):
        self._option = option

    def set_calculation( self, func ):
        self._calc = func

    def calc_value( self, value ):
        self.setText( str( self._calc( value ) ) )
