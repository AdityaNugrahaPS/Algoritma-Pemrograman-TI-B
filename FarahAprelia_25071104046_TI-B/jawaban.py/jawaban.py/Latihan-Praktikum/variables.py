#VARIABLE NAMES

'''
Berikut adalah beberapa cara penamaan variabel yang tepat:

namasaya = 'farah' #Nama variabel menggunakan huruf kecil semua
kelas_saya = 'ti b' #Nama variabel menggunakan underscore sebagai pengganti spasi
_nim_saya = 25071104046 #Nama variabel menggunakan underscore di awal
prodiSaya = 'teknik informatika' #Nama variabel menggunakan huruf kapital sebagai penanda pergantian kata
UMURSAYA = 19 #Nama variabel menggunakan huruf kapital semua
jurusansaya5 = 'teknik elektro' #Nama variabel menggunakan angka di akhir

Contoh penamaan variabel yang salah:

2nama = 'farah' #Nama variabel menggunakan angka di awal
kelas-saya = 'ti b' #Nama variabel menggunakan strip sebagai pengganti spasi
nim saya = 25071104046 #Nama variabel menggunakan spasi
'''

#ASSIGN MULTIPLE VARIABLES

a, b, C = "Kakak", "Adik", "Sepupu" #Mendeklarasikan tiga variabel secara singkat
print(a)
print(b)
print(C)

keluarga = ["kakak", "adik", "sepupu"] #Menyatukan tiga value dalam string bernama keluarga
a, b, C = keluarga #Kemudian memberi nama string keluarga menjadi a, b dan c
print(a)
print(b)
print(C)

#OUTPUT VARIABLES

a = "Slipknot sangat keren!" #Variabel a berisi text yang akan menjadi output nantinya
print(a)

a = 45
b = 80
print(a + b) #Secara otomatis menjumlahkan kedua value yang terdapat di dalam dua variabel

#GLOBAL VARIABLES

a = "keren" #Ini adalah variabel global, variabel global dapat diubah dengan menggunakan keyword 'global'

def func(): #Ini adalah definisi fungsi yang bernama func
  print("Korn itu sangat " + a) #Berisi fungsi dan variabel global

func() #Digunakan untuk memanggil fungsi untuk dijalankan