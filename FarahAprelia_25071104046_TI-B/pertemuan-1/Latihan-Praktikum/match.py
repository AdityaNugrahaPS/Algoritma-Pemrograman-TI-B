#MATCH (Digunakan sebagai alternatif untuk menghindari penulisan banyak if-else)

'''
match expression:
  case a:
    code block
  case b:
    code block
  case c:
    code block
'''

bulan = 4 #Variabel bulan memiliki value 4
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