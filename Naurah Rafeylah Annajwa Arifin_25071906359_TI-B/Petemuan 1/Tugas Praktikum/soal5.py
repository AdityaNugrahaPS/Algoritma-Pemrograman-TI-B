#fungsi
def hitung(a, b):
    penjumlahan = a + b
    pengurangan = a - b
    return penjumlahan, pengurangan


hasil_tambah, hasil_kurang = hitung(57, 76)
print("Hasil penjumlahan:", hasil_tambah)
print("Hasil pengurangan:", hasil_kurang)