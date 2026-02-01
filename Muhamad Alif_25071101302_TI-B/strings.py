# python string
'''
string dapat dituliskan dalam beberapa cara
'''

# 1 perkata
print ('hello')

# 2 perkalimat
print('orang baik')
print('senantiasa dipermuda kan jalan hidupnya')

# 3 variable
a = 'aku ora wong suge'
print(a)

# 4 multiline 
a = '''sak tenane aku tresno karo 
dekne tapi aku seng kudu sadar diri'''
print(a)

# 5 strings arrays
a = 'satu dua tiga'
print(a[1]) # berawal dari indeks 0

# 6 string looping
for x in 'mahato':
    print(x)

# 7 string length
a = 'I Love You'
print(len(a)) # spasi termasuk hitungan

# 8 check strings
# mengecek strings apakah terdapat didalam suatu variable 
# yes
a = 'ikan paus adalah mamalia'
print('a'in a) # Output True/False

# dapat digunakan di if else
a = 'ikan paus adalah mamalia'
if 'paus' in a:
    print('kata itu benaran ada')

# not
a = 'ikan paus adalah mamalia'
print('harimau'not in a) # Output True/False

# dapat digunakan di if else
a = 'ikan paus adalah mamalia'
if 'malaya' not in a:
    print('kata itu benaran tidak ada')

 # slicing strings
a = 'kamu ayu'
print(a[1:3]) # output = indek 1 dan 2

# versi perkata
a = 'kamu ayu'
print(a[:4]) # tulis sammpe indeks ke 3

# huruf yang dihilangkan di awal kalimat/kata
a = 'kamu ayu'
print(a[2:])

# negative
# menghilangkan huruf dari sisi kanan ke kiri
a = 'kamu ayu'
print(a[-5:-2])

# Modify strings
# upper case
a = 'aku ra ganteng'
print(a.upper()) # merubah kalimat kecil menjadi kalimat besar

# Lower case
a = 'AKU RA GANTENG'
print(a.lower())

# remove whitespace
a = ' aku ra ganteng '
print(a.strip()) # menghapus spasi yang kosong

# replace strings
a = 'aku ra ganteng'
print(a.replace('aku','kamu')) # merubah string 

# split strings
a = 'aku ra ganteng'
print(a.split()) # membagi string menjadi substring dengan tanda bisa berupa spasi atau apa pun itu

# String Concatenation
a = 'aku'
b = 'kamu'
c = a + b
print(c) # menambah string

a = 'aku'
b = 'kamu'
c = a +' '+ b
print(c) # menambahkan spasi

# format string
# kita tidak dapat menggabungkan angka dan string seperti ini
# age = 36
# #This will produce an error:
# txt = "My name is John, I am " + age
# print(txt)

# yes
umur = 18
a = f'nama saya alif, umur saya {umur}'
print(a)

umur = 18
a = f'nama saya alif, umur saya {umur:.1f}' # float
print(a)

umur = 18
a = f'nama saya alif, umur saya {umur + 2}' # oprasi aritmatika
print(a)

# Escape character
'''
\'	kutipan tunggal	
\\	garis miring terbalik	
\n	jalur baru	
\r	Pengembalian Kereta	
\t	Tab	
\b	Ruang belakang	
\f	Formulir Umpan	
\ooo	Nilai oktal
\xhh	Nilai hex
'''
print('aku\'kamu')
print('aku \\ kamu')
print('aku \nkamu')
print('aku \rkamu')
print('aku \tkamu')
print('aku \bkamu')
print('aku \fkamu')
#hello
# a = "\110\145\154\154\157"
# print(a) 
# txt = "\x48\x65\x6c\x6c\x6f"
# print(txt) 

