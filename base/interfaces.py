import abc
from typing import Callable

class InterfacesBase(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod

    def __init__( self, name ):
        pass
    
    def set_name( self, name ):
        pass

    def get_name( self ):
        pass

    def _add_getter( self, name, options : dict ):
        pass

    def get_int( self, name, **options ):
        options["func"] = int

        if not "error_warning" in options:
            options["error_warning"] = "hanya masukkan nilai angka"

        self._add_getter( name, options )
        
    def get_float( self, name, **options ):
        options["func"] = float

        if not "error_warning" in options:
            options["error_warning"] = "hanya masukkan nilai angka, pisahkan desimal dengan \".\" (Titik)"
        
        self._add_getter( name,options )


    def add_func( self, name, func : Callable[ [ dict ], None ], **options):
        pass

    def show_result( self ):
        pass