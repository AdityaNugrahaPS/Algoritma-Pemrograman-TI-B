#PYTHON IF

a = 66 #Variabel a memiliki value sebesar 66
b = 99 #Variabel b memiliki value sebesar 99
if b > a:
  print("b lebih besar dari a") #Jika b lebih besar dari a, maka akan menghasilkan output ini

#PYTHON ELIF

a = 88 #Variabel a memiliki value sebesar 88
b = 88 #Variabel b memiliki value sebesar 88

if a > b:
    print('a lebih besar dari b') #Jika a lebih besar dari b, maka akan menghasilkan output ini
elif a == b:
    print('a sama besar dengan b') #Namun, jika a sama besar dengan b, maka akan menghasilkan output ini

#PYTHON ELSE

a = 789 #Variabel a memiliki value sebesar 789
b = 456 #Variabel b memiliki value sebesar 456
if a > b:
  print("a lebih besar dari b") #Jika a lebih besar dari b, maka akan menghasilkan output ini
else:
  print("a tidak lebih besar dari b") #Tapi a tidak lebih besar dari b, maka akan menghasilkan output ini

#SHORTHAND IF

a = 33 #Variabel a memiliki value sebesar 33
b = 44 #Variabel b memiliki value sebesar 44

print('A') if a > b else print('B') #Output akan mencetak A jika a lebih besar dari b, namun akan mencetak B jika a tidak lebih besar dari b

a = 10 #Variabel a memiliki value sebesar 10
b = 20 #Variabel b memiliki value sebesar 20

bigger = a if a > b else b #Variabel bigger akan terisi  oleh salah satu value, yaitu di antara 10 dan 22
print('Bigger is', bigger) #Jika a lebih besar dari b, maka bigger bernilai 10. Namun jika a tidak lebih besar dari b, bigger bernilai 20

#LOGICAL OPERATORS

'''
and = Mengembalikan True jika kedua kondisi benar
or = Mengembalikan True jika salah satu dari dua kondisi benar
not = Membalikkan hasil, mengembalikan False jika hasilnya adalah True
'''

a = 123 #Variabel a memiliki value sebesar 123
b = 22 #Variabel b memiliki value sebesar 22
c = 345 #Variabel c memiliki value sebesar 345
if a > b and c > a: #Jika a lebih besar dari b dan c lebih besar dari a
  print("Kedua kondisi bernilai True") #Jika kondisi pertama dan kedua benar, maka akan ditampilkan output berikut

a = 123 #Variabel a memiliki value sebesar 123
b = 22 #Variabel b memiliki value sebesar 22
c = 345 #Variabel c memiliki value sebesar 345
if a > b or a > c: #Jika a lebih besar dari b atau a lebih besar dari c
  print("Setidaknya satu dari kondisi bernilai True") #Jika salah satu dari kondisi pertama dan kedua benar, maka akan ditampilkan output berikut

a = 22 #Variabel a memiliki value sebesar 22
b = 345 #Variabel b memiliki value sebesar 345
if not a > b: #Jika a lebih besar dari b
  print("a TIDAK lebih besar dari b") #Jika kondisi bernilai benar, maka akan ditampilkan output berikut, karena operator not membalikkan nilai

#NESTED IF (Ada if di dalam if)

a = 89 #Variabel a memiliki value sebesar 89

if a > 50: #Jika a lebih besar dari 50
  print("Lebih dari 50,")
  if a > 80: #Jika a lebih besar dari 80
    print("Dan juga lebih dari 80")
  else:
    print("Tapi tidak lebih dari 90")

#PASS STATEMENT (Pass tidak memiliki arti apa-apa dan hanya digunakan sebagai placeholder atau pengganti)

umur = 19 #Variabel umur memiliki value sebesar 19

if umur < 21:
  pass #Digunakan pass agar tidak terjadi error, logikanya akan diimplementasikan setelahnya
else:
  print("Akses diterima!") #Jika umur di atas 21, maka akan menampilkan output berikut