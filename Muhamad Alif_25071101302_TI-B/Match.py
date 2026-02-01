# Python Match
# Pernyataan `match` digunakan untuk melakukan tindakan berbeda berdasarkan kondisi yang berbeda.
# The Python Match Statement
'''
daripada menulis banyak pernyataan if..else, Anda dapat menggunakan pernyataan match.
Pernyataan match memilih salah satu dari banyak blok kode untuk dieksekusi.
'''

''''
match expression:
  case x:
    code block
  case y:
    code block
  case z:
    code block
    '''

'''
Begini cara kerjanya:
Ekspresi pencocokan dievaluasi sekali.
Nilai ekspresi dibandingkan dengan nilai setiap kasus.
Jika ada kecocokan, blok kode terkait akan dieksekusi.
Contoh di bawah ini menggunakan nomor hari dalam seminggu untuk mencetak nama hari dalam seminggu:
'''

day = 4
match day:
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
  case 6:
    print("Sabtu")
  case 7:
    print("minggu")

# Default Value
day = 4
match day:
  case 6:
    print("Today is Saturday")
  case 7:
    print("Today is Sunday")
  case _:
    print("Looking forward to the Weekend")

# Combine Values
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

# If Statements as Guards
month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

