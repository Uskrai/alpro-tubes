from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLayout

class FormVLayout( QVBoxLayout ):
    def __init__( self, parent=None ):
        super().__init__( parent )

        self.col = 0
        self.row = 0

        self.col_layout = []

    def prepare_layout( self, row ):
        if self.row <= row:
            self.col_layout.append( QHBoxLayout() )
            super().addLayout( self.col_layout[ row] )
            self.row += 1

    def addWidget( self, name, widget : QWidget, row : int, col : int ):
        self.prepare_layout( row )
        self.col_layout[row].insertWidget( col, widget )

    def addItem( self, name, item, row, col ):
        self.prepare_layout( row )
        self.col_layout[row].insertItem( item, col )

    def addLayout( self, name, layout : QLayout, row, col ):
        self.prepare_layout( row )
        self.col_layout[ row].insertLayout( layout, col )
