#1. Boolean Values
'''
Boolean mewakili salah satu dari dua nilai Benar (true) dan Salah (false).
Saat dua nilai dibandingkan, ekspresi dievaluasi dan Python mengembalikan nilai Boolean.
'''

print("--Booleans--") #Menampilkan header
print(1 > 2)  #False
print(1 == 2) #False
print(1 < 2)  #True

'''
Saat kondisi dijalankan dalam pernyataan if, Python mengembalikan Benar atau Salah.
'''

a = 300
b = 400

if a > b :
    print("a is bigger than b")
else :
    print("b is bigger than a")

#2. Evaluate Values and Variables
'''
Fungsi bool() memungkinkan untuk mengevaluasi nilai apa pun, dan mengembalikan nilai Benar atau Salah
'''

print(bool(15))
print(bool("Hello"))

a = 300
b = "Hello"

print(bool(a)) #Mengevaluasi variabel
print(bool(b))

#3. Most Values are True
'''
Hampir semua nilai dievaluasi jika memiliki nilai True
String apa pun adalah True, kecuali string kosong.
Angka apa pun adalah True, kecuali 0.
Setiap daftar, tuple, himpunan, dan kamus adalah True, kecuali yang kosong.
'''

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])
#Ketiganya bernilai True

#4. Some Values are False
'''
Pernyataan ini akan mengembalikan nilai False
'''

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})