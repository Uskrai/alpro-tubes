from base.interfaces import InterfacesBase
from base.modul import Modul
import math

class MenaraAir(Modul):
    name = "Menara Air"
    def init_formula(self, interfaces: InterfacesBase):
        interfaces.get_float("h<sub>1</sub>",
                             brief="Tinggi air diatas lubang",
                             deskripsi=
"Tinggi air didalam tangki terhitung\n\
dari atas lubang tangki",
                             postfix="m")

        interfaces.get_float("g",
                             brief="Percepatan gravitasi bumi",
                             deskripsi=
"Percepatan gravitasi suatu objek yang berada pada permukaan\n\
laut dikatakan ekuivalen dengan 1 g, yang didefinisikan\n\
memiliki nilai 9,80665 m/s²",
                             postfix="m/s²")

        interfaces.get_float("h<sub>2</sub>",
                             brief="Tinggi menara air",
                             deskripsi=
"Tinggi menara air yang terhitung dari\n\
tanah hingga bagian bawah tangki",
                             postfix="m")

        interfaces.add_func("v", self.menentukan_kecepatan,
                            brief="Kecepatan air yang mengalir",
                            postfix="m/s")

        interfaces.add_func("x", self.jarak,
                            brief="Jarak air yang keluar",
                            postfix="m/s")

    def menentukan_kecepatan( self, value : dict):
        h1 = value["h<sub>1</sub>"]
        g = value["g"]
        return math.sqrt(2*g*h1)

    def jarak(self, value: dict):
        h1 = value["h<sub>1</sub>"]
        h2 = value["h<sub>2</sub>"]
        return 2*math.sqrt(h1*h2)
