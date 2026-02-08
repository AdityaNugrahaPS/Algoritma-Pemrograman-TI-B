#FOR LOOP
""" 
pengulangan for digunakan untuk mengulang suatu urutan
kita dapat mengeksekusi serangkaian pernyataan,
satu kali untuk setiap item dalam daftar, tuple, set, dan lain sebagainya.
"""
#contoh 
'mencetak nama nama teman rania'
namarania = ["fildza", 'najwa', 'naura', 'salwa','syifa','farah']
for x in namarania:
    print(x)
'Perulangan for tidak memerlukan variabel pengindeksan yang harus diatur sebelumnya.'

"kita bisa melakukan perulangan melalui sebuah string"

for x in "rania":
    print(x)

"pernyataan jeda"
#kata kunci `break` ,
#kita dapat menghentikan perulangan sebelum selesai memproses semua item

#contoh
namarania = ["fildza", 'najwa', 'naura', 'salwa','syifa','farah']
for x in namarania:
    print(x)
    if x == 'naura':
        break
print("PEMBATAS UNTUK CONTOH PERNYATAAN LANJUTAN")
"pernyataan lanjutan"
#kata kunci 'continue'
#kita dapat menghentikan iterasi loop saat ini dan melanjutkan ke iterasi berikutnya

#contoh
namarania = ["fildza", 'najwa', 'naura', 'salwa','syifa','farah']
for x in namarania:
    if x == 'naura':
        continue
    print(x)

"fungsi range"
#kata kunci 'range()'
'''
mengembalikan serangkaian angka, dimulai dari 0 secara default 
dan bertambah 1 (secara default), dan berakhir pada angka yang ditentukan.
'''

#contoh
for x in range(10): #mencetak dari 0 - 9
  print(x)

for x in range(2,15): #menggunakan parameter awal, artinya mencetak 2 hingga 14
  print(x)

"""
Fungsi ini range()secara default akan menambah nilai urutan sebanyak 1, 
namun dimungkinkan untuk menentukan nilai penambahan dengan menambahkan parameter ketiga
"""

#contoh
for x in range(10, 20, 30):
  print(x)

"pernyataan else dalam for loop"
'''
Kata else kunci `in` dalam sebuah forperulangan menentukan blok kode yang akan dieksekusi ketika perulangan selesai
'''
#contoh
"""
Cetak semua angka dari 0 hingga 5, dan cetak pesan ketika perulangan telah berakhir:
"""

for x in range(5):
  print(x)
else:
  print("ALHAMDULILLAH")

  #CATATAN : Blok ini else TIDAK akan dieksekusi jika perulangan dihentikan oleh sebuah breakpernyataan.

"""
Hentikan perulangan saat x nilainya 3, dan lihat apa yang terjadi dengan else blok tersebut
"""
for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

"pernyataan pass"
'''
forLoop tidak boleh kosong, 
tetapi jika karena suatu alasan Anda memiliki forloop tanpa isi, 
tambahkan passpernyataan tersebut untuk menghindari kesalahan.
'''

#contoh
for x in [0, 1, 2]:
  pass