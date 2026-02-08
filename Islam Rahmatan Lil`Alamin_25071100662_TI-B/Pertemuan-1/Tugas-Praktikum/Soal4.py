# Buat sebuah program Python yang:
# 1. Menggunakan perulangan for
# 2. Menampilkan bilangan dari 1 sampai 10
# 3. Menghitung dan menampilkan jumlah dari bilangan 1 sampai 10
# Contoh keluaran:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# Jumlah = 55

jumlah = 0
for i in range(0, 11): # buat perulangan dari 1 sampai 10, 11 gak termasuk karna sifat akhirannya ekslisif
    print(i)
    jumlah += i
print("Jumlah:", jumlah)

