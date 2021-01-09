from base.modul import Modul
from fisdas.vektor import Vektor
from fisdas.menara_air import MenaraAir
from fisdas.gelombang import Gelombang
from fisdas.gerakpeluru import GerakPeluru
from fisdas.tetapan_pegas import TetapanPegas
from fisdas.glb import GLB
from fisdas.glbb import GLBB
from fisdas.pgb import PGB

class ModulType:
    Choice = 1
    Modul = 2

# ini buat list modulnya
# langsung masukin sini aja
list_modul = {
    TetapanPegas.name : TetapanPegas,
    GerakPeluru.name : GerakPeluru,
    PGB.name : PGB,
    Gelombang.name : Gelombang,
    MenaraAir.name : MenaraAir,
    GLB.name : GLB,
    GLBB.name : GLBB,
    Vektor.name : Vektor
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
