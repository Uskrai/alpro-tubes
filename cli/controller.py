import modulfactory
from base.controller import ControllerBase
from base.modul import Modul
from .interfaces import InterfacesCLI

class ControllerCLI( ControllerBase ):
    def __init__( self ):
        super().__init__()
        self._interfaces = InterfacesCLI("")
        self._modul : Modul

    def show( self ):
        self._interfaces.show_result()

    def start(self, modul : dict ):
        inp = ""

        keys : list = []
        for key in modul.keys():
            keys.append( key )

        while inp != "0":
            i = 1

            for name in keys:
                print(f"{i}.{name}")
                i += 1
            print("0.Exit")
            
            inp = input("masukkan Pilihan:")
            if inp.isdigit():
                idx = int(inp) - 1
                if idx >= 0 and idx < len( keys ):
                    modul_name = keys[idx]

                    if issubclass( modul[modul_name], Modul ):
                        modul_type = modulfactory.ModulType.Modul
                    elif modul[modul_name] is dict:
                        modul_type = modulfactory.ModulType.Choice

                    if modul_type == modulfactory.ModulType.Modul:
                        self._modul = modulfactory.get_modul( keys[idx] )()
                        self.add_modul()
                        self.show()
                    elif modul_type == modulfactory.ModulType.Choice :
                        self.start( modul[ keys[idx] ] )
                            
    def add_modul( self ):
        interface = InterfacesCLI(self._modul.name)
        self._modul.init_formula( interface )
        self._interfaces = interface
