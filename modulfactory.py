from base.modul import Modul
from fisdas.vektor import Vektor
from fisdas.menara_air import MenaraAir
from fisdas.gelombang import Gelombang
from fisdas.gerakpeluru import GerakPeluru
from fisdas.tetapan_pegas import TetapanPegas

class ModulType:
    Choice = 1
    Modul = 2

# ini buat list modulnya
# langsung masukin sini aja
list_modul = {
    Vektor.name : Vektor,
    MenaraAir.name : MenaraAir,
    Gelombang.name : Gelombang,
    GerakPeluru.name : GerakPeluru,
    TetapanPegas.name : TetapanPegas
}

def get_all_modul() -> list:
    return list_modul


def get_type( key : str ):
    if issubclass( list_modul[key], Modul ):
        return ModulType.Modul

    elif list_modul[key] is dict:
        return ModulType.Choice
    
def get_modul( key : str ) -> Modul:
    return list_modul.get(key)
