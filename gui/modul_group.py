from PyQt5.QtWidgets import QScrollArea, QGroupBox, QVBoxLayout
from PyQt5.QtCore import Qt
from .perhitungan_widget import PerhitunganWidget

class ModulGroup( QScrollArea ):
    def __init__( self, parent=None ):
        super().__init__( parent )
        self.set_modul( None )
        self.setWidgetResizable( True )

        self.group_modul = QGroupBox( self )
        self.group_layout = QVBoxLayout( self.group_modul )
        self.group_layout.setAlignment( Qt.AlignTop )

        self.setWidget( self.group_modul )

        self._modul_list = []

    def set_modul( self, modul ):
        self._modul = modul

    def add_modul( self ):
        if self._modul is not None:
            modul = self._modul()
            modul_widget = PerhitunganWidget( self.group_modul, modul )

            self.group_layout.addWidget( modul_widget )
            self._modul_list.append( modul_widget )

    def pop_modul( self ):
        if self._modul_list:
            modul_widget = self._modul_list.pop()
            modul_widget.hide()
            modul_widget.destroy()
            self.group_layout.removeWidget( modul_widget )

    def clear_modul( self ):
        while self._modul_list:
            self.pop_modul()

    def clear_value( self ):
        pass
