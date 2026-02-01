#MATCH

"""
match digunakan untuk melakukan tindakan berbeda berdasarkan kondisi yang berbeda.
"""
# KATA KUNCI (match)

contohmatch_menentukan_nilai = 5

match contohmatch_menentukan_nilai :
    case 1 :
        print("HALLO")
    case 2 :
        print("HALOO")
    case 3 :
        print("HAII")
    case 4 :
        print("HEIHEII")
    case 5 :
        print("ASSALAMUALAIKUM")

'''
ada juga namanya nilai default, yang kata kuncinya (case_), 
yang menandakan nilai kasus akhir ketika tidak ada kecocokan yang dapat di eksekusi
'''
contohmatch2 = 3
match contohmatch2:
    case 1 :
        print(".....")
    case 2 :
        print("HELLO SEMUA")
    case _ :
        print("lastt")

"Kita dapat menggabungkan nilai case itu menjadi satu"
contohmatch_menentukan_nilai = 5

match contohmatch_menentukan_nilai :
    case 1 | 2 | 3 | 4:
       print("assalamualaikum")
    case 5 :
        print("ASSALAMUALAIKUM")

"kita juga bisa membbuat if sebagai guard dalam ini"
bulan = 7
hari = 2
match hari:
  case 1 | 2 | 3 | 4 | 5 if bulan == 7:
    print("April")
  case 1 | 2 | 3 | 4 | 5 if bulan == 5:
    print("May")
  case _:
    print("ga ada")

#MATCH DONE