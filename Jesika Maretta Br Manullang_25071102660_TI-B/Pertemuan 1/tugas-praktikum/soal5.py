# 1. Membuat fungsi hitung
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan  # Mengembalikan dua nilai sekaligus

# 2. Memanggil fungsi
hasil_jumlah, hasil_kurang = hitung(4, 2)

# 3. Menampilkan hasil
print("Penjumlahan =", hasil_jumlah)
print("Pengurangan =", hasil_kurang)
