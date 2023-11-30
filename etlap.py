meret: int = int(50)
karakter = "*"
'''levesek = ["0 - Nem kér semmit", "1 - Húsleves", "2 - Gyümölcsleves", "3 - Bableves"]
levesar = [0,880,600,1200]
foetel = ["0 - Nem kér semmit", "1 - Tojásos nokedli", "2 - Rántott hús rizibizivel", "3 - Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["0 - Nem kér semmit", "1 - Coca Cola", "2 - Kőbányai", "3 - Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]'''
'''''
lev() Leves
foet() Főétel
drink() Itallap
dessert() Desszertek
'''''





def keret(meret,karakter):
    print(karakter*meret)
def szoveg_kiiras(jel, szoveg, jel2,nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def etel_kiiras(jel, szoveg, jel2,nyugta_meret,ar):
    behuzas = nyugta_meret-10
    arbehuzas = int(nyugta_meret/10)
    print(f"{jel}{szoveg:<{behuzas}}{ar:<{arbehuzas}}ft {jel2}")



def etl():
    keret(meret,karakter)
    szoveg_kiiras(karakter,"Étlap",karakter,meret)
    keret(meret,karakter)

def lev(lista,listaar,cim):
    keret(meret,karakter)
    szoveg_kiiras(karakter,cim,karakter,meret)
    keret(meret,karakter)
    for i in range (0, len(lista), 1):
        leves = lista[i]
        ar = listaar[i]
        etel_kiiras(karakter,leves,karakter,meret,ar)


