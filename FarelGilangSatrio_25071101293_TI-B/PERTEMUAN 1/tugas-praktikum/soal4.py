'''
Soal: Buat sebuah program Python yang:
1. Menggunakan perulangan for.
2. Menampilkan bilangan dari 1 sampai 10.
3. Menghitung dan menampilkan jumlah dari bilangan 1 sampai 10.
Contoh keluaran :
1
2
3
4
5
6
7
8
9
10
jumlah = 55
'''
jumlah = 0

# Perulangan for dari 1 sampai 10
for i in range(1, 11):
    print(i)
    jumlah += i  # Menambahkan angka ke total jumlah

# Menampilkan hasil jumlah
print("Jumlah =", jumlah)