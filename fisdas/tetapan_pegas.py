from base.interfaces import InterfacesBase
from base.modul import Modul
import math

def kuadrat(val):
    return val ** 2

class TetapanPegas(Modul):
    name = "Tetapan Pegas"

    def init_formula(self, interfaces: InterfacesBase):
        interfaces.get_float("m")
        interfaces.get_float("deltay")
        interfaces.get_float("T")

        interfaces.add_func("ks", self.konstanta_statis)
        interfaces.add_func("kd", self.konstanta_dinamis)

    def konstanta_statis(self, value: dict):
        m = value["m"]
        deltay = value["deltay"]
        g = 9.8

        ks = 0
        if deltay != 0:
            ks = (m * g) / deltay

        return ks

    def konstanta_dinamis(self, value: dict):
        m = value["m"]
        T = value["T"]
        kuadrat_T = kuadrat(T)

        kd = 0
        if kuadrat_T != 0:
            kd = (4 * math.pi * m) / kuadrat(T)
        return kd