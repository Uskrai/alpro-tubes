from base.interfaces import InterfacesBase
from base.modul import Modul
class GLB( Modul ):
    name = "GLB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("v",
                             brief="Kecepatan",
                             deskripsi="kecepatan merupakan cepat lambatnya perubahan posisi \n\
(perpindahan) suatu benda terhadap waktu tempuh, dan merupakan \n\
besaran vektor (memiliki nilai dan arah).",
                             posfix="m/s" )
        interfaces.get_float("t",
                             brief="waktu tempuh",
                             deskripsi="waktu tempuh adalah waktu total yang dibutuhkan dalam\n\
perjalanan, sudah termasuk berhenti dan tundaan, dari satu tempat \n\
ke tempat lain yang melalui rute tertentu.",
                             posfix="s")
        interfaces.add_func("s", self.hasil_glb, prefix="m" )

    def hasil_glb( self, value : dict ):
        v = value["v"]
        t = value["t"]
        return v*t




