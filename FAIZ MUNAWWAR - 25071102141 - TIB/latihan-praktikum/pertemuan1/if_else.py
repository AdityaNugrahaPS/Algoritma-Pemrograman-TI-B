# **** IF ELSE **** #

# Kondisi Dasar
stok = -1
if stok > 0:
    print("Barang tersedia!")

# Kondisi Kedua
harga = 5000
if harga > 5000:
    print("Mahal")
elif harga == 5000:
    print("Harga pas")

# Kondisi Terakhir
harga = 6000
if harga > 5000:
    print("Mahal")
else:
    print("Murah")

# ShortHand If
a = 6000
b = 5000
if a > b: print("a lebih besar")

# ShortHand If Else 
print("A") if a > b else print("B")

# Logika And & OR
stok = 5
harga = 1000

if stok > 0 and harga < 2000:
    print("Beli sekarang!")

# Nested If Else
fruit = "Dragon"
stok = 10
if stok > 0:
    print(f"Ada stok {fruit}")
    if stok > 5:
        print(f"Stok {fruit} aman")
    else:
        print(f"Stok {fruit} hampir habis")

