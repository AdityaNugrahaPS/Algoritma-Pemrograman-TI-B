#python variables
#VARIABLE adalah wadah untuk menyimpan data
namaku = 'rania' #tipe data string, tipe data ini bisa kita menggunakan tanda kutip double (""), atau tanda kutip single ('')
umurSekarang = 18 #tipe data number

print(namaku) #memanggil variabel namaku
print(umurSekarang) #memanggil variabel umurSekarang

#cara penamaan variabel yang benar
nama = 'rania'
nama_mahasiswa = 'rania' #kata di gabung menggunakan _
_nama_mahasiswa = 'rania' #diawali dengan garis bawah
namaMahasiswa = 'rania' #setiap awal kata kecuali kata pertama, huruf besar
NAMAMAHASISWA = 'rania' #semua kata huruf besar
namamahasiswa07 = 'rania' #kata digabung
namaAbsenKe05 = 'rania' #kata digabung dengan kata pertama setiap kata kecuali kata pertama diawali huruf besar

#pengujian menampilkan output ketika variabel di panggil
print(nama)
print(nama_mahasiswa)
print(_nama_mahasiswa)
print(namaMahasiswa)
print(NAMAMAHASISWA)
print(namamahasiswa07)
print(namaAbsenKe05)


#cara penamaan variabel yang salah

#  2nama = 'rania' 
"""ini salah karena ada angka di depannya"""

#nama-mahasiswa = 'rania' 
"""ini salah karena dengan adanya -, mahasiswanya ga ke detect"""

#nama mahasiswa = 'rania' 
"""ini salah karena dalam penamaan variabel dilarang adanya spasi,
 jadi jika katanya terpisah harus digunakan _atau digabung aja"""

"""
VARIABEL di Python tidak perlu di deklarasikan tipe datanya
dan juga tipedata dari variabel itu dapat kita ubah walaupun 
variabel itu sudah memiliki tipe data
"""

#contoh mengubah tipe data suatu variabel
contoh = 'bertipe data string' #awalnya, variabel contoh itu bertipe datang string 
contoh = 123 #lalu saya mengubah contoh dengan mengisikan nilai 123 yang otomatis berubah menjadi number

"python juga mengizinkan kita untuk memasukkan nilai ke dalam beberapa variabel dalam satu baris"

#contoh memasukkan nilai ke dalam beberapa variabel dalam satu baris

x,y,z = 1, 2, 3
print (x) #nilainya 1
print (y) #nilainya 2
print (z) #nilainya 3

#kita juga bisa langsung print ketiga variabel dalam satu baris yang sama
print(x,y,z)
#atau dengan
print(x + y + z) #hanya berlaku untuk yang sesama text saya, kalau sesama number akan menjadi operasi, 

#jika kita menggunakan + pada variabel bertipe data string dan number, akan terjadi error


"python juga mengizinkan kita untuk mengisi variabel dengan nilai yang sama dalam satu baris"
#contoh memasukkan nilai ke dalam beberapa variabel dalamsatu baris

MakananFavorit = favoriteFood = makananKesukaanku = 'Pizza'

print(MakananFavorit)
print(favoriteFood)
print (makananKesukaanku)

"lalu ada yang namanya unpacking"
'''
unpacking adalah memasukkan nilai kolektif seperti list, tuple, dan sebagainya lalu mengekstrak
nilai itu ke dalam variabel
'''

#contoh unpacking

ListMakananKesukaanku = ["Burger", "pizza", "chiken steak"]
makanan1 = ListMakananKesukaanku[0]
makanan2 = ListMakananKesukaanku[1]
makanan3 = ListMakananKesukaanku[2]

semuamakanan = ListMakananKesukaanku

print(semuamakanan)
print(makanan1)
print(makanan2)
print(makanan3)

#BEDA HURUF KAPITAL BISA MEMBUAT SUATU VARIABEL BARU
#contoh: 
universitas = "Universitas Riau"
UNIVERSITAS = "UNIVERSITAS RIAU"

'''
walau hanya berbeda kapital, variabel yang diatas adalah variabel yang berbeda
variabel universitas dan UNIVERSITAS
'''


#GLOBAL VARIABLES
"""
Variabel global dapat digunakan oleh siapa saja, baik di dalam fungsi maupun di luar fungsi
menggunakan kata kunci 'var'
"""
#contoh
def contohglobal():
  global kata
  kata = "HALOOOO"

contohglobal()

print("Bilang " + kata)

#gunakan global kata kunci jika ingin mengubah variabel global di dalam sebuah fungsi.
#contoh
namanya = "ga ada"

def myfriend():
  global namanya
  namanya = "fildza"

myfriend()

print("aku dan " + namanya)

#DONE VARIABLE

