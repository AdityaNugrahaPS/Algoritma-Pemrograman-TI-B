''''
Soal: Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b.
2. Mengembalikan hasil penjumlahan a + b.
3. Mengembalikan hasil pengurangan a - b. 
Kemudian:
1. Panggil fungsi tersebut.
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar.
Contoh keluaran :
penjumlahan = 8
pengurangan = 2
'''
# Membuat fungsi hitung
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

# Memanggil fungsi dengan nilai a=5 dan b=3
hasil_tambah, hasil_kurang = hitung(5, 3)

# Menampilkan hasil ke layar
print("Penjumlahan =", hasil_tambah)
print("Pengurangan =", hasil_kurang)