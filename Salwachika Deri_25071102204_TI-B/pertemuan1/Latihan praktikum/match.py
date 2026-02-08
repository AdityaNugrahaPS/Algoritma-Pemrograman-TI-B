'''
match adalah struktur kontrol yang dipakai untuk memilih aksi berbeda berdasarkan nilai tertentu.
'''

#contoh bentuk dasar
harikuliah = 4
match harikuliah:
  case 1:
    print("senin")
  case 2:
    print("selasa")
  case 3:
    print("rabu")
  case 4:
    print("kamis")
  case 5:
    print("jumat")
    #(_) maksudnya apapun adalah sebagai default

#default case (_)
    #Dipakai kalau tidak ada yang cocok:
hari = 4
match hari:
    case 6:
        print("Sabtu")
    case 7:
        print("Minggu")
    case _:
        print("Bukan akhir pekan")

#combine value
    #menggunakan Tanda | (atau). digunakan untuk rentang nilai kecil
baterai = 15
match baterai:
    case 0 | 1 | 2 | 3 | 4 | 5:
        print("Baterai kritis")
    case 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15:
        print("Baterai rendah")
    case _:
        print("Baterai aman") 

#If Statements as Guards   
    #Guard = kondisi tambahan setelah case menggunakan if
bulan = 5
hari = 4
match hari:
  case 1 | 2 | 3 | 4 | 5 if bulan == 4:
    print("hari libur di bulan april")
  case 1 | 2 | 3 | 4 | 5 if bulan == 5:
    print("hari libur dibulan mei")
  case _:
    print("tidak ada yang cocok")