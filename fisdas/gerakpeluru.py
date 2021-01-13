from base.interfaces import InterfacesBase
from base.modul import Modul
import math
def kuadrat(val):
    return val ** 2
class GerakPeluru(Modul):
    name = "Gerak Peluru"
    def init_formula(self, interfaces: InterfacesBase):
        interfaces.get_float("V<sub>0</sub>",
                             brief="kecepatan ketika peluru ditembakkan",
                             deskripsi="Kecepatan awal benda (Vo) adalah \n\
kecepatan mula-mula yang dimiliki oleh benda saat \n\
pertama kali benda bergerak.",
                             postfix="m/s")
        interfaces.get_float("t",
                             brief="waktu",
                             deskripsi="waktu tempuh adalah waktu total yang dibutuhkan \n\
dalam perjalanan, sudah termasuk berhenti dan tundaan, dari satu \n\
tempat ke tempat lain yang melalui rute tertentu. Disini waktu yang dimaksud\n\
adalah waktu pada saat kecepatan akan ditentukan. ",
                             postfix= "s")
        interfaces.get_int("θ",
                           brief="sudut elevasi ketika peluru ditembakkan",
                           deskripsi="Sudut elevasi adalah sudut yang dibentuk oleh arah \n\
horizontal dengan arah pandangan mata pengamat ke arah atas.",
                           postfix="o")
        interfaces.get_float("g",
                             brief="Percepatan gravitasi bumi",
                             deskripsi="Percepatan gravitasi suatu objek yang berada pada \n\
permukaan laut dikatakan ekuivalen dengan 1 g, yang didefinisikan \n\
memiliki nilai 9,80665 m/s²",
                             postfix="m/s²")
        interfaces.get_float("Vx",
                             brief="Mencari kuadrat Vx",
                             deskripsi="Masukkan kembali nilai Vx")
        interfaces.get_float("Vy",
                             brief="Mencari kuadrat Vy",
                             deskripsi="Masukkan kembali nilai Vy")
        interfaces.add_func("Vx", self.Vx, postfix="m/s")
        interfaces.add_func("Vy", self.Vy, postfix="m/s")
        interfaces.add_func("Vx<sup>2</sup>", self.Vx2)
        interfaces.add_func("Vy<sup>2</sup>", self.Vy2)
        interfaces.add_func("V", self.V, postfix="m")
        interfaces.add_func("X", self.x, postfix="m")
        interfaces.add_func("Y", self.y, postfix="m")

    def Vx(self, value: dict):
        V0 = value["V<sub>0</sub>"]
        teta = value["θ"]

        Vx = V0 * math.cos(math.radians(teta))
        return Vx

    def Vy(self, value: dict):
        V0 = value["V<sub>0</sub>"]
        t  = value["t"]
        teta = value["θ"]
        g = value["g"]

        Vy = V0 * math.sin(math.radians(teta)) - g * t
        return Vy

    def Vx2(self, value: dict):
        Vx = value["Vx"]
        Vx2 = math.pow(Vx, 2)
        return Vx2

    def Vy2(self, value: dict):
        Vy = value["Vy"]
        Vy2 = math.pow(Vy, 2)
        return Vy2

    def V(self, value: dict):
        Vx = value ["Vx"]
        Vy = value["Vy"]
        V = kuadrat(Vx + Vy)
        return V

    def x(self, value: dict):
        V0 = value["V<sub>0</sub>"]
        t = value["t"]
        teta = value["θ"]

        x = V0 * math.cos(math.radians(teta)) * t
        return x

    def y(self, value: dict):
        V0 = value["V<sub>0</sub>"]
        t = value["t"]
        teta = value["θ"]
        g = value["g"]

        y = (V0 * math.sin(math.radians(teta))) * (t - 0.5 * g * math.pow(t, 2))
        return y






