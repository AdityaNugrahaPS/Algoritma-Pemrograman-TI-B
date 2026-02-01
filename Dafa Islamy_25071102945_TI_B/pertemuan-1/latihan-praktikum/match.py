#match statement berguna ketika terlalu banyak if else statement yang akan ditulis, match statement meringkas penulisan if else statement

'''
syntax

match expression:
    case x:
        code block
    case y:
        code block
    case z:
        code block
'''

hari = 5
match hari:
    case 1:
        print('Senin')
    case 2:
        print('Selasa')
    case 3:
        print('Rabu')
    case 4:
        print('Kamis')
    case 5:
        print('Jumat')
    case 6:
        print('Sabtu')
    case 7:
        print('Minggu')

hari = 5
match hari:
    case 6:
        print('Hari ini hari Sabtu')
    case 7:
        print('Hari ini hari Minggu')
    case _:
        print('Hari ini bukan hari libur') #tanda (_) digunakan ketika tidak ada kecocokan pada blok kode

#tanda (|) atau or operator dapat digunakan ketika terdapat lebih dari satu nilai match untuk satu case
hari = 5
match hari:
    case 1 | 2 | 3 | 4 | 5:
        print('Hari ini weekday')
    case 6 | 7:
        print('Hari ini weekend')

bulan = 6
hari = 5
match hari:
  case 1 | 2 | 3 | 4 | 5 if bulan == 5:
    print("Hari ini merupakan hari kerja di bulan Mei")
  case 1 | 2 | 3 | 4 | 5 if bulan == 6:
    print("Hari ini adalah hari kerja di bulan Juni")
  case _:
    print("No match")