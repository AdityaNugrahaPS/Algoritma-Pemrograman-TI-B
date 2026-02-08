#sub-bab 'python variables'

#creating variables
x =  6
y = 12.3
y = 'Dafa'
print(x) #output akan menampilkan 6
print(y) #output akan menampilkan 'Dafa' karena variabel y telah diubah

#casting
x = int(6) #menjelaskan tipe data x adalah integer
y = float(12.3) #menjelaskan tipe data x adalah float
z = str('Dafa') #menjelaskan tipe data x adalah string

#type
x = 6
y = 12.3
print(type(x)) #untuk melihat tipe data variabel x
print(type(y)) #untuk melihat tipe data variabel y


#sub-bab 'variable name'

#legal
namasaya = 'Dafa'
namaSaya = 'Dafa' #camel case
nama_saya = 'Dafa' #snake case
NAMASAYA = 'Dafa'
namasaya2 = 'Dafa'
_nama_saya = 'Dafa'
NamaSaya =  'Dafa' #pascal case

#illegal
'''
2namasaya = 'Dafa'
nama-saya = 'Dafa'
nama saya = 'Dafa'
'''


#sub-bab 'assign multiple values'

#many values to multiple variables
a, b, c,  = 'Motor', 'Mobil', 'Sepeda'
print(a)
print(b)
print(c)

#one values to multiple variables
a = b = c = "Motor"
print(a)
print(b)
print(c)

#unpack a collection
kendaraan  = ['Motor', 'Mobil', 'Sepeda']
a, b, c, = kendaraan
print(a)
print(b)
print(c)


#sub-bab 'output variables'

x = 'Saya mahasiswa Universitas Riau'
print(x)

w = 'Saya'
x = 'mahasiswa'
y = 'Universitas'
z = 'Riau'
print(w, x, y, z) #menggabungkan variabel menggunakan comma

w = 'Saya '
x = 'mahasiswa '
y = 'Universitas '
z = 'Riau'
print(w + x + y + z) #menggabungkan variabel menggunakan operator +

x = 33
y = 77
print(x + y) #melakukan operasi aritmetika


#sub-bab 'global variables'

x = 'Dafa' #x adalah variabel global yang bisa digunakan baik di dalam fungsi ataupun diluar

def function():
    print('Nama saya ' + x)

function()


x = 'Dafa' #variabel global

def function():
    x = 'Islamy'
    print('Nama saya ' + x) #output akan menghasilkan 'Nama saya Islamy' karena menggunakan variabel didalam fungsi

function()

print('Nama saya ' + x) #output akan menghasilkan 'Nama saya Dafa' karena menggunakan variabel global

#global keyword
x = 'Dafa' #variabel global

def function():
    global x
    x = 'Islamy' #variabel global berubah menjadi 'Islamy' karena didefinisikan sebagai global

function()

print('Nama saya ' + x) #output akan menghasilkan 'Nama saya Islamy' karena variabel global telah berubah