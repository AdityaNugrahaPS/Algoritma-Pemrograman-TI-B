# ==============================
# variables.py
# Belajar variabel di Python
# ==============================

# ==============================
# Python Variables
# ==============================

# 1. Deklarasi variabel sederhana
nama = "Fasbir"
umur = 19
tinggi = 175.5
mahasiswa = True

print("Nama:", nama)
print("Umur:", umur, "tahun")
print("Tinggi:", tinggi, "cm")
print("Status mahasiswa:", mahasiswa)

# ==============================
# Variable Names
# ==============================

# Aturan penamaan variabel
fa_sbir = "underscore"        # snake_case (disarankan di Python)
faSbir = "camelCase"          # camelCase (umum di bahasa lain)
FASBIR = "UPPERCASE"          # Konvensi untuk konstanta
_fas_bir = "private"     # Konvensi untuk private (awalan underscore)
_fasbir = "protected"           # Protected variable

# Nama variabel yang valid
nama_lengkap = "Fasbir Sabran"
umur20 = 19                  # Angka boleh di akhir/tengah
nilai_ujian = 85.5

# Nama variabel yang TIDAK valid (akan error jika dijalankan):
# 2nama = "test"             # Tidak boleh mulai dengan angka
# nama-lengkap = "test"     # Tidak boleh mengandung dash/hyphen
# nama lengkap = "test"     # Tidak boleh mengandung spasi

# ==============================
# Assign Multiple Values
# ==============================

# Multiple assignment
x, y, z = "Merah", "Hijau", "Biru"
print(f"Warna: {x}, {y}, {z}")

# One value to multiple variables
a = b = c = "Python"
print(f"Semua variabel bernilai: {a}, {b}, {c}")

# Unpack collection
buah = ["Apel", "Jeruk", "Mangga"]
buah1, buah2, buah3 = buah
print(f"Buah-buahan: {buah1}, {buah2}, {buah3}")

# Unpack dengan underscore untuk nilai yang diabaikan
orang = ["Fasbir", "Sabran", 19, "Batam"]
nama_depan, nama_belakang, *_ = orang
print(f"Nama: {nama_depan} {nama_belakang}")

# ==============================
# Output Variables
# ==============================

# Output dengan print() 
print("Nama saya", nama, "umur", umur, "tahun")

# Output dengan f-string 
print(f"Nama: {nama}, Umur: {umur}, Tinggi: {tinggi}cm")

# Output dengan concatenation
print("Nama: " + nama + ", Status: Mahasiswa")

# Output dengan format() method
print("Umur: {}, Tinggi: {}cm".format(umur, tinggi))

# Output multiple variables dengan separator
print("Data:", nama, umur, tinggi, sep=" | ")

# ==============================
# Global Variables
# ==============================

# Variabel global
universitas = "Universitas Unri"

def info_mahasiswa():
    # Variabel lokal
    fakultas = "Teknik Informatika"
    print(f"{nama} kuliah di {universitas}, Fakultas {fakultas}")

info_mahasiswa()
print(f"Universitas: {universitas}")  # Bisa diakses di luar fungsi

# Mengubah variabel global di dalam fungsi
counter = 0

def tambah_counter():
    global counter  # Deklarasi untuk mengubah variabel global
    counter += 1

tambah_counter()
tambah_counter()
print(f"Counter: {counter}")

# Variabel nonlocal (untuk nested functions)
def outer_function():
    nilai = 10
    
    def inner_function():
        nonlocal nilai  # Mengakses variabel dari outer function
        nilai = 20
    
    inner_function()
    print(f"Nilai dalam outer function: {nilai}")

outer_function()

