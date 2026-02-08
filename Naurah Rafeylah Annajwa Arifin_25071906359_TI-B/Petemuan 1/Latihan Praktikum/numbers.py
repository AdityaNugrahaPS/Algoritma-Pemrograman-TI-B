#numeric types in python

x = 7 #ini adalah numbers tipe int
y = 33.5 #ini adalah numbers tipe float
z = 6j #ini adalah numbers tipe complex

print(type(x)) #untuk menampilkan tipe numbers x
print(type(y)) #untuk menampilkan tipe numbers y
print(type(z)) #untuk menampilkan tipe numbers z

#type conversion

x = 7
y = 33.5
z = 6j

a = float(x) #mengubah tipe int menjadi float
b = int(y) #mengubah tipe float menjadi int
c = complex(x) #mengubah tipe int menjadi complex

print(a); print(b); print(c) #menampilkan isi dari varabel a,b dan c
print(type(a)) #menampilkan tipe yang telah di convert
print(type(b)) #menampilkan tipe yang telah di convert
print(type(c)) #menampilkan tipe yang telah di convert

#complex numbers tidak bisa diubah ke type numbers yang lain

#random numbers

import random #untuk nomor acak
print(random.randrange(10, 100)) #menampilkan nomor acak dengan rentang 10 sampai 100