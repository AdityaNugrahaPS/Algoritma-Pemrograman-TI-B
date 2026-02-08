#int : berisi bilangan bulat baik positif maupun negatif
x = 6
y = -61

print(type(x)) #mengetahui tipe data x yaitu integer
print(type(y)) #mengetahui tipe data y yaitu integer


#float : berisi bilangan desimal (koma) baik positif maupun negatif
a = 2.7
b = -14.66

print(type(a)) #mengetahui tipe data a yaitu float
print(type(b)) #mengetahui tipe data b yaitu float


#complex : berisi bilangan imajinary yang ditulis sebagai 'j'
p = 7j
q = -16j

print(type(p)) #mengetahui tipe data p yaitu complex
print(type(q)) #mengetahui tipe data q yaitu complex


#type conversion
x = 6 #variabel x berisi bilangan bulat 6 dengan tipe data integer
y = 6.1 #variabel y berisi bilangan desimal 6.1 dengan tipe data float
z = 6j #variabel x berisi bilangan imajiner 6j dengan tipe data complex

a = float(x) #variabel a mengambil nilai x dan mengubah tipe data nya dari integer menjadi float
b = int(y) #variabel b mengambil nilai y dan mengubah tipe data nya dari float menjadi int
c = complex(x) #variabel c mengambil nilai x dan mengubah tipe data nya dari integer menjadi complex

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))


#random number
import random
print(random.randrange(1, 17)) #modul akan menampilkan angka random (acak) dari 1 sampai 16 (17 tidak termasuk)