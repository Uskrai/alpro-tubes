from base.interfaces import InterfacesBase
from base.modul import Modul
class GLBB( Modul ):
    name = "GLBB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("Vo", prefix="m/s")
        interfaces.get_float("a", prefix="m/s<sup>2</sup>")
        interfaces.get_float("t", prefix="s")
        interfaces.add_func("s", self.hasil_glbb )
    def hasil_glbb ( self, value : dict ):
        Vo = value["Vo"]
        a = value["a"]
        t = value["t"]
        return (Vo*t)+(0.5*a*(t*t))
