#Bagian ini berisi match case (mirip dengan swith case kalau di c++)

rasaSakit = 5

match rasaSakit:
    case 1:
        print("Biasa aja")
    case 2:
        print("Agak sakit")
    case 3:
        print("Lumayan sakit")
    case 4:
        print("Sakit banget")
    case 5:
        print("meninggal")
    case _:
        print("1 sampe 5 aja woeh")