def keret(meret,karakter):
    print(karakter*meret)
    
def szoveg_kiiras(jel, szoveg, jel2,nyugta_meret):
    hossz: int = int(nyugta_meret-(len(jel) + len(jel2)))
    print(f"{jel}{szoveg:^{hossz}}{jel2}")

def etel_kiiras(jel, szoveg, jel2,nyugta_meret,ar):
    behuzas = nyugta_meret-10
    arbehuzas = int(nyugta_meret/10)
    print(f"{jel}{szoveg:<{behuzas}}{ar:<{arbehuzas}}ft {jel2}")