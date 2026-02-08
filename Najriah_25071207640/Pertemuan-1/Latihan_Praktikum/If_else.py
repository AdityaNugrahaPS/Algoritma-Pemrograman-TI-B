#1. Python If Statement
'''
Python mendukung kondisi logis yang biasa dari matematika:
Sama dengan: a == b
Tidak Sama: a != b
Kurang dari: < b
Kurang dari atau sama dengan: a <= b
Lebih besar dari: a > b
Lebih besar dari atau sama dengan: a >= b
Kondisi ini dapat digunakan dalam beberapa cara, paling sering dalam pernyataan "if" dan loop.
Pernyataan "if" ditulis dengan menggunakan kata kunci if.
'''

print("--Python If Statement--") #Menampilkan header

a = 1
b = 2
if b > a:
  print("b is greater than a")

'''
Kita dapat memiliki beberapa pernyataan di dalam blok if.
'''

age = 21
if age >= 19:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")

'''
Variabel Boolean dapat digunakan langsung dalam pernyataan if tanpa operator perbandingan.
'''
login = True
if login :
  print("P, mabar")

#2. Python Elif Statement
'''
Kata kunci elif memungkinkan Anda memeriksa beberapa ekspresi untuk True dan mengeksekusi 
blok kode segera setelah salah satu kondisi dievaluasi ke True.
'''

print("\n--Python Elif Statement--") #Menampilkan header

a = 100
b = 100
if b > a:
  print("b is bigger than a")
elif a == b:
  print("equal")

'''
Kita dapat memiliki pernyataan elif sebanyak yang dibutuhkan. Python akan memeriksa 
setiap kondisi secara berurutan dan menjalankan yang pertama yang benar
'''

score = 57

if score >= 90:
  print("A")
elif score >= 80:
  print("B")
elif score >= 70:
  print("C")
elif score >= 60:
  print("D")

#3. Python Else Statement
'''
Kata kunci else menangkap apa pun yang tidak tertangkap oleh kondisi sebelumnya.
Pernyataan else dijalankan ketika kondisi if (dan kondisi elif apa pun) dievaluasi ke False.
'''

print("\n--Python Else Statement--") #Menampilkan header

a = 157
b = 33
if b > a:
  print("b is bigger than a")
else:
  print("b is not bigger than a")

#4. Short Hand If
'''
Jika hanya memiliki satu pernyataan untuk dieksekusi, Kita bisa meletakkannya pada 
baris yang sama dengan pernyataan
'''

print("\n--Short hand If--") #Menampilkan header
a = 5
b = 2
if a > b: print("a is bigger than b")

#Short Hand If ... Else
a = 2
b = 5
print("A") if a > b else print("B")

#Assign a Value With If ... Else
a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

#Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

#5. Nested If
'''
Anda dapat memiliki pernyataan if di dalam pernyataan if. 
Ini disebut pernyataan if bersarang.
'''

print("\n--Nested If--") #Menampilkan header

x = 55

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#6. Pass Statements
'''
Pernyataan if tidak boleh kosong, tetapi jika Anda Untuk beberapa alasan memiliki pernyataan 
if tanpa isi, masukkan pernyataan pass untuk menghindari kesalahan.
'''

print("\n--Pass Statements--")
a = 50
b = 200

if b > a:
  pass