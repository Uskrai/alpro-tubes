from PyQt5.QtWidgets import QGridLayout, QWidget, QLabel, QLayout

class FormVLayout( QGridLayout ):

    def addWidget( self, name, widget : QWidget, row : int, col : int ):
        label = QLabel( name )

        super().addWidget( label, row * 2, col )
        super().addWidget( widget, row * 2 + 1, col )

    def addItem( self, name, item, row, col ):
        label = QLabel( name )

        super().addWidget( label, row * 2, col )
        super().addItem( item, row * 2 + 1, col )

    def addLayout( self, name, layout : QLayout, row, col ):
        label = QLabel( name )

        super().addWidget( label, row * 2, col )
        super().addLayout( layout, row * 2 + 1, col )
