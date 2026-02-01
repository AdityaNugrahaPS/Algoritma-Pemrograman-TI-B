# // Kegunaan tuple adalah menyimpan data yang urutannya tetap dan tidak dapat berubah // #

# Membuat Tuple
stok_fruit = ("Kitsune", "Buddha", "Portal")
print(stok_fruit)

# Mengambil tuple
stok_fruit = ("Kitsune", "Buddha", "Portal")
print(stok_fruit[0]) # Hasil = Kitsune
print(stok_fruit[1]) # Hasil = Buddha

# Update tuple
stok_fruit = ("Gas", "Phoenix", "Magma")
stok_baru = list(stok_fruit) # Mengganti dari tuple ke list
stok_baru [1] = "Dough"  # Mengganti Phoenix menjadi Dough
stok_fruit = tuple(stok_baru) # Kembalikan menjadi tuple
print(stok_fruit)

# Unpack tuple
stok_fruit = ("Gas", "Phoenix", "Barrier")
(Elemental, Beast, Natural) = stok_fruit
print(Elemental)    # Hasil = Gas
print(Beast)        # Hasil = Barrier

# Loop tuple
stok_fruit = ("Spirit", "Venom", "Control")
for x in stok_fruit:
    print("Ready Nich :" + x)

# Join tuple
stok_fruit = ("Leopard", "Dragon", "Spirit")
stok_baru = ("Gravity", "Mammoth")
stok_akhir = stok_fruit + stok_baru
print(stok_akhir)

# Tuple Methods
angka = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
print(angka.count(5))   # Untuk menghitung ada berapa banyak angka yang ingin di lihat
print(angka.index(8))   # Untuk melihat di index mana angka yang ingin di lihat
