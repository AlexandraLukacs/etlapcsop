import etlap
import osszegzes

levesek = ["0 - Nem kér semmit", "1 - Húsleves", "2 - Gyümölcsleves", "3 - Bableves"]
levesar = [0,880,600,1200]
foetel = ["0 - Nem kér semmit", "1 - Tojásos nokedli", "2 - Rántott hús rizibizivel", "3 - Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["0 - Nem kér semmit", "1 - Coca Cola", "2 - Kőbányai", "3 - Márka szörp"]
italar = [0,450,450,350]
desszertek = ["0 - Nem kér semmit", "1 - Tiramisu", "2 - Nutellás palacsinta", "3 - Túrós palacsinta"]
desszertar = [0,650,750,250]

def rendelesek(lista,listaar, cim):
    for i in range(0, len(lista), 1):
        print(" ")
        print(" ")
        etlap.lev(lista,listaar, cim)
        print("Válasszon ételt/italt! (0-tól 3-ig válasszon)")
    

        i: int = int(input("írd be hogy hanyas számu ételt/italt kéred? (Írj egy 0-t ha semmit): "))

        ##rendeles = rendeles - 1
        leves = lista[i]
        '''print (leves + "-t kér!")'''
        return i
    



'''def rendelesossz():
    print(" ")
    print(" ")
    etlap.lev(levesek,levesar,"Leves")
    print("Válasszon levest! (0-tól 3-ig válasszon)")
    

    rendeles: int = int(input("írd be hogy hanyas számu levest kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    leves = levesek[rendeles]
    print (leves + "-t kér!")

    print(" ")
    print(" ")
    etlap.lev(foetel,foetelar,"Főétel")
    print("Válasszon főételt! (0-tól 3-ig válasszon)")
    list = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]

    rendeles1: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    kaja = list[rendeles1]
    print (kaja + "-t kér!")

    print(" ")
    print(" ")
    etlap.lev(itallap,italar,"Italok")
    print("Válasszon italt! (0-tól 3-ig válasszon)")
    itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]

    rendeles2: int = int(input("írd be hogy hanyas számu italt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    ital = itallap[rendeles2]
    print (ital + "-t kér!")

    print(" ")
    print(" ")
    etlap.lev(desszertek,desszertar,"Desszertek")
    print("Válasszon desszertet! (0-tól 3-ig válasszon)")
    desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]

    rendeles3: int = int(input("írd be hogy hanyas számu ételt kéred (Írj egy 0-t ha semmit)"))

    ##rendeles = rendeles - 1
    desszert = desszertek[rendeles3]
    print (desszert + "-t kér!")

    osszegzes.nyugta()
    osszegzes.nyugta_levesek()'''






