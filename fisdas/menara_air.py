from base.interfaces import InterfacesBase
from base.modul import Modul
import math

# kalo mau buat kelas(Modul) baru
# ini filenya dicopy terus ganti nama
# "Vektor"nya diganti
# "Modul"nya jangan
# kalo udah jadi, masukkin ke file modulfactory.py
class MenaraAir(Modul):
    # ini nama praktikumnya
    name = "Menara Air"

    # ini tempat ngambil nilai
    def init_formula(self, interfaces: InterfacesBase):
        # kalo mau minta bilangan bulat pake get_int
        # kalo minta bilangan desimal pake get_float
        # parameter pertama itu buat namain variablenya pas nanti dioper
        # kalo make parameter yang sama, nanti ke overwrite jadi hati hati
        interfaces.get_float("h1")
        interfaces.get_float("h2")

        # ini buat nambahin fungsi buat ngitung rumusnya,
        # parameter pertama itu hasil dari apa,
        # parameter kedua itu fungsinya
        # ini bisa dipanggil berkali-kali
        interfaces.add_func("v", self.kecepatan)
        interfaces.add_func("x", self.jarak)

    # ini fungsi buat ngitung rumusnya
    # parameter kedua itu buat nilai yang diambil dari method
    # get_value diatas
    # isi key( [key] ) itu sama kayak yang parameter diatas
    # kalo diatas interfaces.get_float("a")
    # ngambilnya value["a"]

    # kalo mau ngambil nama yang dimasukkin
    # di add_func parameter pertama
    # bisa ngambil lewat value["_name"]
    def kecepatan(self, value: dict):
        h1 = value["h1"]
        g  = 9.8

        return str(math.sqrt(2*g*h1)) + " m/s"

    def jarak(self, value: dict):
        h1 = value["h1"]
        h2 = value["h2"]

        return str(2*math.sqrt(h1*h2)) + " m"