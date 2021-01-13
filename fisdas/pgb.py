from base.interfaces import InterfacesBase
from base.modul import Modul
import math

class PGB( Modul ):
    name = "Percepatan Gravitasi Bumi"

    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("l",
                             brief="panjang tali yang digunakan",
                             deskripsi="Panjang adalah dimensi suatu benda yang \n\
menyatakan jarak antar ujung. Panjang tali diukur menggunakan penggaris",
                             posfix="m")
        interfaces.get_float("T",
                             brief="Periode getaran bandul",
                             deskripsi="Periode merupakan waktu yang diperlukan suatu \n\
benda untuk melakukan satu getaran/putaran penuh",
                             posfix="s")
        interfaces.get_float("phi",
                             brief="masukkan bilangan desimal",
                             deskripsi="phi adalah sebuah konstanata dalam matematika\n\
yang merupakan perbandingan keliling lingkaran dengan diameter")
        interfaces.add_func("g",self.percepatan_gravitasi_bumi)

    def percepatan_gravitasi_bumi(self,value : dict):
        l = value ["l"]
        T = value ["T"]
        phi = value["phi"]
        if T == 0:
            return 0

        g = 4*(math.pow(phi, 2))*l / math.pow(T, 2)
        return g