# String Methods
'''
capitalize()	Mengubah karakter pertama menjadi huruf besar.
casefold()	    Mengubah string menjadi huruf kecil.
center()	    Mengembalikan string yang berpusat
count()	        Mengembalikan jumlah berapa kali nilai tertentu muncul dalam sebuah string.
encode()	    Mengembalikan versi string yang telah dienkode.
endswith()	    Mengembalikan nilai true jika string diakhiri dengan nilai yang ditentukan.
expandtabs()	Mengatur ukuran tab pada string.
find()	        Mencari nilai tertentu dalam string dan mengembalikan posisi di mana nilai tersebut ditemukan.
format()	    Memformat nilai-nilai tertentu dalam sebuah string.
format_map()	Memformat nilai-nilai tertentu dalam sebuah string.
index()	        Mencari nilai tertentu dalam string dan mengembalikan posisi di mana nilai tersebut ditemukan.
isalnum()	    Mengembalikan nilai True jika semua karakter dalam string adalah alfanumerik.
isalpha()	    Mengembalikan True jika semua karakter dalam string adalah karakter dalam alfabet.
isascii()	    Mengembalikan True jika semua karakter dalam string adalah karakter ASCII.
isdecimal()	    Mengembalikan True jika semua karakter dalam string adalah angka desimal.
isdigit()	    Mengembalikan True jika semua karakter dalam string adalah angka.
isidentifier()	Mengembalikan nilai True jika string tersebut adalah pengidentifikasi.
islower()	    Mengembalikan nilai True jika semua karakter dalam string adalah huruf kecil.
isnumeric()	    Mengembalikan nilai True jika semua karakter dalam string adalah angka.
isprintable()	Mengembalikan True jika semua karakter dalam string dapat dicetak.
isspace()	    Mengembalikan nilai True jika semua karakter dalam string adalah spasi.
istitle()	    Mengembalikan nilai True jika string tersebut mengikuti aturan sebuah judul.
isupper()	    Mengembalikan nilai True jika semua karakter dalam string adalah huruf besar.
join()	        Menggabungkan elemen-elemen dari sebuah iterable ke akhir string.
ljust()	        Mengembalikan versi string yang rata kiri.
lower()	        Mengubah string menjadi huruf kecil.
lstrip()	    Mengembalikan versi string yang dipangkas dari sisi kiri.
maketrans()	    Mengembalikan tabel terjemahan yang akan digunakan dalam penerjemahan.
partition()	    Mengembalikan tuple di mana string dibagi menjadi tiga bagian.
replace()	    Mengembalikan string di mana nilai yang ditentukan diganti dengan nilai yang ditentukan.
rfind()	        Mencari nilai tertentu dalam string dan mengembalikan posisi terakhir di mana nilai tersebut ditemukan.
rindex()	    Mencari nilai tertentu dalam string dan mengembalikan posisi terakhir di mana nilai tersebut ditemukan.
rjust()	        Mengembalikan versi string yang rata kanan.
rpartition()	Mengembalikan tuple di mana string dibagi menjadi tiga bagian.
rsplit()	    Memisahkan string berdasarkan pemisah yang ditentukan, dan mengembalikan sebuah daftar.
rstrip()	    Mengembalikan versi string yang dipangkas ke kanan.
split()	        Memisahkan string berdasarkan pemisah yang ditentukan, dan mengembalikan sebuah daftar.
splitlines()	Memisahkan string berdasarkan jeda baris dan mengembalikan sebuah daftar.
startswith()	Mengembalikan nilai true jika string diawali dengan nilai yang ditentukan.
strip()	        Mengembalikan versi string yang telah dipangkas.
swapcase()	    Huruf besar dan kecil ditukar posisinya, huruf kecil menjadi huruf besar dan sebaliknya.
title()	        Mengubah karakter pertama setiap kata menjadi huruf besar.
translate()	    Mengembalikan string yang telah diterjemahkan
upper()	        Mengubah string menjadi huruf besar.
zfill()	        Mengisi string dengan sejumlah nilai 0 yang ditentukan di bagian awal.
'''