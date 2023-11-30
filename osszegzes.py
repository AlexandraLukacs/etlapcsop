levesek = ["Nem kér semmit", "Húsleves", "Gyümölcsleves", "Bableves"]
levesar = [0,880,600,1200]
foetel = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]
import rendeles

meret: int = int(50)
karakter = "*"

def keret(meret,karakter):
    print(karakter*meret)

def szoveg_kiiras(jel, szoveg, jel2,nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def etel_kiiras(jel, szoveg, jel2,nyugta_meret,ar):
    behuzas = nyugta_meret-10
    arbehuzas = int(nyugta_meret/10)
    print(f"{jel}{szoveg:<{behuzas}}{ar:<{arbehuzas}}ft {jel2}")

def leves_valasztas():
    leves=rendeles.rendelesek(levesek, levesar, "Leves")
    print(f"{leves}-t kért!")
    return leves

def foetel_valasztas():
    foetelek=rendeles.rendelesek(foetel, foetelar, "Főétel")
    print(f"{foetelek}-t kért!")
    return foetelek

def ital_valasztas():
    italok=rendeles.rendelesek(itallap, italar, "Italok")
    print(f"{italok}-t kért!")
    return italok

def desszert_valasztas():
    desszert = rendeles.rendelesek(desszertek, desszertar, "Desszert")
    print(f"{desszert}-t kért!")
    return desszert




def nyugta_levesek(levesek):
    for i in range(0, len(levesek), 1):
        if "0" in i:
            print(karakter, levesek[0], karakter)
        elif "1" in i:
            print(karakter, levesek[1], karakter)
        elif "2" in i:
            print(karakter, levesek[2], karakter)
        elif "3" in i:
            print(karakter, levesek[3], karakter)
    keret(meret, karakter)
    

def rendeltetelital():
    keret(meret, karakter)
    szoveg_kiiras()

