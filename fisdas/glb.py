from base.interfaces import InterfacesBase
from base.modul import Modul
class GLB( Modul ):
    name = "GLB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("v", prefix="m/s" )
        interfaces.get_float("t", prefix="s")
        interfaces.add_func("s", self.hasil_glb, prefix="m" )
    def hasil_glb( self, value : dict ):
        v = value["v"]
        t = value["t"]
        return v*t




