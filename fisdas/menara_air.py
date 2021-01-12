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
        interfaces.get_float("h2",
                             brief="Tinggi menara air",
                             deskripsi="Tinggi menara air yang terhitung dari tanah hingga bagian bawah tangki",
                             posfix"m")
        interfaces.add_func("v", self.kecepatan)
        interfaces.add_func("x", self.jarak)

    def kecepatan(self, value: dict):
        h1 = value["h1"]
        g  = 9.8

        return str(math.sqrt(2*g*h1))

    def jarak(self, value: dict):
        h1 = value["h1"]
        h2 = value["h2"]

        return str(2*math.sqrt(h1*h2))