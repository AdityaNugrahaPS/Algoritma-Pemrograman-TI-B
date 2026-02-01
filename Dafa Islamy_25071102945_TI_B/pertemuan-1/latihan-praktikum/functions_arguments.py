'''
- Fungsi adalah blok kode yang hanya berjalan saat dipanggil.
- Fungsi dapat mengembalikan data sebagai hasilnya.
- Fungsi membantu menghindari pengulangan kode.
'''

def myfunction():
    print('Hello World')
myfunction() #untuk memanggil fungsi, tulis nama fungsi fungsi beserta tanda kurung

#fungsi berguna ketika ingin digunakan berkali-kali
def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9
print(fahrenheit_to_celcius(32))
print(fahrenheit_to_celcius(50))
print(fahrenheit_to_celcius(122))

#return statement akan mengirim data kembali ke kode yang memanggilnya
def namaMahasiswa():
    return 'Dafa Islamy'
nama = namaMahasiswa()
print(nama)

def namaMahasiswa():
    return 'Dafa Islamy'
print(namaMahasiswa()) #juga dapat mengembalikan nilai langsung

#fungsi tidak boleh kosong, tetapi jika ingin dibuat kosong atau tidak melakukan apa-apa, dapat menggunakan pass statement
def myfunction():
    pass


#sub-bab 'python arguments'
'''
Informasi dapat diteruskan ke fungsi menggunakan argumen.
Argumen ditentukan setelah nama fungsi, didalam tanda kurung, argumen bisa berapa saja asal dipisah dengan tanda koma
'''

def fungsiNamaLengkap(fname):
    print(fname + ' Islamy') #fname adalah parameter

#"Dafa", "Arya", "Afif" adalah argumen
fungsiNamaLengkap("Dafa")
fungsiNamaLengkap("Arya")
fungsiNamaLengkap("Afif")

#Kita dapat  menetapkan default value dari parameter, jika fungsi saat dipanggil tidak menggunakan argumen maka yang ditampilakn adalah default valuenya
def fungsiNamaLengkap(name = 'teman'):
    print('Halo', name)

fungsiNamaLengkap("Dafa")
fungsiNamaLengkap() #output akan menghasilkan 'Halo teman' karena argumen dikosongkan

#argumen dapat dikirim dengan sintaks key = value
def function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
function(name = 'buddy', animal = 'dog') #dengan menggunakan keyword argumen, urutan argumen tidak berlaku

#jika tidak menggunakan keyword argumen, peletakan argumen harus sesuai urutan dan biasa disebut sebagai 'positional argument'
def function(animal, name):
    print("I have a", animal)
    print("My", animal + "'s name is", name)
function('dog', 'buddy')

#tipe data apapun dapat dikirim sebagai argumen dalam sebuah fungsi (string, number, list, dictionary)
def function(kendaraan):
    for x in kendaraan:
        print(x)
kendaraan = ['Motor', 'Mobil', 'Sepeda']
function(kendaraan)

#fungsi dapat mengembalikan nilai dengan menggunakan return statement
def penjumlahan(x, y):
    return x + y
hasil = penjumlahan(9, 7)
print(hasil)

#positional-only argument, kita dapat menentukan bahwa suatu fungsi hanya dapat memiliki positional argument dengan menambahkan tanda '/' diakhir argumen
def function(name, /):
    print('Perkenalkan nama saya', name)
function('Dafa')

#keyword-only argument, kita dapat menentukan bahwa suatu fungsi hanya dapat memiliki keyword argument dengan menambahkan tanda '*' diawal argumen
def function(*, name):
    print('Perkenalkan nama saya', name)
function(name = 'Dafa')

#kombinasi positional dan keyword only argument
#argumen sebelum tanda '/' adalah positional argumen dan argumen setelah tanda '*' adalah keyword argumen
def function(a, b, /, *, c, d):
    return a + b + c + d
hasil = function(3, 4, c = 7, d = 6)
print(hasil)