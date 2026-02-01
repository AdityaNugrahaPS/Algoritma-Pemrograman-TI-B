"""
Python numbers
"""

# Tipe Data Integer (int)
# Bilangan bulat positif atau negatif tanpa desimal
bilangan_bulat_positif = 10
bilangan_bulat_negatif = -5
bilangan_bulat_nol = 0

"""
Gunakan konverter kalau bingung
misal, octal to dec; biner to dec, hex to dec, dll.
"""
# Integer dalam berbagai basis
bilangan_desimal = 255        # Basis 10 (desimal)
bilangan_biner = 0b11111111   # Basis 2 (biner), sama dengan 255
bilangan_oktal = 0o377        # Basis 8 (oktal), sama dengan 255
bilangan_heksadesimal = 0xFF  # Basis 16 (heksadesimal), sama dengan 255

# Tipe Data Float (float)
# Bilangan desimal atau bilangan dengan titik koma
bilangan_desimal_kecil = 3.14
bilangan_desimal_besar = 1.7e10    # Notasi ilmiah: 1.7 x 10^10
bilangan_desimal_negatif = -2.5
bilangan_sangat_kecil = 4.2e-4     # Sama dengan 0.00042

# Tipe Data Complex (complex)
# Bilangan kompleks dengan bagian real dan imajiner
bilangan_kompleks1 = 3 + 4j      # 3 adalah bagian real, 4 adalah bagian imajiner
bilangan_kompleks2 = 2 - 5j      # 2 adalah bagian real, -5 adalah bagian imajiner
bilangan_kompleks_hanya_imajiner = 7j  # Hanya bagian imajiner

# Konversi antar tipe numerik
konversi_int_to_float = float(5)      # Mengubah integer menjadi float: 5.0
konversi_float_to_int = int(7.9)      # Mengubah float menjadi integer: 7 (dipotong)
konversi_string_to_int = int("123")   # Mengubah string menjadi integer: 123
konversi_string_to_float = float("3.14")  # Mengubah string menjadi float: 3.14

# Operasi aritmatika dasar
penjumlahan = 5 + 3        # Hasil: 8
pengurangan = 10 - 4       # Hasil: 6
perkalian = 6 * 7          # Hasil: 42
pembagian = 15 / 3         # Hasil: 5.0 (selalu menghasilkan float)
pembagian_bulat = 15 // 4  # Hasil: 3 (pembagian yang dibulatkan ke bawah)
modulus = 17 % 5           # Hasil: 2 (sisa pembagian)
pangkat = 2 ** 3           # Hasil: 8 (2 pangkat 3)

# Fungsi bawaan untuk angka
nilai_absolut = abs(-10)            # Nilai absolut: 10
pembulatan = round(3.7)             # Pembulatan: 4
pembulatan_dua_desimal = round(3.14159, 2)  # Pembulatan ke 2 desimal: 3.14
nilai_maksimum = max(1, 5, 3, 9, 2) # Nilai maksimum: 9
nilai_minimum = min(1, 5, 3, 9, 2)  # Nilai minimum: 1
pangkat_fungsi = pow(2, 3)          # Pangkat menggunakan fungsi: 8 ; 2^3

"""
Ini termasuk ke dalam modular
"""
# Konstanta matematika umum (dari modul math)
import math

nilai_pi = math.pi          # π ≈ 3.141592653589793
nilai_e = math.e            # e ≈ 2.718281828459045
akar_infinity = math.inf    # Infinity
nilai_nan = math.nan        # Not a Number

# Fungsi matematika lainnya
akar_kuadrat = math.sqrt(16)    # Akar kuadrat
logaritma_alami = math.log(math.e)  # Logaritma
sinus = math.sin(math.pi / 2)   # Sinus dari π/2: 1.0
cosinus = math.cos(0)           # Cosinus dari 0: 1.0