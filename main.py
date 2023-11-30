levesek = ["Nem kér semmit", "Húsleves", "Gyümölcsleves", "Bableves"]
levesar = [0,880,600,1200]
foetel = ["Nem kér semmit", "Tojásos nokedli", "Rántott hús rizibizivel", "Rántott hús sült krumplival"]
foetelar = [0,880,1500,2000]
itallap = ["Nem kér semmit", "Coca Cola", "Kőbányai", "Márka szörp"]
italar = [0,450,450,350]
desszertek = ["Nem kér semmit", "Tiramisu", "Nutellás palacsinta", "Túrós palacsinta"]
desszertar = [0,650,750,250]
import etlap
import rendeles
import osszegzes

etlap.etl()
etlap.lev(levesek,levesar,"Leves")
etlap.lev(foetel,foetelar,"Főétel")
etlap.lev(itallap,italar,"Italok")
etlap.lev(desszertek,desszertar,"Desszertek")

osszegzes.leves_valasztas()
osszegzes.foetel_valasztas()
osszegzes.ital_valasztas()
osszegzes.desszert_valasztas()
osszegzes.nyugta()


