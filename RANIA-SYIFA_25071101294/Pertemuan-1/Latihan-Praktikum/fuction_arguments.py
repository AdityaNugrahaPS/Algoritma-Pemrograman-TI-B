#FUNCTION PYTHON
""" 
apa itu fungsi?
fungsi akan berjalan ketika dipanggil
nah fungsi akan mengembalikan data sebagai hasil
adanya fungsi untuk menghindari pengulangan pada kode
"""

"CARA MEMBUAT FUNGSI"
#kata kunci 'def'
#contoh
def contohfungsi ():
    print("INI CONTOH DARI FUNGSI")

'kita membuat sebuah fungsi bernama "contohfungsi" yang akan mencetak "INI CONTOH DARI FUNGSI"'

"CARA MEMANGGIL FUNGSI"
def contohfungsi (): 
    print("INI CONTOH DARI FUNGSI")
contohfungsi() #tuliskan nama fungsinya, diikuti oleh tanda kurung
#kita bisa memanggil fungsi berkali kali

"ATURAN PENAMAAN FUNGSI"
'''
Aturannya sama dengan aturan penamaan untuk variabel, yaitu :
- Nama fungsi harus diawali dengan huruf atau garis bawah.
- Nama fungsi hanya boleh berisi huruf, angka, dan garis bawah.
- Nama fungsi peka terhadap huruf besar dan kecil ( Rania() dan rania() berbeda)
'''

"CONTOH PENGGUNAKAN FUNGSI"
def konversifahrenheit(fahrenheit):
  return (fahrenheit - 32) * 5 / 9 #fungsi 'return' program akan berhenti mengeksekusi dan mengirimkan hasilnya kembali, jika sudah mencapai return

print(konversifahrenheit(77))
print(konversifahrenheit(95))
print(konversifahrenheit(50))

#kita tidak perlu membuat ulang kode satu persatu berkat adanya fungsi

"PASS PADA FUNGSI"
'''
fungsi tidak boleh kosong, jika kita membutuhkan placeholder fungsi tanpa kode apa pun, gunakan 'pass'
'''
#contoh:
def contohfungsi():
   pass

"ARGUMEN PADA FUNGSI"
'''
argumen digunakan untuk dipanggil sebagai informasi, letak argumen terletak di dalam tanda kurung setelah nama fungsi
'''
#contoh
def contohfungsi2(nama): # 'nama' itu adalah argumen
   pass

"MEMBANDINGKAN PARAMETER DENGAN ARGUMEN PADA FUNGSI"
'''
Parameter adalah variabel yang tercantum di dalam tanda kurung pada definisi fungsi .

Argumen adalah nilai sebenarnya yang dikirim ke fungsi saat fungsi tersebut dipanggil .
'''
#contoh
def contohfungsi3(nama): # name is a parameter
  print("Hello", nama)

contohfungsi3("Rania") # "Emil" is an argument

"JUMLAH ARGUMEN PADA FUNGSI"
'''
kita bisa membuat 2 argumen, itu juga secara default yaa
'''
#contoh
def contohfungsi4 (nama1, nama2): #karena ada dua 
   print(nama1 + "" + nama2)
contohfungsi4("Rania", "Fildza") #maka harus ada dua juga
contohfungsi4("Najwa", "Salwa")

"NILAI PARAMETER DEFAULT PADA FUNGSI"
'''
kita juga dapat menetapkan nilai default untuk parameter. 
Jika fungsi dipanggil tanpa argumen, fungsi tersebut akan menggunakan nilai default
'''
#contoh
def contohfungsi5 (nama = "teman"):
   print("hello, nama temanku ", nama)
   contohfungsi5("fildza")
   contohfungsi5("najwa")
   contohfungsi5("salwa")
   contohfungsi5("syifa")
   contohfungsi5("masih banyak lagi")


"KEYWORD ARGUMEN PADA FUNGSI"
'''
kita juga dapat mengirim argumen dengan sintaks key = value
'''
#contoh
def contohfungsi6 (namaku, namtemanku):
  print("halo, namaku ", namaku)
  print("namaku", namaku + " dan nama temanku", namtemanku)

