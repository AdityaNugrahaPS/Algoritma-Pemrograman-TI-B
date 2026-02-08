'''
---MACAM - MACAM TIPE DATA YANG ADA DI PYTHON---
Text Type       :	str 
Numeric Types   :	int, float, complex
Sequence Types  :	list, tuple, range
Mapping Type    :	dict
Set Types       :	set, frozenset
Boolean Type    :	bool
Binary Types    :	bytes, bytearray, memoryview
None Type       :	NoneType
'''
#MARI KITA BAHAS SATU SATU YAAAA -RANIA

#1. Tipe Data Text (biasa dikenal dengan string)
'''
jadi, tipe data text ini berupa kumpulan karakter
'''

contohstring = 'Ini output dari string'
print(contohstring)
print(type(contohstring))

#2. Tipe Data Numbers
'''
Dalam Numbers, ada tiga numerik yang tersedia dalam Python, yaitu:
1. Integer
    yaitu tipe data yang berisi bilangan bulat, mau itu positif atau negatif
2. Float
    yaitu tipe data yang berisi bilangan desimal
3. Complex
    yaitu tipe data yang berisi bilangan kompleks dengan ditulis huruf "j" sebagai bagian imajiner
'''


contohint = 8
contohfloat = 4.3
contohcomplex = 8j

print(contohint)
print(contohfloat)
print(contohcomplex)

print(type(contohint))
print(type(contohfloat))
print(type(contohcomplex))

#3.Sequence Types 
'''
tipe ini berfungsi untuk menyimpan kumpulan elemen, baik sesama elemen ataupun berbeda elemen.
berikut contoh Sequence Types:
1. List
    List digunakan untuk menyimpan beberapa nilai dalam satu variabel
    List dibuat dengan menggunakan tanda kurung siku []
    List memungkinkan item yang ada didalamnya dapat diubah, diurutkan, ataupun nilai duplikat
    item pertama di dalam List terletak pada index [0], item kedua [1], dan seterusnya.
    tipe data list ini adalah <list>
'''
#contoh list
contohlist = [4, 'Rania', 8.9, True]
print(contohlist)
print(type(contohlist))


'''
2. Tuple
    Tuple digunakan untuk menyimpan beberapa nilai dalam satu variabel.
    perbedaan Tuple dengan List adalah, Tuple dibuat dengan menggunakan tanda kurung (),
    lalu nilai didalam Tuple, tidak dapat diubah.
    tipe data untuk tuple adalah <tuple>
'''
#contoh tuple
contohtuple = (87, "Universitas Riau", False, -6.9)
print(contohtuple)
print(type(contohtuple))

'''
3. Range
    Range adalah fungsi bawaan untuk mengembalikan urutan angka yang tidak dapat untuk diubah
    tipe data range ini adalah <range>
'''
#contoh range
contohrange = range(10)
print(contohrange)
print(type(contohrange))

#4. Mapping Type
'''
    Dictionary
    Dictionary digunakan untuk menyimpan nilai data dengan pasangan kunci yaitu key value
    Dictionary merupakan kumpulan yang berurut, dapat diubah, tetapi tidak memungkinkan untuk di duplikasi.
    Dictionary dibuat tanda kurung kurawal {} dan memiliki key dan value.
    tipe data Dictionary adalah <dict>
'''
#contoh dictionary
contohdict = {'nama': 'Rania', 'nim': '25071101294', 'kelas':'Teknik Informatika - B'}
print(contohdict)
print(type(contohdict))

#5. Set Types
'''
1.  Set
    Set digunakan untuk menyimpan beberapa nilai dalam satu variabel
    Perbedaan Set dari Sequence Type lainnya adalah Set dibuat dengan menggunakan tanda kurung kurawal {},
    lalu, set tidak memungkinkan item yang tidak terurut, tidak dapat di ubah, dan tidak ada indeks
    tipe data Set adalah <set>
'''
#contoh set
contohset = {1,3,4,5,6,7,3,2}
print(contohset)
print(type(contohset))

'''
2.  Frozenset
    Frozenset adalah versi dari set yang tidak dapat di ubah, tidak dapat di tambah atau di hapus dari Frozenset.
    tipe data Frozenset adalah <frozenset>
'''
#contoh frozenset
contohfrozenset = frozenset({'nama','nim','kelas',3,2,4})
print(contohfrozenset)
print(type(contohfrozenset))

#6. Boolean Type
'''
    Boolean
    Boolean adalah tipe data yang mewakili satu nilai, yaitu benar (True) atau salah (False)
    tipe data Boolean adalah <bool>

    Hampir semua nilai di evaluasi True, contohnya:
    - semua string adalah True, kecuali string kosong
    - angka apapun adalah True, kecuali 0
    - semua list, tuple, set, dict adalah True, kecuali yang kosong.

    bagi string kosong, 0, ataupun list dan kawan kawan yang kosong, maka akan dievaluasi menjadi False
'''
#contoh boolean
contohboolean1 = True
contohboolean2 = False

print(contohboolean1)
print(contohboolean2)

print(type(contohboolean1))
print(type(contohboolean2))

#7. Binary Types
'''
1.  bytes
    Urutan byte yang tidak dapat diubah. 
    Tipe ini tepat untuk data biner yang tidak perlu diubah setelah dibuat
'''
#contoh bytes
contohbytes = b'ini contoh bytes'

print(contohbytes)

print(type(contohbytes))

'''
2.  bytearray
    Urutan byte yang dapat diubah, ini digunakan jika kita ingin memodifikasi data biner secara dinamis
'''
#contoh bytesarray
contohbytesarray = bytearray(39)

print(contohbytesarray)

print(type(contohbytesarray))

'''
3.  memoryview
    Objek view yang menyediakan cara untuk mengakses data biner dari objek lain (seperti bytes atau bytearray) tanpa menyalin data yang sebenarnya. 
    Ini memungkinkan manipulasi data biner yang efisien dalam hal memori. 
'''
#contoh memoryview
contohmemoryview = memoryview(bytes(4))

print(contohmemoryview)

print(type(contohmemoryview))

#8. None Type
'''
    NoneType
    None itu adalah suatu konostanta khusus yang mewakili ketiadaan nilai.
    tipe data dari None adalah <NoneType>
'''
#contoh nonetype
contohnone = None

print(contohnone)

print(type(contohnone))


#BAB INI FOKUS KEPADA BAGAIMANA CARA KITA MENAMPILKAN TIPE DATA SUATU VARIABEL KE LAYAR TERMINAL / OUTPUT
#UNTUK MEMBAHAS LEBIH LANJUT SUATU TIPE DATA, AKAN DI JELASKAN DI BAB TIPEP DATA ITU SENDIRI
# TERIMAKASIH

#datatypes done