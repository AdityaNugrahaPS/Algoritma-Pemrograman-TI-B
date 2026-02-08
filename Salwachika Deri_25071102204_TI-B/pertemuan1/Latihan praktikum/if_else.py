#if statement
umur = 18
if umur >= 17:
    print("sudah boleh membuat KTP")
#multipple statements if
nilai = 90
if nilai >=85:
    print('nilai sangat baik')
    print('tanda termasuk ke daftar siswa eligibel')

#Elif statements
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
#multiple statements Elif
score = 75
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#else statements
a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#shorthand if & Elif
#if dan Elif didalam satu baris
a = 2
b = 330
print("A") if a > b else print("B")     #if dalam satu baris

a = 10
b = 20
bigger = a if a > b else b      #elif dalam satu baris
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")       #beberapa kondisi didalam satu baris

#menggunakan logical operator
'''
and = semua harus benar
or = cukup salah satu benar
not = kebalikannya
'''
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Nested If Statements
#menggunakan if di dalam if
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")