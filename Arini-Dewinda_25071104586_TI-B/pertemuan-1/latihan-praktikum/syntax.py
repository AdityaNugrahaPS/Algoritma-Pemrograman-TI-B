#syntax

"""
Pada bahasa pemrograman python, identasi (spasi ke dalam) sangat
penting dan akan menyebabkan error jika diabaikan.
"""

#contohnya

height = 172

if height > 170 :
print("Kamu tinggi!") #kode ini akan error karena baris tidak teridentasi

#contoh yang benar

height = 172

if height > 170 :
    print("Kamu tinggi!") 

""""
kode diatas akan berjalan dengan baik karena setelah if
wajib ada baris yang teridentasi. Jadi jangan lupa identasi dan ':'
setelah if biar python ga marah.
"""

#sub-bab : statements

"""
Di python, statement berakhir jika baris berakhir. Jadi, ga perlu
pakai semicolon ';' seperti di bahasa pemrograman lain.
"""

#Ini adalah statement untuk menampilkan teks ke layar
print("Nihao!")

#Ini adalah statement untuk menyimpan nilai ke dalam variabel
sapaan = ["nihao", "konnichiwa", "guten morgen"]

#Ini adalah statement untuk operasi sederhana
tinggi = 170 + 7

#Dan ini untuk menampilkan hasil operasinya
print(tinggi)
