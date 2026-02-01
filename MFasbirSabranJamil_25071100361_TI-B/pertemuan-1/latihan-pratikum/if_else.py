# ==============================
# if_else.py
# Belajar percabangan if-else di Python
# ==============================

# ==============================
# Python If
# ==============================
print("=== Python If ===")

# If statement untuk mengeksekusi kode jika kondisi True
usia = 20

if usia >= 17:
    print("Sudah cukup usia untuk membuat KTP")

nilai = 85
if nilai >= 75:
    print("Anda lulus mata kuliah ini")
    print("Selamat!")

# ==============================
# Python Elif
# ==============================
print("\n=== Python Elif ===")

# Elif (else if) untuk kondisi kedua, ketiga, dst
nilai = 82

if nilai >= 85:
    print("Grade: A")
    print("Sangat baik!")
elif nilai >= 75:
    print("Grade: B")  # Ini yang akan dieksekusi
    print("Baik")
elif nilai >= 65:
    print("Grade: C")
    print("Cukup")
elif nilai >= 55:
    print("Grade: D")
    print("Kurang")

# Contoh dengan kondisi kompleks
jam = 14

if jam < 12:
    print("Selamat pagi!")
elif jam < 18:
    print("Selamat siang!")  # Dieksekusi
elif jam < 21:
    print("Selamat sore!")
else:
    print("Selamat malam!")

# ==============================
# Python Else
# ==============================
print("\n=== Python Else ===")

# Else untuk kondisi terakhir jika semua if/elif False
password = "python123"

if password == "admin123":
    print("Login sebagai admin")
elif password == "user123":
    print("Login sebagai user")
else:
    print("Password salah!")  # Ini dieksekusi

# Contoh sederhana if-else
nilai = 58

if nilai >= 60:
    print("Status: Lulus")
    print("Nilai akhir:", nilai)
else:
    print("Status: Tidak Lulus")
    print("Remidi diperlukan")

# ==============================
# Shorthand If
# ==============================
print("\n=== Shorthand If (If Satu Baris) ===")

# Format: nilai_jika_true if kondisi else nilai_jika_false
x = 10
y = 15

# Cara biasa
if x > y:
    hasil = "x lebih besar"
else:
    hasil = "y lebih besar atau sama"
print("Cara biasa:", hasil)

# Cara shorthand
hasil = "x lebih besar" if x > y else "y lebih besar atau sama"
print("Shorthand:", hasil)

# Contoh lain
nilai = 75
status = "Lulus" if nilai >= 65 else "Tidak Lulus"
print(f"Nilai: {nilai}, Status: {status}")

usia = 18
kategori = "Dewasa" if usia >= 17 else "Anak-anak"
print(f"Usia: {usia}, Kategori: {kategori}")

# Shorthand dengan multiple statements (tidak disarankan)
print("Genap") if 10 % 2 == 0 else print("Ganjil")

# ==============================
# Logical Operators
# ==============================
print("\n=== Logical Operators (Dalam If) ===")

# AND - kedua kondisi harus True
username = "fasbir"
password = "python123"

if username == "fasbir" and password == "python123":
    print("Login berhasil!")
else:
    print("Username atau password salah")

# Contoh AND lainnya
nilai = 80
kehadiran = 85

if nilai >= 75 and kehadiran >= 75:
    print("Syarat lulus terpenuhi")
    print("Bisa ikut ujian")
else:
    print("Tidak memenuhi syarat")

# OR - salah satu kondisi True
hari = "Sabtu"

if hari == "Sabtu" or hari == "Minggu":
    print("Hari libur!")
    print("Bisa istirahat")
else:
    print("Hari kerja")
    print("Waktunya kuliah")

# NOT - membalikkan kondisi
mahasiswa = False

if not mahasiswa:
    print("Bukan mahasiswa")  # Dieksekusi
    print("Tidak bisa akses e-learning")
else:
    print("Akses diberikan")

# Kombinasi AND, OR, NOT
usia = 19
izin_ortu = True

if (usia >= 17 or izin_ortu) and not mahasiswa:
    print("Bisa ikut kursus")
    print("Daftar sekarang!")

# ==============================
# Nested If
# ==============================
print("\n=== Nested If (If Bersarang) ===")

# If di dalam if
usia = 20
punya_ktp = True
saldo = 1500000

if usia >= 17:
    print("✅ Cukup usia")
    
    if punya_ktp:
        print("✅ Punya KTP")
        
        if saldo >= 1000000:
            print("✅ Cukup saldo")
            print("Bisa buka rekening bank!")
        else:
            print("❌ Saldo tidak cukup")
            print(f"Minimal Rp 1.000.000, saldo Anda: Rp {saldo:,}")
    else:
        print("❌ Belum punya KTP")
        print("Harus buat KTP dulu")
else:
    print("❌ Belum cukup usia")
    print(f"Usia Anda: {usia}, minimal 17 tahun")

# Contoh lain: penilaian mahasiswa
nilai_tugas = 85
nilai_uts = 78
nilai_uas = 82

if nilai_tugas >= 60:
    print("Tugas: Lulus")
    
    if nilai_uts >= 60:
        print("UTS: Lulus")
        
        if nilai_uas >= 60:
            print("UAS: Lulus")
            print("Selamat, Anda lulus mata kuliah!")
        else:
            print("UAS: Tidak lulus")
            print("Remidi UAS diperlukan")
    else:
        print("UTS: Tidak lulus")
        print("Remidi UTS diperlukan")
else:
    print("Tugas: Tidak lulus")
    print("Perbaiki tugas terlebih dahulu")

# ==============================
# Pass Statement
# ==============================
print("\n=== Pass Statement ===")

# Pass digunakan sebagai placeholder untuk kode yang belum diimplementasi
usia = 16

if usia >= 17:
    # Kode akan ditambahkan nanti
    pass  # Tidak melakukan apa-apa
else:
    print("Belum cukup usia")

# Contoh: struktur program yang belum lengkap
nilai = 90

if nilai >= 85:
    # TODO: Tambahkan logika untuk grade A
    pass
elif nilai >= 75:
    print("Grade B")
    print("Pertahankan!")
elif nilai >= 65:
    # TODO: Tambahkan saran perbaikan
    pass
else:
    print("Perlu belajar lebih giat")

# Pass dalam fungsi kosong
def cek_kelulusan():
    pass  # Fungsi belum diimplementasi

def hitung_nilai():
    # Akan diisi nanti
    pass