# Buat sebuah fungsi bernama hitung(a, b) yang:
# 1. Menerima dua parameter a dan b
# 2. Mengembalikan hasil penjumlahan a + b
# 3. Mengembalikan hasil pengurangan a - b
# Kemudian:
# 1. Panggil fungsi tersebut
# 2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
# Contoh keluaran:
# Penjumlahan = 8
# Pengurangan = 2

def hitung(a, b):
    return a + b, a - b

# angka = hitung(5, 2) 
# print(angka)        # Output: (7, 3)
# print(type(angka))  # Output: tuple

'''
Karena fungsi hitung mengembalikan 2 nilai dan-
di soal kita diminta agar dapat memisahkan kedua-
nilai tersebut menjadi hasil pertambahan dan pengurangan,
maka kita harus memasukkan nilai kembaliannya langsung ke dalam 2 variabel 
'''

tambah, kurang = hitung (6, 4)
print("Hasil Penjumlahan:", tambah) # Output: 10
print("Hasil Pengurangan:", kurang) # Output: 2
