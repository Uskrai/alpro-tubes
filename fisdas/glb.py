from base.interfaces import InterfacesBase
from base.modul import Modul
class GLB( Modul ):
    name = "GLB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("v",
                             brief="Kecepatan",
                             deskripsi=
"kecepatan merupakan cepat lambatnya perubahan posisi \n\
(perpindahan) suatu benda terhadap waktu tempuh, dan merupakan \n\
besaran vektor (memiliki nilai dan arah).",
                             postfix="m/s" )

        interfaces.get_float("t",
                             brief="waktu tempuh",
                             deskripsi=
"waktu tempuh adalah waktu totalyang dibutuhkan dalam\n\
perjalanan, sudah termasuk berhenti dan tundaan, dari\n\
satu tempat ke tempat lain yang melalui rute tertentu.",
                             postfix="s")

        interfaces.add_func("s",
                            self.hasil_glb,
                            brief="Jarak tempuh",
                            deskripsi=
"Jarak tempuh adalah panjang lintasan yang dilakui oleh\n\
suatu obyek yang bergerak, mulai dari posisi awal dan\n\
dan selesai pada posisi akhir.",
                            postfix="m" )

    def hasil_glb( self, value : dict ):
        v = value["v"]
        t = value["t"]
        return v*t




