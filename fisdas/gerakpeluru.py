from base.interfaces import InterfacesBase
from base.modul import Modul
import math
def kuadrat(val):
    return val ** 2
class GerakPeluru(Modul):
    name = "Gerak Peluru"
    def init_formula(self, interfaces: InterfacesBase):
        interfaces.get_float("V0",
                             brief="kecepatan ketika peluru ditembakkan",
                             deskripsi="Kecepatan awal benda (Vo) adalah \n\
                             kecepatan mula-mula yang dimiliki oleh benda saat \n\
                             pertama kali benda bergerak.",
                             posfix="m/s")
        interfaces.get_float("t",
                             brief="waktu",
                             deskripsi="waktu tempuh adalah waktu total yang dibutuhkan \n\
                             dalam perjalanan, sudah termasuk berhenti dan tundaan, dari satu \n\
                             tempat ke tempat lain yang melalui rute tertentu. Disini waktu yang dimaksud\n\
                             adalah waktu pada saat kecepatan akan ditentukan. ",
                             posfix= "s")
        interfaces.get_int("teta",
                           brief="sudut elevasi ketika peluru ditembakkan",
                           deskripsi="Sudut elevasi adalah sudut yang dibentuk oleh arah \n\
                                     horizontal dengan arah pandangan mata pengamat ke arah atas.",
                           posfix="o")
        interfaces.get_float("g",
                             brief="Percepatan gravitasi bumi",
                             deskripsi="Percepatan gravitasi suatu objek yang berada pada \n\
                             permukaan laut dikatakan ekuivalen dengan 1 g, yang didefinisikan \n\
                             memiliki nilai 9,80665 m/s²",
                             posfix="m/s²")
        interfaces.add_func("Vx", self.Vx)
        interfaces.add_func("Vy", self.Vy)
        interfaces.add_func("Vx^2", self.Vx2)
        interfaces.add_func("Vy^2", self.Vy2)
        interfaces.add_func("V", self.V)
        interfaces.add_func("X", self.x)
        interfaces.add_func("Y", self.y)

    def Vx(self, value: dict):
        V0 = value["V0"]
        teta = value["teta"]

        Vx = V0 * math.cos(teta)
        return Vx

    def Vy(self, value: dict):
        V0 = value["V0"]
        t  = value["t"]
        teta = value["teta"]
        g = value["Gravitasi"]

        Vy = V0 * math.sin(teta) - g * t
        return Vy

    def Vx2(self, value: dict):
        V0 = value["V0"]
        teta = value["teta"]

        Vx = V0 * math.cos(teta)
        Vx2 = kuadrat(Vx)
        return Vx2

    def Vy2(self, value: dict):
        V0 = value["V0"]
        t  = value["t"]
        teta = value["teta"]
        g = value["Gravitasi"]

        Vy = V0 * math.sin(teta) - g * t
        Vy2 = kuadrat(Vy)
        return Vy2

    def V(self, value: dict):
        V0 = value["V0"]
        t  = value["t"]
        teta = value["teta"]
        g = value["Gravitasi"]

        Vx = V0 * math.cos(teta)
        Vy = V0 * math.sin(teta) - g * t
        V = kuadrat(Vx + Vy)
        return V

    def x(self, value: dict):
        V0 = value["V0"]
        t = value["t"]
        teta = value["teta"]

        x = V0 * math.cos(teta) * t
        return x

    def y(self, value: dict):
        V0 = value["V0"]
        t = value["t"]
        teta = value["teta"]
        g = value["Gravitasi"]

        y = (V0 * math.sin(teta)) * t - 0.5 * g * kuadrat(t)
        return y






