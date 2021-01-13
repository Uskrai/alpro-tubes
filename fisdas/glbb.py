from base.interfaces import InterfacesBase
from base.modul import Modul
class GLBB( Modul ):
    name = "GLBB"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("V<sub>O</sub>",
                             brief="Kecepatan Awal",
                             deskripsi=
"Kecepatan awal benda (V<sup>O</sup>) adalah kecepatan \
mula-mula yang dimiliki oleh benda saat pertama kali\
benda bergerak.",
                             postfix="m/s")
        interfaces.get_float("a",
                             brief="percepatan",
                             deskripsi=
"percepatan atau akselerasi adalah perubahan\n\
kecepatan dalam satuan waktu tertentu.",
                             postfix="m/s<sup>2</sup>")

        interfaces.get_float("t",
                             brief="waktu tempuh",
                             deskripsi=
"waktu tempuh adalah waktu total yang dibutuhkan dalam\n\
perjalanan, sudah termasuk berhenti dan tundaan, dari\n\
satu tempat ke tempat lain yang melalui rute tertentu.",
                             postfix="s")

        interfaces.add_func("s", self.hasil_glbb,
                            brief="Jarak tempuh",
                            deskripsi=
"Jarak tempuh adalah panjang lintasan yang dilakui\n\
oleh suatu obyek yang bergerak,mulai dari posisi\n\
awal dan selesai pada posisi akhir.",
                            postfix="m")

    def hasil_glbb ( self, value : dict ):
        Vo = value["V<sub>O</sub>"]
        a = value["a"]
        t = value["t"]
        return (Vo*t)+(0.5*a*(t*t))
