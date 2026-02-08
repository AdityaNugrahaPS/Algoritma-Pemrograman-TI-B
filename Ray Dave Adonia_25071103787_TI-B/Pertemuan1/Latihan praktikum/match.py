# Match
print("-Match-")
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
        print("Galat.") # Default, konteksnya disini error

# Combine Values
match bulan:
    case 1 | 2 | 3 | 4 :
        print("Awal tahun.")
    case 5 | 6 | 7 | 8 :
        print("Pertengahan tahun.")
    case 9 | 10 | 11 | 12 :
        print("Akhir tahun.")
print(" ")