contohfungsi6(namaku = "rania", namtemanku = "fildza")

"ARGUMEN POSISIONAL PADA FUNGSI"
'''
kita juga bisa memanggil argumen tanpa kata kunci, asalkan penempatan argumennya benar
'''
#contoh
def contohfungsi7 (namaku, namtemanku):
  print("halo, namaku ", namaku)
  print("namaku", namaku + " dan nama temanku", namtemanku)

contohfungsi7( "rania", "fildza") #tidak ada dipanggil dengan kata kunci

"MENCAMPUR ARGUMEN POSISIONAL DAN KEYWORD ARGUMENT PADA FUNGSI"
'''
nah kita bisa menggabungkan, maksudnya ada yang dipanggil dengan kata kunci, ada yang tidak
'''
#contoh
def contohfungsi8 (namaku, namtemanku, umur):
  print("halo, namaku ", namaku)
  print("namaku", namaku + " dan nama temanku", namtemanku + "kami berumur ", umur)

contohfungsi8 ("rania", "fildza", umur = 19)

"MENERUSKAN BERBAGAI TIPE DATA PADA FUNGSI"
'''
kita juga dapat mengirimkan tipe data apa pun sebagai argumen ke suatu fungsi 
'''
#contoh
def contohfungsi9(teman):
  for teman in teman:
    print(teman)

temanku = ["fildza", "najwa", "salwa", "syifa", 'farah', 'naura', 'dan banyak lainnya']
contohfungsi9(temanku)

"NILAI KEMBALIAN PADA FUNGSI"
'''
Fungsi dapat mengembalikan nilai menggunakan 'return' pernyataan
'''
#contoh
def contohfungsi10(x, y):
  return x * y

hasil = contohfungsi10(12, 6)
print(hasil)

"MENGEMBALIKAN TIPE DATA YANG BERBEDA PADA FUNGSI"
'''
Fungsi dapat mengembalikan tipe data apa pun, termasuk daftar, tuple, kamus, dan banyak lagi.
'''
#contoh
def contohfungsi11():
  return ["fildza", "najwa", "salwa", "syifa", 'farah', 'naura', 'dan banyak lainnya']

teman = contohfungsi10()
print(teman[0])
print(teman[1])
print(teman[2])

"ARGUMEN HANYA BERDASARKAN POSISI PADA FUNGSI"
'''
kita juga dapat menentukan bahwa suatu fungsi HANYA dapat memiliki argumen posisional.

Untuk menentukan argumen hanya berdasarkan posisi, tambahkan , /setelah argumen
'''
#contoh
def contohfungsi11(nama, /):
  print("Halo, Namaku ", nama)

contohfungsi11("Rania")

"KEYWORD ARGUMEN KHUSUS PADA FUNGSI"
'''
Untuk menentukan bahwa suatu fungsi hanya dapat memiliki argumen kata kunci, 
tambahkan *, sebelum argumen
'''
#contoh
def contohfungsi12(*, nama):
  print("Halo, Namaku", nama)

contohfungsi12(nama = "Rania")

'''
Tanpa *,, Anda diperbolehkan menggunakan argumen posisi meskipun 
fungsi tersebut mengharapkan argumen kata kunci
'''
#contoh
def contohfungsi13(nama):
  print("Halo, Namaku ", nama)

contohfungsi13("Rania")

"MENGGABUNGKAN PERCARIAN BERDASARKAN POSISI SAJA DAN PENCARIAN BERDASARKAN KEYWORD SAJA PADA FUNGSI"
'''
kita juga dapat menggabungkan kedua tipe argumen dalam fungsi yang sama.
Argumen sebelum /hanya berupa argumen posisional, dan argumen setelah *hanya berupa argumen kata kunci
'''
#contoh
def contohfungsi14(a, b, /, *, c, d):
  return a + b - c * d

hasil = contohfungsi14(14, 5, c = 43, d =98)
print(hasil)

#FUNCTION DONE