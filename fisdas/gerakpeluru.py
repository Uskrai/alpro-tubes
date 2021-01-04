from base.interfaces import InterfacesBase
from base.modul import Modul
import math


def kuadrat(val):
    return val ** 2





# kalo mau buat kelas(Modul) baru
# ini filenya dicopy terus ganti nama
# "Vektor"nya diganti
# "Moduil"nya jangan
# kalo udah jadi, masukkin ke file modulfactory.py
class GerakPeluru(Modul):
    # ini nama praktikumnya
    name = "Gerak Peluru"

    # ini tempat ngambil nilai
    def init_formula(self, interfaces: InterfacesBase):
        # kalo mau minta bilangan bulat pake get_int
        # kalo minta bilangan desimal pake get_float
        # parameter pertama itu buat namain variablenya pas nanti dioper
        # kalo make parameter yang sama, nanti ke overwrite jadi hati hati
        interfaces.get_float("V0")
        interfaces.get_float("t")
        interfaces.get_int("teta")
        interfaces.get_float("Gravitasi")

        # ini buat nambahin fungsi buat ngitung rumusnya,
        # parameter pertama itu hasil dari apa,
        # parameter kedua itu fungsinya
        # ini bisa dipanggil berkali-kali
        interfaces.add_func("Vx", self.Vx)
        interfaces.add_func("Vy", self.Vy)
        interfaces.add_func("Vx^2", self.Vx2)
        interfaces.add_func("Vy^2", self.Vy2)
        interfaces.add_func("V", self.V)
        interfaces.add_func("X", self.x)
        interfaces.add_func("Y", self.y)

    # ini fungsi buat ngitung rumusnya
    # parameter kedua itu buat nilai yang diambil dari method
    # get_value diatas
    # isi key( [key] ) itu sama kayak yang parameter diatas
    # kalo diatas interfaces.get_float("a")
    # ngambilnya value["a"]

    # kalo mau ngambil nama yang dimasukkin
    # di add_func parameter pertama
    # bisa ngambil lewat value["_name"]
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






