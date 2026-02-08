# Membuat list 
stok_fruit = ["Leopard", "Dragon", "Spirit"]
print("Stok awal:", stok_fruit)

# Mengambil item pertama (indeks di mulai dari nol)
stok_fruit = ["Leopard", "Dragon", "Spirit"]
print("Buah paling mahal saat ini:", stok_fruit[0])

# Mengganti list item (dari dari Spirit Ke Control)
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_fruit[2] = "Control"
print("Setelah stok diganti:", stok_fruit)

# Menambahkan item
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_fruit.append("Dough")

# Menyelipkan item di urutan kedua
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_fruit.insert(1, "Venom")
print("Setelah ditambah fruit baru:", stok_fruit)

# Menghapus item yang sudah tidak terpakai
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_fruit.remove("Leopard")
print("Setelah leopard tidak terpakai:", stok_fruit)

# Loop list menampilkan isi stok
stok_fruit = ["Leopard", "Dragon", "Spirit"]
print("\n--- DAFTAR STOK FRUIT ---")
for x in stok_fruit:
    print("-" + x)

# List yang lebih singkat
stok_fruit = ["Leopard", "Dragon", "Spirit"]
new_fruit = []

for x in stok_fruit:
  if "a" in x:          # Jika ada buah yang ada huruf a nya maka akan di print
    new_fruit.append(x)

print(new_fruit)

# Versi satu baris aja
stok_fruit = ["Leopard", "Dragon", "Spirit"]
new_fruit = [x for x in stok_fruit if "a" in x]

print(new_fruit)

# Sort list
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_fruit.sort()
print("Fruit yang setelah di sort :", stok_fruit) # Mengikuti Alfabet dari turun ke naik
stok_fruit.sort(reverse=True)
print("Fruit yang setelah di sort :", stok_fruit) # dari naik ke turun (Reverse)

# Copy List
stok_fruit = ["Leopard", "Dragon", "Spirit"]
akun1 = stok_fruit.copy()
print(akun1)

# Join List
stok_fruit = ["Leopard", "Dragon", "Spirit"]
stok_baru = ["Gravity", "Mammoth"]

stok_akhir = stok_fruit + stok_baru
stok_akhir.sort()
print(stok_akhir)

