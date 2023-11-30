levesek = ["Nem kér semmit", "Húsleves", "Gyümölcsleves", "Bableves"]
levesar = [0,880,600,1200]
foetel = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]
rendeles_lista=[]
rendeles_listaar = []
import etlap
import rendeles
import osszegzes
import nyugta

etlap.etl()
etlap.lev(levesek,levesar,"Leves")
etlap.lev(foetel,foetelar,"Főétel")
etlap.lev(itallap,italar,"Italok")
etlap.lev(desszertek,desszertar,"Desszertek")

leves_index=osszegzes.leves_valasztas()
rendeles_lista.append(levesek[leves_index])
rendeles_listaar.append(levesar[leves_index])

foetel_index=osszegzes.foetel_valasztas()
rendeles_lista.append(foetel[foetel_index])
rendeles_listaar.append(foetelar[foetel_index])


ital_index = osszegzes.ital_valasztas()
rendeles_lista.append(itallap[ital_index])
rendeles_listaar.append(italar[ital_index])

desszert_index = osszegzes.desszert_valasztas()
rendeles_lista.append(desszertek[desszert_index])
rendeles_lista.append(desszertar[desszert_index])

nyugta.nyugta(rendeles_lista, rendeles_listaar)



