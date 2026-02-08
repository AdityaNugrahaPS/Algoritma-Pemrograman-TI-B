#PYTHON STRING

print("Hello, World!") #Contoh string yang menggunakan tanda kutip satu
print('Hello, World!') #Contoh string yang menggunakan tanda kutip dua

a = "Hello, World!" #Memasukkan value string ke dalam variabel a
print(a) #Mencetak string yang sudah dimasukkan valuenya ke dalam variabel a

#SLICING STRING

a = "Hello, World!"
print(a[2:5]) #Memotong karakter string dari posisi ke-2 hingga ke-5 (Posisi ke-5 tidak dihitung)

a = "Hello, World!"
print(a[:5]) #Memotong karakter string dari posisi awal hingga ke-5 (Posisi ke-5 tidak dihitung)

#MODIFY STRING

a = "Hello, World!"
print(a.upper()) #Mengubah semua karakter dalam string menjadi huruf kapital

a = "Hello, World!"
print(a.swapcase()) #Mengubah huruf kecil dalam string menjadi kapital, dan mengubah huruf kapital dalam string menjadi huruf kecil

a = "Hello, World!"
print(a.replace("H", "J")) #Menukar karakter H dalam string menjadi J

#CONCATENATE STRING

a = "Hello"
b = "World"
c = a + b #Menggabungkan kedua value dari variabel a dan b dan memasukkannya ke dalam variabel c
print(c)

#FORMAT STRING

umur = 36
txt = f"Namaku adalah John, Aku {umur} tahun" #Menambahkan f di dalam string untuk memastikan bahwa ini adalah f-string. Serta kurung kurawal sebagai tempat penampung variabel
print(txt)

#ESCAPE CHARACTERS

'''
Kode        Hasil
'                 	Tanda kutip tunggal	
2 backslash      	Garis miring terbalik	
n	                Baris baru	
r	                Kembalikan kursor	
t	                Tab	
b	                Spasi belakang	
f	                Form Feed	
ooo                 Nilai Oktal
xhh	                Nilai Heksadesimal

Note: simbol backslash tidak ditulis untuk mencegah agar tidak terjadi error
'''

#STRING METHODS

'''
capitalize()                    Mengubah karakter pertama menjadi huruf besar
casefold()                      Mengubah string menjadi huruf kecil
center()                        Mengembalikan string yang dipusatkan
count()                         Mengembalikan jumlah kemunculan nilai tertentu dalam sebuah string
encode()                        Mengembalikan versi string yang telah dienkode
endswith()                      Mengembalikan true jika string diakhiri dengan nilai yang ditentukan
expandtabs()                    Mengatur ukuran tab string
find()                          Mencari nilai tertentu dalam string dan mengembalikan posisi di mana nilai tersebut ditemukan
format()                        Memformat nilai tertentu dalam sebuah string
format_map()                    Memformat nilai tertentu dalam sebuah string
index()                         Mencari nilai tertentu dalam string dan mengembalikan posisi di mana nilai tersebut ditemukan
isalnum()                       Mengembalikan True jika semua karakter dalam string adalah alfanumerik
isalpha()                       Mengembalikan True jika semua karakter dalam string adalah alfabet
isascii()                       Mengembalikan True jika semua karakter dalam string adalah karakter ASCII
isdecimal()                     Mengembalikan True jika semua karakter dalam string adalah desimal
isdigit()                       Mengembalikan True jika semua karakter dalam string adalah angka digit
isidentifier()                  Mengembalikan True jika string tersebut adalah pengidentifikasi
islower()                       Mengembalikan True jika semua karakter dalam string adalah huruf kecil
isnumeric()                     Mengembalikan True jika semua karakter dalam string adalah angka
isprintable()                   Mengembalikan True jika semua karakter dalam string dapat dicetak
isspace()                       Mengembalikan True jika semua karakter dalam string adalah spasi
istitle()                       Mengembalikan True jika string tersebut mengikuti aturan judul
isupper()                       Mengembalikan True jika semua karakter dalam string adalah huruf besar
join()                          Menggabungkan elemen-elemen dari iterable ke akhir string
ljust()                         Mengembalikan versi string yang rata kiri
lower()                         Mengonversi string menjadi huruf kecil
lstrip()                        Mengembalikan versi string yang dipangkas kiri
maketrans()                     Mengembalikan tabel terjemahan yang akan digunakan dalam terjemahan
partition()                     Mengembalikan tuple di mana string dibagi menjadi tiga bagian
replace()                       Mengembalikan string di mana nilai tertentu diganti dengan nilai tertentu
rfind()                         Mencari nilai tertentu dalam string dan mengembalikan posisi terakhir di mana nilai tersebut berada ditemukan
rindex()                        Mencari nilai tertentu dalam string dan mengembalikan posisi terakhir di mana nilai tersebut ditemukan
rjust()                         Mengembalikan versi string yang rata kanan
rpartition()                    Mengembalikan tuple di mana string dibagi menjadi tiga bagian
rsplit()                        Membagi string pada pemisah yang ditentukan, dan mengembalikan daftar
rstrip()                        Mengembalikan versi string yang dipangkas kanan
split()                         Membagi string pada pemisah yang ditentukan, dan mengembalikan daftar
splitlines()                    Membagi string pada jeda baris dan mengembalikan daftar
startswith()                    Mengembalikan true jika string dimulai dengan nilai yang ditentukan
strip()                         Mengembalikan versi string yang dipangkas
swapcase()                      Menukar huruf besar/kecil, huruf kecil menjadi huruf besar dan sebaliknya
title()                         Mengubah karakter pertama setiap kata menjadi huruf besar
translate()                     Mengembalikan string yang diterjemahkan
upper()                         Mengubah string menjadi huruf besar
zfill()                         Mengisi string dengan sejumlah nilai 0 yang ditentukan di awal
'''