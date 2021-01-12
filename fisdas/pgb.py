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
        interfaces.add_func("Periode", self.periode_getaran )
        interfaces.add_func("g",self.percepatan_gravitasi_bumi)

    def periode_getaran( self, value : dict ):
        t = value ["t"]
        n = value ["n"]
        
        if n == 0:
            return 0

        periode = n/t
        return periode

    def percepatan_gravitasi_bumi(self,value : dict):
        l = value ["l"]
        n = value ["n"]
        t = value ["t"]

        if value ["Periode"] == 0:
            return 0

        g = (4*(math.pi ** 2)*l) / (value ["Periode"]) ** 2
        return g