# Contoh sederhana match case
nilai = 80

match nilai:
    case 90 | 80:
        print("Bagus")
    case 70 | 60:
        print("Cukup")
    case _:
        print("Kurang")
# Output: Bagus

# Contoh dengan kombinasi case
hari = 3

match hari:
    case 1 | 2 | 3 | 4 | 5:
        print("Hari kerja")
    case 6 | 7:
        print("Hari libur")
    case _:
        print("Tidak valid")
# Output: Hari kerja

# Contoh dengan if statement
angka = 10

match angka:
    case x if x > 0:
        print("Positif")
    case x if x < 0:
        print("Negatif")
    case _:
        print("Nol")
# Output: Positif