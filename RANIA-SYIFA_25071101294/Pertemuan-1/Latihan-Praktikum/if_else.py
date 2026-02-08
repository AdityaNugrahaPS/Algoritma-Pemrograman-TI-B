#if else
""" 
Pernyataan if mengevaluasi suatu kondisi (ekspresi yang menghasilkan True atau False ). 
Jika kondisinya benar, blok kode di dalam pernyataan if akan dieksekusi. 
Jika kondisinya salah, blok kode akan dilewati.
"""
#kata kunci untuk mengevaluasi kondisi adalah if
#contoh
contohif1 = 35

if contohif1 < 40 :
    print("angka lebih kecil") #karena 35 lebih kecil dari pada 40, maka hasilnya True dan akan mengeksekusi aksi.
#kenapa kata print ada di tengah, bukan sejajar dengan if?
#karena adanya indentasi, atau spasi di awal baris, jika tidak ada indentasi, maka akan terjadi error

"Kita juga bisa membuat beberapa pernyataan dalam blok if, dengan syarat indentasinya sama"
#contoh

if contohif1 == 35:
    print("ini akan ditampilkan di output")
    print("ini juga akan ditampilkan")
    print('walau dengan tanda kutip satu, tidak akan ada error')

"variabel boolean juga dapat di pakai dalam pernyataan if walau ttanpa operator perbandingan"

contohif2 = True
if contohif2 :
    print('ini akan ditampilkan pada layar')

"""
Python dapat mengevaluasi True atau False dalam pernyataan if
semua kecuali inputan kosong, akan dievaluasi sebagai False, selain itu akan di evaluasi sebagai True.
"""

"PYTHON ELIF"
#akan digunakan dengan kata kunci "elif" ketika ada jika satu kondisi tidak terpenuhi, maka evaluasi kondisi kedua

contohelif1 = 8
contohelif2 = 10

if contohelif1 > contohelif2 :
    print("lebih besar")
elif contohelif1 < contohelif2:
    print("lebih kecil")

#dalam contoh diatas, karena 8 lebih kecil dari pada 10, maka yang aka di eksekusi adalah 8 < 10
#maka output yang akan di tampilkan adalah "lebih kecil"

'beberapa pernyataan elif'
"kita bisa membuat beberapa kondisi, lalu python akan mengeksekusi kondisi pertama yang bernilia True."
#contoh

nilaisaya = 99

if nilaisaya == 100:
    print("nilai A")
elif nilaisaya <= 99:
    print ("nilai B")
elif nilaisaya <=89:
    print("nilai B")
elif nilaisaya <= 79:
    print("nilai C")
elif nilaisaya <= 69:
    print("nilai D")
elif nilaisaya <=59:
    print("nilai E")

'karenna nilaisaya nilainya 99, maka kondisi kedua yaitu "nilai B", yang akan di eksekusi, dan ditampilkan ke layar'

"kita juga bisa membuat dua aksi dalam satu kondisi"
#kaca kunci yang kita gunakan adalah "else"
#contoh

contohelse1 = 54
contohelse2 = 98

if contohelse1 == contohelif2 :
    print("nilai sama")
elif contohelse1 > contohelse2:
    print("lebih besar")
else:
    print("lebih kecil")

'karena 54 lebih kecil dari 94, maka aksi yang akan di eksekusi adalah "lebih kecil".'

#kita bisa hanya memakai if dan else
if contohelse1 > contohelse2 :
    print("lebih besar")
else:
    print("lebih kecil")

'karena 54 lebih kecil dari 94, maka aksi yang akan di eksekusi adalah "lebih kecil".'

"kita juga bisa membuat if dan aksi dalam satu baris"
#contoh
if contohelse1 < contohelse2 : print("lebih kecil") #jangan lupa untuk tanda : yaa

"kita juga bisa meletakkan pernyataan untuk if dan pernyataan untuk else dalam satu baris"
#contoh
print("lebih besar") if contohelse2 > contohelse1 else print("lebih kecil")
'Ini disebut ekspresi kondisional (kadang-kadang dikenal sebagai "operator ternary")'

'''kita juga bisa menggunakan garis tunggal if/ else 
untuk memilih nilai dan menetapkannya ke variabel'''
#contoh
angka1 = 39
angka2 = 10

hurufgede = angka1 if angka1 > angka2 else angka2
print("angka yang terbesar adalah ",hurufgede)
'''
penjelasan kode:
nilai dari hurufgede akan diisi dengan nilai yang ada di variabel angka1 jika
angka1 lebih besar daripada angka2, namun jika tidak
nilai dari hurufgede akan diisi dengan nilai yang ada di variabel angka2
'''

