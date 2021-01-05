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
        self._widget_list = []

        self._rounding = 10 ** 10

    # set modul
    def set_modul( self, modul ):
        self._modul = modul

    # nambah widget
    def add_widget( self ):
        if self._modul is not None:
            modul = self._modul()
            perhitungan_widget = PerhitunganWidget( self.group_modul, modul )
            perhitungan_widget.do_remove_widget.connect( self.remove_widget )
            perhitungan_widget.set_rounding( self._rounding )

            self.group_layout.addWidget( perhitungan_widget )
            self._widget_list.append( perhitungan_widget )

    # hapus widget yang ditunjuk obj
    def remove_widget( self, obj ):
        self.group_layout.removeWidget( obj )
        obj.hide()
        obj.destroy()

    def set_rounding( self, val ):
        self._rounding = val
        for item in self._widget_list:
            item.set_rounding( val )

    # hapus widget paling akhir
    def pop_widget( self ):
        if self._widget_list:
            perhitungan_widget = self._widget_list.pop()
            self.remove_widget( perhitungan_widget )

    # hapus semua widget
    def clear_widget( self ):
        # ulangi sampai _widget_list kosong
        while self._widget_list:
            self.pop_widget()

    # clear semua nilai
    def clear_value( self ):
        for item in self._widget_list:
            item.clear_value()
