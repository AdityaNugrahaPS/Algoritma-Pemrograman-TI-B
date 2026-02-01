# Inisialisasi variabel untuk menyimpan jumlah
jumlah = 0

# Perulangan untuk menampilkan bilangan 1 sampai 10
print("Bilangan dari 1 sampai 10:")
for i in range(1, 11):  # range(1, 11) menghasilkan 1,2,3,4,5,6,7,8,9,10
    print(i)
    jumlah += i  # Menambahkan i ke jumlah

# Menampilkan jumlah total
print("Jumlah =", jumlah)