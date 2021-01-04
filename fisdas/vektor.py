import math
from base.interfaces import InterfacesBase
from base.modul import Modul

def kuadrat( val ):
    return val ** 2

# kalo mau buat kelas(Modul) baru
# ini filenya dicopy terus ganti nama
# "Vektor"nya diganti
# "Moduil"nya jangan
# kalo udah jadi, masukkin ke file modulfactory.py
class Vektor( Modul ):
    # ini nama praktikumnya
    name = "Vektor"

    # ini tempat ngambil nilai
    def init_formula( self, interfaces : InterfacesBase ):
        # kalo mau minta bilangan bulat pake get_int
        # kalo minta bilangan desimal pake get_float
        # parameter pertama itu buat namain variablenya pas nanti dioper
        # kalo make parameter yang sama, nanti ke overwrite jadi hati hati
        interfaces.get_float("a")
        interfaces.get_float("b")
        interfaces.get_float("teta")

        # ini buat nambahin fungsi buat ngitung rumusnya,
        # parameter pertama itu hasil dari apa,
        # parameter kedua itu fungsinya
        # ini bisa dipanggil berkali-kali
        interfaces.add_func("a + b", self.penjumlahan_vektor )


    # ini fungsi buat ngitung rumusnya
    # parameter kedua itu buat nilai yang diambil dari method
    # get_value diatas
    # isi key( [key] ) itu sama kayak yang parameter diatas
    # kalo diatas interfaces.get_float("a")
    # ngambilnya value["a"]

    # kalo mau ngambil nama yang dimasukkin
    # di add_func parameter pertama
    # bisa ngambil lewat value["_name"]
    def penjumlahan_vektor( self, value : dict ):
        a = value["a"]
        b = value["b"]
        teta = value["teta"]

        res = kuadrat(a) + kuadrat(b) + ( 2 * a * b * math.cos(math.radians(teta)))
        res = math.sqrt(res)
        return res
