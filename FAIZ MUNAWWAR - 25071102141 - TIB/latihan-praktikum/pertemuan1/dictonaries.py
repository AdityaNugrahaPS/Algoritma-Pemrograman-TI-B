# **** DICTONARIES **** #
# Dictonaries berguna untuk menyimpan nilai data

# Menyimpan nilai data (Dictonaries)
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
print(fruit_info)

# Mengambil Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
print(fruit_info["nama"])      # Hasil: Dragon
print(fruit_info.get("harga")) # Hasil: 5000000

#  Mengubah Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
fruit_info["harga"] = 4800000
print(fruit_info)

# Menambah Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
fruit_info["stok"] = 10
print(fruit_info)

# Menghapus Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
fruit_info.pop("tipe") # pop : Menghapus kunci tertentu.
print(fruit_info)

# Loop Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
for x in fruit_info:
    print(x)

# Melihat semua Nilai
for x in fruit_info.values():
    print(x)

# Melihat Kunci dan Nilai sekaligus
for x, y in fruit_info.items():
    print(x, ":", y)

# Copy Dictonaries
fruit_info = {
  "nama": "Dragon",
  "tipe": "Beast",
  "harga": 5000000
}
data_copy = fruit_info.copy()

# Nested Dictonaries
toko_fruit = {
  "fruit1": {"nama": "Kitsune", "stok": 5},
  "fruit2": {"nama": "Leopard", "stok": 2}
}
print(toko_fruit["fruit1"]["nama"]) # Hasil: Kitsune