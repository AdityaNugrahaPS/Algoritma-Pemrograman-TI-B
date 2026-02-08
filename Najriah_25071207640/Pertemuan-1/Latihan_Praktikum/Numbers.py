#1. Python Numbers
'''
Ada 3 jenis numerik dalam Python (int, float, complex).
'''

x = 5    # int
y  = 7.0 # float
z = 1j   # complex

'''
Untuk memastikan tipe data dari suatu variabel, bisa dengan menggunakan type().
'''
print(type(x))
print(type(y))
print(type(z))

#2. Int
'''
Int, atau Integer, adalah bilangan bulat, positif atau negatif, 
tanpa desimal, dengan panjang yang tidak terbatas.
'''
a = 7
b = 78989665476
c = -9897655435

print(type(a))
print(type(b))
print(type(c))

#3. Float
'''
Float, atau "floating point number" adalah angka yang mengandung satu atau lebih desimal.
'''
d = 10.7
e = 4.5
f = -1.7

print(type(d))
print(type(e))
print(type(f))


'''
Float juga bisa berupa angka ilmiah dengan huruf "e" untuk menunjukkan pangkat 10.
'''
g = 45e8
h = 1E2
i = -2E3

print(type(g))
print(type(h))
print(type(i))

#4. Complex
'''
Bilangan kompleks ditulis dengan "j" sebagai bagian imajiner.
'''
j = 5j
k = 7j + 5
l = 3 - 2j

print(type(j))
print(type(k))
print(type(l))

#5. Type Convertion
'''
Suatu tipe data bisa diubah menjadi tipe data yang lain.
'''
x = 5    # int
y  = 7.0 # float
z = 1j   # complex

m = complex(x) #Mengubah int menjadi complex
n = int(y)     #Mengubah float menjadi int
o = float(x)   #Mengubah int menjadi float

print("--Type Convertion--") #Menampilkan header
print(m)
print(n)
print(o)

print("\n--Get The Type--") #Menampilkan header
print(type(m))
print(type(n))
print(type(o))

#6. Random Number
'''
Python tidak memiliki fungsi untuk membuat angka acak, tetapi Python memiliki modul bawaan
yang disebut 'random' yang dapat digunakan untuk membuat angka acak.
'''
import random

print("\n--Random Number--") #Menampilkan header
print(random.randrange(2, 7)) #Menampilkan angka acara dari rentang 2 sampai 7