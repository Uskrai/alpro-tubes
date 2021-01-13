from base.interfaces import InterfacesBase
from base.modul import Modul
import math

class MenaraAir(Modul):
    name = "Menara Air"
    def init_formula(self, interfaces: InterfacesBase):
        interfaces.get_float("h1",
                             brief="Tinggi air diatas lubang",
                             deskripsi="Tinggi air didalam tangki terhitung dari atas lubang tangki",
                             posfix="m")
        interfaces.get_float("g",
                             brief="Percepatan gravitasi bumi",
                             deskripsi="Percepatan gravitasi suatu objek yang berada pada \n\
                             permukaan laut dikatakan ekuivalen dengan 1 g, yang didefinisikan \n\
                             memiliki nilai 9,80665 m/s²",
                             posfix="m/s²")
        interfaces.get_float("h2",
                             brief="Tinggi menara air",
                             deskripsi="Tinggi menara air yang terhitung dari tanah hingga bagian bawah tangki",
                             posfix="m")
        interfaces.add_func("v", self.menentukan_kecepatan,
                            brief="Kecepatan air yang mengalir",
                            posfix="m/s")
        interfaces.add_func("x", self.jarak,
                            brief="Jarak air yang keluar",
                            posfix="m/s")

    def menentukan_kecepatan( self, value : dict):
        h1 = value["h1"]
        g = value["g"]
        return math.sqrt(2*g*h1)

    def jarak(self, value: dict):
        h1 = value["h1"]
        h2 = value["h2"]
        return 2*math.sqrt(h1*h2)