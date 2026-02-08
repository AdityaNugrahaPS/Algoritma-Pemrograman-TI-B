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
# Mendefinisikan fungsi hitung
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

# Memanggil fungsi hitung dengan contoh nilai
hasil_penjumlahan, hasil_pengurangan = hitung(5, 3)

# Menampilkan hasil penjumlahan dan pengurangan ke layar
print("Penjumlahan =", hasil_penjumlahan)
print("Pengurangan =", hasil_pengurangan)