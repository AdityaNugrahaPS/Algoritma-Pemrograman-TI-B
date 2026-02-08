'''
Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b
2. Mengembalikan hasil penjumlahan a + b
3. Mengembalikan hasil pengurangan a - b
Kemudian:
1. Panggil fungsi tersebut
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
Contoh keluaran:
Penjumlahan = 8
Pengurangan = 2
'''

def kalkulator (a,b):
    tambah = a + b
    kurang = a - b

    return tambah, kurang

hasilkalkulator = kalkulator(10, 5)

print("Penjumlahan = ", hasilkalkulator)
print("Pengurangan = ", hasilkalkulator)