"kita juga bisa membuat beberapa kondisi dalam satu baris"
#contoh
print("Sama") if angka1 == angka2 else print('lebih besar') if angka1 > angka2 else print("lebih kecil")
'''
penjelasan kode:
output akan menampilkan "Sama" jika nilai yang ada didalam variabel angka1 sama dengan yang ada di dalam variabel angka2,
output akan menampilkan "lebih besar" jika nilai yang ada didalam variabel angka1 lebih besar nilainya dari pada variabel angka2
output akan menampilkan "lebih kecil" jika nilai yang ada didalam variabel angka1 lebih kecil nilainya dari pada variabel angka2
'''

"PENGGUNAAN IF ELSE PADA OPERASI LOGIKA"
'''
ada tiga operator logika, yaitu:
and - Mengembalikan True jika kedua pernyataan tersebut benar
or  - Mengembalikan True jika salah satu pernyataan benar
not - Membalikkan hasilnya, mengembalikan False jika hasilnya benar
'''
#contoh
#1. operator dan (and)
    #kata kunci (and)
'''
kita akan gunakan untuk menggabungkan pernyataan kondisional.
dengan syarat kedua kondisi harus benar agar seluruh ekspresi menjadi benar (True).
'''
#contoh
contohand1 = 90
contohand2 = 80
contohand3 = 192

if contohand1 > contohand2 and contohand3 > contohand1 :
    print("Hasil benar") #ini hasil jika kondisinya terbukti True

#2. operator atau (or)
    #kata kunci (or)
'''
kita akan gunakan untuk menggabungkan pernyataan kondisional.
dengan syarat salah satu kondisi harus benar agar seluruh ekspresi menjadi benar (True).
'''
if contohand1 > contohand2 or contohand3 > contohand1 :
    print("OKE") #ini hasil jika kondisinya terbukti F

#3 operator negasi (not)
    #kata kunci (not)
'''
fungsi dari not adalah untuk membalikkan hasil dari pernyataan kondisional.
'''

if not contohand1 < contohand2 :
    print("ini bentuk negasi") #membalikkan nilai kebenaran

"kita dapat menggabungkan beberapa operator dalam satu pernyataan"

Angka = 25
Status = False
Kode = True

if (Angka < 20 or Angka > 89) and not Status or Kode: #gunakan tanda kurung untuk memperjelas maksud Anda dan mengontrol urutan evaluasi.
  print("INI AKAN MUNCUL YAAAAA")

"KITA DAPAT MENGGUNAKAN IF DIDALAM IF"
#contoh
contohifif1 = 50

if contohifif1 > 17:
  print("1")
  if contohifif1 > 38:
    print("2")
  else:
    print("3")

"KITA BISA MEMBUAT BEBERAPA TINGKATAN"
NILAIMU = 85
KKM = 80
STATUS = True

if NILAIMU >= 60:
  if KKM >= 80:
    if STATUS:
      print("BAGUS")
    else:
      print("BAIK")
  else:
    print("CUKUP")
else:
  print("ULANG")

"kita bisa menggunakan if tingkat ini dengan operator logika"
NILAI = 80
STATUSMHS = True

if NILAI > 60 and STATUSMHS:
  print("LULUS")

"kita bisa menggunakan if untuk pernyataan lulus atau tidak"
#kata kunci (pass)
'''
pass adalah operasi null - tidak ada yang terjadi saat dieksekusi. 
Pernyataan ini berfungsi sebagai placeholder.
'''
a = 49
b = 3922

if b > a:
  pass

"""
Pernyataan `pass` memungkinkan Anda melakukan ini tanpa kesalahan sintaks.
"""
contohpass1 = 30

if contohpass1 < 34:
  pass
else:
  print("hallo")

"perbedaan pass vs comment"

"""
comment  - comment diabaikan oleh Python
pass     - pernyataan yang dieksekusi walau tidak melakukan apapun
"""

"pass dalam beberapa kondisi"
contohpass2 = 50

if contohpass2 < 0:
  print("Hallo")
elif contohpass2 == 0:
  pass #tidak ada aksi
else:
  print("Hello")

"pass dalam konteks lain"
#pass bisa kita lakukan dalam perulangan, fungsi, dan class.
def Kelas(Tingkat):
  pass

#IF ELSE DONE