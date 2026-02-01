def hitung(a,b):
    hasilTambah = a + b
    hasilKurang = a - b

    print(f"Penjumlahan = {hasilTambah}")
    print(f"Pengurangan = {hasilKurang}")

hitung(15,8)

#Atau

def Hitung(x,y):
    tambah = x + y
    kurang = x - y

    return tambah,kurang

hasil_tambah, hasil_kurang = Hitung(20,13)
print(f"Penjumlahan = {hasil_tambah}")
print(f"Pengurangan = {hasil_kurang}")

