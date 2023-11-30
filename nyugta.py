levesek = ["Nem kér semmit", "Húsleves", "Gyümölcsleves", "Bableves"]
levesar = [0,880,600,1200]
foetel = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]
import osszegzes
import rendeles

meret: int = int(50)
karakter = "*"

def keret(meret,karakter):
    print(karakter*meret)

def szoveg_kiiras(jel, szoveg, jel2,nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def szoveg_kiiras2(jel, szoveg, ar, jel2, nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{ar}{jel2}")


def nyugta(lista, listaar, ):
    keret(meret,karakter)
    szoveg_kiiras(karakter,"NYUGTA",karakter,meret)
    keret(meret,karakter)
    for i in range(0, len(lista), 1):
        szoveg_kiiras2(karakter, lista[i], listaar[i], karakter, meret)
    