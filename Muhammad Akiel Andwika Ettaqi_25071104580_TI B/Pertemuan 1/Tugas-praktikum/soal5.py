#Menggunakan fungsi
def hitung(a,b):
    tambah = a + b
    kurang = a - b
    return tambah, kurang  #Jika ingin dipanggil, yang pertama dipanggil tambah, yang kedua kurang

#Kita buat variabel yang mau dihitung
a = 100
b = 67

hasilTambah, hasilKurang = hitung(a,b)

print("Penjumlahan =", hasilTambah)
print("Pengurangan =", hasilKurang)