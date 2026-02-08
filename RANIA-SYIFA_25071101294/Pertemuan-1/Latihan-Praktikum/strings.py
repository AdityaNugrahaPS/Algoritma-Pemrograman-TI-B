# String pada Bahasa Pemprograman Python, diapit oleh tanda kutip dua ("") atau tanda kutip satu ('')
#contoh

contohstring1 = "Halooo"
contohstring2 = 'Halooo'
'kedua variabel ini bertipe data string karena adanya tanda kutip tersebut'

#kita bisa menampilakn teks ke tampilan dengan memberikan perintah print()
print(contohstring1)
print(contohstring2)

"""
kita juga bisa menggunakan tanda kutip di dalam tanda kutip, 
dengan syarat tanda kutip yang ada di dalam tidak sama dengan tanda kutip yang di awal
"""

#contoh
contohstring3 = "guys, nama ku 'Rania'" #nah kayak gini
contohstring4 = 'kalau gini juga "bisa"' #atau kayak gini
print(contohstring3)
print(contohstring4)

'''
kita juga bisa melakukan multiline string dengan cara triple tanda kutip dan memasukkannya
kedalam sebuah variabel
'''

contohstring5 = '''nah kalau gini
kita bisa buat
menjadi beberapa baris'''
print(contohstring5)

#STRING ADALAH ARRAY
'''dalam Python, satu karakter yang ada dalam string itu berada dalam satu indeks
jadi dihitung dari indeks[0]'''

#contoh
contohstring6 = "namaku rania"
print(contohstring6[3])
#karena kita meminta untuk menampilkan indeks[3], maka yang akan tampil adalah "a"

#KITA JUGA DAPAT MELAKUKAN PERULANGAN MELALUI STRING
"""dengan memanfaatkan fakta bahwa string itu adalah array,
kita bisa melakukan perulangan menggunakan seuah for loop"""

#contoh
for contohkonver7 in "Rania" :
    print(contohkonver7)
# ini akan melakukan perulangan dengan menggunakan nilai dari variabel "contohkkonver7"

#ADA JUGA NAMANYA STRING LENGTH
'''ini berfungsi untuk mengetahui panjang dari string
gunakan fungsi len()
'''
#contoh
contohkonversi8 = "Namaku Rania"

print(len(contohkonversi8))

#KITA JUGA BISA MENGECHECK APAKAH ADA KARAKTER INI DALAM STRING KITA
'''untuk mencari suatu karakter dalam string yang kita buat, 
kita perlu memasukkan kata kunci in'''

#contoh
contohkonversi9 = "HALO SEMUANYA, NAMA AKU RANIA SYIFA DARI KELAS TEKNIK INFORMATIKA B"
print("RANIA" in contohkonversi9)

#kita juga bisa melakukan suatu kondisi menggunakan kata kunci if

contohkonversi10 = "Namaku Rania"
if "Rania" in contohkonversi10:
    print("Kelas Teknik Informatika")

#berikut contoh jika ternyata tidak ada karakter tersebut dalam string

contohkonver11 = "coba coba"
print("nama" not in contohkonver11)
#gunakan if untuk membuat suatu aksi

if "main" not in contohkonver11:
    print("salah salah")

#KITA MASUK KE MATERI SLICING YUK
'''
slicing adalah memotong string yang telah ada, gimana tu?
kita tentukan indeks awal dan indeks akhir, yang diantara itu ada titik dua :
untuk mendapatkan suatu string

ingat, indeks itu dimulai dari 0
'''
#contoh

contohslicing1 = "ini teksnya sengaja di panjangkan yaa"
print(contohslicing1[3:10])

'kita juga bisa menghapus indeks yang awal saja'
print(contohslicing1[:10])

'kita jugabisa menghilangkan indeks yang terakhir'
print(contohslicing1[4:])

'kita bisa menggunakan indeks negatif untuk memulai pemotongannya dari akhir'
print(contohslicing1[-7:-5])

#KITA JUGA MENGUBAH HURUF YANG ADA DI STRING MENJADI HURUF BESAR ATAUPUN KECIL

#mengubah menjadi huruf besar
'menggunakan kata kunci upper()'
contohkata = "ini akan diubah"
print(contohkata.upper())

