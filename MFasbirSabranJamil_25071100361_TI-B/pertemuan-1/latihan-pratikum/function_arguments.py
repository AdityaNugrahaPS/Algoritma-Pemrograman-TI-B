# ==============================
# function_arguments.py
# Belajar fungsi dengan argumen di Python
# ==============================

# 1. Fungsi dengan parameter
def sapa(nama):
    print(f"Halo, {nama}!")

sapa("Fasbir")
sapa("Sabran")

# 2. Fungsi dengan multiple parameters
def tambah(a, b):
    hasil = a + b
    print(f"{a} + {b} = {hasil}")

tambah(5, 3)
tambah(10, 20)

# 3. Default parameter
def sapa_lengkap(nama, salam="Halo"):
    print(f"{salam}, {nama}!")

sapa_lengkap("Fasbir")              # Gunakan default
sapa_lengkap("Sabran", "Selamat pagi")  # Custom salam

# 4. Keyword arguments
def buat_profil(nama, umur, kota):
    print(f"Nama: {nama}")
    print(f"Umur: {umur}")
    print(f"Kota: {kota}")

buat_profil(nama="Fasbir", kota="Batam", umur=19)

# 5. Arbitrary arguments (*args)
def jumlahkan(*angka):
    total = sum(angka)
    print(f"Total: {total}")

jumlahkan(1, 2, 3)           # Total: 6
jumlahkan(10, 20, 30, 40)    # Total: 100

# 6. Arbitrary keyword arguments (**kwargs)
def tampilkan_info(**info):
    for key, value in info.items():
        print(f"{key}: {value}")

tampilkan_info(nama="Fasbir", umur=19, kota="Batam")

# 7. Return value
def pangkat(angka, eksponen=2):
    return angka ** eksponen

hasil = pangkat(5, 3)  # 5^3 = 125
print(f"5 pangkat 3 = {hasil}")

# 8. Fungsi dengan tipe hint (Python 3.5+)
def hitung_luas(panjang: float, lebar: float) -> float:
    """Menghitung luas persegi panjang"""
    return panjang * lebar

luas = hitung_luas(5.5, 3.2)
print(f"Luas: {luas}")