import math
from base.interfaces import InterfacesBase
from base.modul import Modul
def kuadrat( val ):
    return val ** 2
class Vektor( Modul ):
    name = "Vektor"

    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("a",
                             brief="vektor a")
        interfaces.get_float("b",
                             brief="vektor b")
        interfaces.get_float("θ",
                             brief="Sudut diantara 2 vektor",
                             deskripsi=
"sudut yang terbentuk ketika 2 ujung garis vektor disatukan",
                             postfix="o")
        interfaces.add_func("a + b", self.penjumlahan_vektor )

    def penjumlahan_vektor( self, value : dict ):
        a = value["a"]
        b = value["b"]
        teta = value["θ"]

        res = kuadrat(a) + kuadrat(b) + ( 2 * a * b * math.cos(math.radians(teta)))
        res = math.sqrt(res)
        return res
