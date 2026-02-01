# Function Dasar
def sapa_pelanggan():
  print("Halo Selamat Datang!")

sapa_pelanggan()

# Function Input
def sapa_nama(nama):
  print("Halo " + nama + ", mau beli buah apa?")

sapa_nama("Budi")

# *args ||| Parameter ini *args memungkinkan sebuah fungsi untuk menerima sejumlah argumen posisi ||| #
def daftar_pesanan(*buah):
  print("Pelanggan ini membeli:")
  for x in buah:
    print("- " + x)

daftar_pesanan("Dragon", "Leopard")
daftar_pesanan("Kitsune", "Dough", "Venom", "Spirit")

# kwargs ||| digunakan jika menerima sejumlah argumen kata kunci ||| #
def pembeli(**data):
    for kunci, nilai in data.items():
        print(f"{kunci}: {nilai}")

pembeli(nama="Budi", status="VVIP", total_beli=5)

# Scope Function
x = 300

def angka_berubah():
  x = 200
  print(x)

angka_berubah()

print(x)

# Decorator Function
def hiasan(fungsi_asli):
    def bungkus():
        print("--- Memulai Transaksi ---")
        fungsi_asli()
        print("--- Transaksi Selesai ---")
    return bungkus

@hiasan
def jual_buah():
    print("Berhasil menjual Dragon Fruit!")

jual_buah()

# Lambda Function
perkalian = lambda x : x * 2

print(perkalian(5))

# Recursion Function
def hitung_mundur(n):
  if n > 0:
    print(n)
    hitung_mundur(n - 1)
  else:
    print("Selesai!")

hitung_mundur(3)

# Generator Function
def penghitung_stok(n):
    i = 1
    while i <= n:
        yield i
        i += 1

stok = penghitung_stok(3)
print(next(stok)) 
print(next(stok)) 
