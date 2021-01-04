from base.interfaces import InterfacesBase
from base.modul import Modul
class Gelombang( Modul ):
    name = "Gelombang"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("s")
        interfaces.get_float("n")
        interfaces.get_float("lamda")
        interfaces.get_float("f")
        interfaces.add_func("s / n", self.menentukan_panjang_gelombang)
        interfaces.add_func("lamda * f", self.menentukan_cepat_rambat_gelombang)
    def menentukan_panjang_gelombang( self, value : dict ):
        s = value["s"]
        n = value["n"]
        if n == 0:
            return 0
        return s/n
    def menentukan_cepat_rambat_gelombang(self, value : dict):
        lamda = value["lamda"]
        f = value["f"]
        return lamda*f
