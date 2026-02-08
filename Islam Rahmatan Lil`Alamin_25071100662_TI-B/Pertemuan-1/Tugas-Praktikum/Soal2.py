# Buat sebuah program Python yang:
# 1. Menyimpan dua bilangan ke dalam dua variabel
# 2. Menghitung hasil penjumlahan dan perkalian dari kedua bilangan tersebut
# 3. Menampilkan hasilnya ke layar

x = 67
y = 69

## Bisa pake 3 cara
# 1. Cara Noob
print('Hasil tambah:', x + y)
print("Hasil kali:", x * y)


# 2. Cara Pro
def tambah(a, b): # Fungsi yang mengembalikan hasil penjumlahan 2 buah bilangan
    return a + b

def kali(a, b): # Fungsi yang mengembalikan hasil perkalian 2 buah bilangan
    return a * b

print('Hasil tambah:', tambah(x, y))
print("Hasil kali:", kali(x, y))


# 3. Cara Hengker
tambah = lambda a, b: a + b # Fungsi one-Liner yg ngembaliin hasil pejumlahan
print("Hasil tambah:",tambah(x, y))

kali = lambda a,b: a * b # Fungsi one-Liner yg ngembaliin hasil perkalian
print("Hasil kali",kali(x, y))