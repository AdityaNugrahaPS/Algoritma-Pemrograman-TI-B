# Kali ini mengenai while loops atau perulangan while
# while loops akan terus mengulang blok kode selama kondisi yang diberikan bernilai True

# 1. Menggunakan while loops untuk mencetak angka dari 1 hingga 5
angka = 1
while angka <= 5: # intinya selama angka kurang dari atau sama dengan 5, dia akanngeprint angka setelahnya dengan pertambahan 1
    print(angka)  #output: 1 2 3 4 5 (cetak angka dari 1 sampai 5)
    angka += 1  # penambahan nilai agar tidak menjadi infinite loop

# 2. Menggunakan while loops untuk menjumlahkan angka dari 1 hingga n
n = int(input("Masukkan nilai n: ")) # langsung ubah inputan jadi integer
i = 1
while i <= n:
    print(i)  #output: cetak angka dari 1 sampai n
    i += 1

# 3. Menggunakan while loops dengan pernyataan break dan continue
count = 0
while True:  # perulangan tak hingga
    count += 1
    if count == 3:
        continue  # ketika di perulangan ke 3, dia akan melewati aja
    if count > 5:
        break  # keluar dari loop ketika count lebih dari 5
    print(count)  #output: 1 2 4 5 (skip 3)
