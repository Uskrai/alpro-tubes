from base.interfaces import InterfacesBase
from base.modul import Modul
class Gelombang( Modul ):
    name = "Gelombang"
    def init_formula( self, interfaces : InterfacesBase ):
        interfaces.get_float("s",
                             brief="Panjang Gelombang Seluruhnya",
                             deskripsi="Panjang gelombang seluruhnya dalam\n\
1 frekuensi dan 1 amplitudo",
                             posfix="m")
        interfaces.get_float("n",
                             brief="jumlah gelombang yang terukur",
                             deskripsi="Jumlah gelombang yang dapat diukur dalam\n\
1 frekuensi dan 1 amplitudo")
        interfaces.get_float("lamda",
                             brief="panjang gelombang",
                             deskripsi="panjang gelombang berdasarkan hasil perhitungan s/n",
                             posfix="m")
        interfaces.get_float("f",
                             brief="frekuensi",
                             deskripsi="Frekuensi adalah ukuran jumlah terjadinya sebuah\n\
peristiwa dalam satuan waktu.",
                             posfix="Hz")
        interfaces.add_func("lamda", self.menentukan_panjang_gelombang,
                            brief="Panjang gelombang",
                            deskripsi="panjang gelombang berdasarkan hasil perhitungan s",
                            posfix="m")
        interfaces.add_func("v", self.menentukan_cepat_rambat_gelombang,
                            brief="Cepat rambat gelombang",
                            deskripsi="Cepat rambat gelombang yaitu jarak yang ditempuh gelombang satu detik",
                            posfix="m/s")

    def menentukan_panjang_gelombang( self, value : dict ):
        s = value["s"]
        n = value["n"]
        if n == 0:
            return 0
        return s/n

    def menentukan_cepat_rambat_gelombang(self, value : dict):
        lamda = value["lamda"]
        f = value["f"]
        return lamda*f
