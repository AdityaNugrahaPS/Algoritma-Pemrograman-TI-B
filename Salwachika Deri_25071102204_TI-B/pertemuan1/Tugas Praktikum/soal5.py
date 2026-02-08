#fungsi
def hitung (a, b):
    hasilpenjumlahan = a + b
    hasilpengurangan = a - b
    return hasilpenjumlahan, hasilpengurangan

penjumlahan, pengurangan = hitung(15, 4)    #memanggil fungsi
    #hasil
print('penjumlahan = ', penjumlahan)
print('pengurangan = ', pengurangan) 