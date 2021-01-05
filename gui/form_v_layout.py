from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget, QLabel, QLayout

class FormVLayout( QVBoxLayout ):
    def __init__( self, parent=None ):
        super().__init__( parent )

        self.col = 0
        self.row = 0

        self.col_layout = []

    def prepare_layout( self, row ):
        if self.row <= row:
            self.col_layout.append( QHBoxLayout() )
            self.col_layout.append( QHBoxLayout() )
            super().addLayout( self.col_layout[ row * 2 ] )
            super().addLayout( self.col_layout[ row * 2 + 1] )
            self.row += 1

    def add_label( self, name, row, col ):
        label = QLabel( name )
        self.col_layout[ row * 2 ].insertWidget( col, label )


    def addWidget( self, name, widget : QWidget, row : int, col : int ):
        self.prepare_layout( row )
        self.add_label( name, row, col )

        self.col_layout[row * 2 + 1].insertWidget( col, widget )

    def addItem( self, name, item, row, col ):
        self.prepare_layout( row )
        self.add_label( name, row, col )

        self.col_layout[row * 2 + 1 ].insertItem( item, col )

    def addLayout( self, name, layout : QLayout, row, col ):
        self.prepare_layout( row )
        self.add_label( name, row, col )

        self.col_layout[ row * 2 + 1].insertLayout( layout, col )