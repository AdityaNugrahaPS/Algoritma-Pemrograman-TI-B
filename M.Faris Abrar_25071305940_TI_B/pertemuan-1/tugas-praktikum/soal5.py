
#membuat fungsi bernama htiung parameter

def hitung(a,b):
    penjumlahan = a + b
    pengurangan = a - b

    return penjumlahan, pengurangan

hasil_tambah, hasil_kurang = hitung(6,7)
 #mencetak output yg akan keluar
print(f'hasil penjumlahan kedua bilangan tersebut adalah : {hasil_tambah}')
print(f'hasil pengurangan kedua bilangan tersebut adalah : {hasil_kurang}')

