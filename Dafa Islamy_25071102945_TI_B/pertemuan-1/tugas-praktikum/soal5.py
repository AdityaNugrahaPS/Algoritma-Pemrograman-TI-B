'''
Soal 5 (Fungsi)

Buat sebuah fungsi bernama hitung(a, b) yang:
1. Menerima dua parameter a dan b
2. Mengembalikan hasil penjumlahan a + b
3. Mengembalikan hasil pengurangan a - b
Kemudian:
1. Panggil fungsi tersebut
2. Tampilkan hasil penjumlahan dan pengurangannya ke layar
'''

#membuat sebuah fungsi untuk menghtiung penjumlahan dan pengurangan dua variabel
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan #kembalian dari fungsi ini berupa tuple

hasilTambah, hasilKurang = hitung(6, 16) #memanggil fungsi lalu memecah isi tuple dan menyimpan hasilnya kedalam dua variabel berbeda

print('Hasil penjumlahan 6 dan 16 adalah', hasilTambah) #output = Hasil penjumlahan 6 dan 16 adalah 22
print('Hasil pengurangan 6 dan 16 adalah', hasilKurang) #output = Hasil pengurangan 6 dan 16 adalah -10