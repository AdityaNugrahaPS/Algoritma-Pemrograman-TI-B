#Python Match Statement
'''
Daripada menulis banyak pernyataan if ... else, kita dapat menggunakan pernyataan match.
Pernyataan ini memilih salah satu dari banyak blok kode yang akan dieksekusi.
'''

print("--Match Statement--")

adjab = 3
match adjab:
  case 1:
    print("a")
  case 2:
    print("b")
  case 3:
    print("c")