# Soal 1.5 (Fungsi)

def operasi(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan

hasil_tambah, hasil_kurang = operasi(5, 3)

print("Penjumlahan =", hasil_tambah)
print("Pengurangan =", hasil_kurang)