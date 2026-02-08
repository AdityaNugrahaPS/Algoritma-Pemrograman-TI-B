# match = versi switch case di python
bulan = 2
match bulan:
    case 1: 
        print("Januari")
    case 2: 
        print("Februari")
    case 3: 
        print("Maret")
    case 4: 
        print("April")
    case 5: 
        print("Mei")
    case 6: 
        print("Juni")
    case 7: 
        print("Juli")
    case 8: 
        print("Agustus")
    case 9: 
        print("September")
    case 10: 
        print("Oktober")
    case 11: 
        print("November")
    case 12: 
        print("Desember")
    case _:
        print("kiamat") # T-T

hari = 5
match hari:
    case 1 | 2 | 3 | 4: # dipisah dengan | karena 'or'
        print("Hari kuliah :( ")
    case 5| 6 | 7:
        print("Hari libur :)")
    case _:
        print("Hari tidak valid")

match hari:
    case 1 | 2 | 3 | 4 if bulan == 1: # tambahan kondisi dengan if
        print("Hari kuliah di bulan Januari")
    case 1 | 2 | 3 | 4 if bulan == 2:
        print("Hari kuliah di bulan Februari")
    case _:
        print("Bukan hari kuliah atau bulan tidak valid")