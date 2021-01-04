import abc
from base.interfaces import InterfacesBase

class Modul( metaclass=abc.ABCMeta ):
    name = ""
    @abc.abstractclassmethod

    def init_formula( self, interfaces : InterfacesBase ):
        pass

    def show( self ):
        pass