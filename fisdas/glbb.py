from base.interfaces import InterfacesBase
from base.modul import Modul
class GLBB( Modul ):
    name = "GLBB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("Vo",
                             brief="Kecepatan Awal",
                             deskripsi="Kecepatan awal benda (Vo) adalah kecepatan mula-mula yang\n\
dimiliki oleh benda saat pertama kali benda bergerak. ",
                             posfix="m/s")
        interfaces.get_float("a",
                             brief="percepatan",
                             deskripsi="percepatan atau akselerasi adalah perubahan kecepatan dalam\n\
satuan waktu tertentu. ",
                             posfix="m/s<sup>2</sup>")
        interfaces.get_float("t",
                             brief="waktu tempuh",
                             deskripsi="waktu tempuh adalah waktu total yang dibutuhkan dalam\n\
perjalanan, sudah termasuk berhenti dan tundaan, dari satu tempat \n\
ke tempat lain yang melalui rute tertentu.",
                             posfix="s")
        interfaces.add_func("s", self.hasil_glbb,
                            brief="Jarak tempuh",
                            dekripsi="Jarak tempuh adalah panjang lintasan yang dilakui\n\
oleh suatu obyek yang bergerak, mulai dari posisi awal dan selesai pada posisi akhir.",
                            posfix="m")

    def hasil_glbb ( self, value : dict ):
        Vo = value["Vo"]
        a = value["a"]
        t = value["t"]
        return (Vo*t)+(0.5*a*(t*t))
