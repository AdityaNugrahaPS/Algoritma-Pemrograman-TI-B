### Dalam python, tipe data dikelompokkan menjadi dua, yakni tipe data primitif dan tipe data collection.
## A. Tipe data primitif
# 1. Numbers
A = 1       # Ini merupakan integer atau bilangan bulat dan tidak memiliki angka desimal
B = 3.14    # Ini merupakan float atau bilangan rill yang mewakili angka desimal
C = 3 + 2j  # ini merupakan bilangan kompleks

print(type(A))  #output: int
print(type(B))  #output: float
print(type(C))  #output: complex


# 2. Boolean
Baik = True
jahat = False
print(type(Baik))   #output: bool
print(type(jahat))  #output: bool


# 3. String
kota = 'pekanbaru'
print(type(kota))  #output: str


## B. Tipe data collection
# 1. List
ibuKota = ['Jakarta', 'Bandung', 'Pekanbaru', 'Surabaya'] #bisa diisi dengan tipe data yg sama
identitas = ['Alam', 18, 1.65, True] # juga bisa dengan tipe data yang berbeda"

#kita bisa mengambil data dengan indeking misalnya indeks ke 1
print(ibuKota[1]) #output: Bandung

# kita juga bisa memanggil dari belakang, misalnya urutan ke dua dari belakang
print(ibuKota[-2]) #output: Pekanbaru

# Selain indeksing, ada yg namanya slicing, yaitu mengambil data berdasarkan rentang tertentu
# cth: var[start:stop:step] yg dimana start itu inklusif(>=) dan stop itu eksklusif(<)
ibuKota = ['Jakarta', 'Bandung', 'Pekanbaru', 'Surabaya', 'Medan', 'Padang', 'Yogyakarta']
print(ibuKota[1:]) # cetak semua ibukota dimulai dari indeks 1
print(ibuKota[:4]) # cetak semua ibukota yang berada sebelum indeks 4
print(ibuKota[0:6:2]) # cetak

# 2. Tuple
x = (1, 'satu', 1j, True)
print(type(x))  #output: tuple


# kita bisa mengambil nilainya baik dengan cara indeksing maupun slicing sama seperti list
print(x[1]) #output: satu
print(x[:3]) #output: (1, 'satu', 1j)

# tapi kita tidak bisa mengubah nilai yang ada didalammnya alias tuple bersifat immutable
try:
    x[1] = 'dua'
    print(x[1])
except TypeError:
    print('Tidak bisa merubah nilai tuple! tuple bersifat immutable') #ketika kode merubah isi tuple dijalankan, python akan memberikan jawaban bahwa ada kesalahan tipe, jadi kita akan menangkapnya dengan pengecualian/exception

# 3. Set
a = {2,4,7,4,9,1}
print(type(a))  #output: set

# set merupakan kumpulan data yang tidak memiliki urutan, jadi kita tidak bisa menggunakan indeksing maupun slicing
try:
    print(a[2])
except TypeError:
    print('Tidak bisa merubah nilai tuple! tuple bersifat immutable') #ketika kode indeksing dijalankan, python akan memberikan jawaban bahwa ada kesalahan tipe(TypeError)

# selain tidak berurutan, set itu bersifat unik, jadi ketika kita memasukkan nilai/data double, otomatis set akan membuangny. artinya tidak ada data duplikat didalamnya
b = {3, 3, 6, 7, 1, 12, 44, 6, 9}
print(b) #output: {1, 3, 6, 7, 9, 12, 44}

# Karena set merupakan himpunan dalam matematika,kita bisa menggunakan method union(gabungan) dan intersection(irisan)
a = {2,4,7,4,9,1}
b = {3, 3, 6, 7, 1, 12, 44, 6, 9}

gabungan = a.union(b) # menggabungkan dua himounan yaitu a dan b
print(f'gabungan: {gabungan}') # output: gabungan: {1, 2, 3, 4, 6, 7, 9, 12, 44}

irisan = a.intersection(b)
print('irisan:',irisan) # output: irisan: {1, 9, 7}

# selain menggunakan angka/numbers, kita bisa gunakan text/string sebagai data dalam set
buah = {'pepaya', 'nanas', 'anggur', 'apel', 'jeruk', 'pisang'}
print(buah) # output: {'nanas', 'pisang', 'apel', 'pepaya', 'jeruk', 'anggur'}
# output dari set yang berisi string berbeda" urutannya disetiap kali pemanggilan

# 4. Dictonery
dataDiri = {
    'nama' : 'alam',
    'umur' : 18,
    'prodi' : 'Teknik Informatika',
    'statusMahasiswa' : True,
    'BahasaPemograman' : ['python', 'c', 'cpp', 'js'] # kita bisa menyimpan list dalam dictonary
}
print(type(dataDiri)) # output: dict

# pada dictonary, data tidak dali disimpan berdasarkan indeksnya, tetapi disimpan sebagai pasangan key(kunci) dan value(nilai)
print(dataDiri['prodi'])# output: teknik Informatika

# karena sifat uniknya itu, key harus unik dan tidak boleh ada duplikatnya, tetapi value boleh sama
kamus = {
    'apple' : 'apel',
    'banana' : 'pisang', 
    'grape' : 'anggur',
    'apple' : 'pisang'
}
print(kamus) # output: {'apple': 'pisang', 'banana': 'pisang', 'grape': 'anggur'}
# dapat dilihat bahwa dia melihat nilai yang paling terakhir di masukkan

