# **** SETS **** #
# Sets adalah koleksi yang tidak terurut , tidak dapat diubah* , dan tidak terindeks

# Membuat Set
stok_fruit = {"Dragon", "Leopard", "Dough"}
print(stok_fruit)

# Mengambil Set
stok_fruit = {"Dragon", "Leopard", "Dough"}
for buah in stok_fruit:
    print(buah)

# Menambah Set
stok_fruit = {"Dragon"}
stok_fruit.add("Kitsune") # Add : Untuk menambah satu item.
stok_fruit.update(["Venom", "Spirit"]) # Update : Untuk menambah banyak item
print(stok_fruit)

# Menghapus item dari Set
stok_fruit = {"Dragon", "Leopard", "Dough"}  # remove : Menghapus item. Jika item tidak ada, akan muncul error.
stok_fruit.discard("Leopard")                # discard: Menghapus item. Jika item tidak ada, tidak akan muncul error
print(stok_fruit)

# Loop Set
stok_fruit = {"Dragon", "Leopard", "Dough"}
for buah in stok_fruit:
    print("Stok: " + buah)

# Join Set
stok_fruit = {"Dragon", "Leopard", "Dough"}
stok_baru = {"Venom", "Yeti", "Dark"}
stok_akhir = stok_fruit.union(stok_baru)    # union : Menggabungkan semuanya
print(stok_akhir)