#mengubah menjadi huruf kecil
'menggunakan kata kunci lower()'
print(contohkata.lower())

#kita juga bisa menghapus spasi kosong yang ada di awal dan akhir string
'menggunakan kata kunci strip()'
print(contohkata.strip())

#kita juga bisa mengubha string menjadi string yang lain
'menggunakan kata kunci replace()'
print(contohkata.replace("k", "W"))

#kita juga bisa memisahkan string menjadi substring jika menemukan kemunculan yang di buat menjadi pemisah
'menggunakan kata kunci split()'
print(contohkata.split("n"))

#kita juga bisa menggabungkan dua string menjadi satu string
kata1 = "ini"
kata2 = "adalah"
kata3 = "gabungan"

variabelKumpul = kata1 + kata2 + kata3
print(variabelKumpul)

#jika ingin ada spasi, tambahkan " "

variabelSpasi = kata1 + " " + kata2 + " " + kata3
print(variabelSpasi)

#kita dapat menggabungkan string dan angka dengan
'Menggunakan f-string atau format()'
contohumur = 20
print(f"halu nama saya rania syifa, saya berumur {contohumur}")

contohdesimal = 3.9
print(f"ipk saya {contohdesimal:.2f}")

#kita juga bisa melakukan operasi aritmatika
contohtambah = f"ini ya coba {90 + 200}"
print(contohtambah)

#kita juga bisa menyisipkan karakter yang tidak sah menggunakan karakter escape
'menggunakan "\"'

#BERIKUT KUMPULAN KARAKTER ESCAPE YANG ADA DI PYTHON

print("hello\'")
print("hello\\")
print("hello\n haii")
print("hello\r haii")
print("hello\t haii")
print("hello\b haii")
print("hello\f haii")

#BEBERAPA KATA KUNCI YANG DAPAT DIGUNAKAN DI PYTHON PADA STRING
"""
capitalize()	Converts the first character to upper case
casefold()  	Converts string into lower case
center()    	Returns a centered string
count()	        Returns the number of times a specified value occurs in a string
encode()    	Returns an encoded version of the string
endswith()  	Returns true if the string ends with the specified value
expandtabs()	Sets the tab size of the string
find()	        Searches the string for a specified value and returns the position of where it was found
format()	    Formats specified values in a string
format_map()	Formats specified values in a string
index()	        Searches the string for a specified value and returns the position of where it was found
isalnum()	    Returns True if all characters in the string are alphanumeric
isalpha()	    Returns True if all characters in the string are in the alphabet
isascii()	    Returns True if all characters in the string are ascii characters
isdecimal() 	Returns True if all characters in the string are decimals
isdigit()	    Returns True if all characters in the string are digits
isidentifier()	Returns True if the string is an identifier
islower()	    Returns True if all characters in the string are lower case
isnumeric() 	Returns True if all characters in the string are numeric
isprintable()	Returns True if all characters in the string are printable
isspace()	    Returns True if all characters in the string are whitespaces
istitle()	    Returns True if the string follows the rules of a title
isupper()	    Returns True if all characters in the string are upper case
join()      	Joins the elements of an iterable to the end of the string
ljust()	        Returns a left justified version of the string
lower()	        Converts a string into lower case
lstrip()	    Returns a left trim version of the string
maketrans()	    Returns a translation table to be used in translations
partition()	    Returns a tuple where the string is parted into three parts
replace()	    Returns a string where a specified value is replaced with a specified value
rfind()	        Searches the string for a specified value and returns the last position of where it was found
rindex()	    Searches the string for a specified value and returns the last position of where it was found
rjust()	        Returns a right justified version of the string
rpartition()	Returns a tuple where the string is parted into three parts
rsplit()	    Splits the string at the specified separator, and returns a list
rstrip()	    Returns a right trim version of the string
split()     	Splits the string at the specified separator, and returns a list
splitlines()	Splits the string at line breaks and returns a list
startswith()	Returns true if the string starts with the specified value
strip()     	Returns a trimmed version of the string
swapcase()	    Swaps cases, lower case becomes upper case and vice versa
title()	        Converts the first character of each word to upper case
translate()	    Returns a translated string
upper()	        Converts a string into upper case
"""

#String Done