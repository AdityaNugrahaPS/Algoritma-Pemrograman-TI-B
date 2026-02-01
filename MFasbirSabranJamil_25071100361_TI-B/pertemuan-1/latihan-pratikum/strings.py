# ==============================
# strings.py
# Belajar string di Python
# ==============================

# ==============================
# 1. Python Strings
# ==============================
print("1. Python Strings")

nama = "Fasbir Sabran"
print("Nama saya:", nama)

# String bisa pakai kutip satu atau dua
kata1 = 'Halo'
kata2 = "Dunia"
print(kata1, kata2)

# Akses karakter dalam string
print("Karakter pertama:", nama[0])     # F
print("Karakter keempat:", nama[3])     # b
print("Karakter terakhir:", nama[-1])   # n

# ==============================
# 2. Slicing Strings
# ==============================
print("\n2. Slicing Strings (Memotong String)")

teks = "PythonProgramming"
print("Teks lengkap:", teks)

# Format: string[awal:akhir]
print("Potongan 0-6:", teks[0:6])      # Python
print("Potongan 6-akhir:", teks[6:])   # Programming
print("Potongan awal-6:", teks[:6])    # Python
print("Potongan -8:-1:", teks[-8:-1])  # Program

# Contoh praktis: ambil username dari email
email = "fasbir@unri.ac.id"
print("\nEmail:", email)
print("Username:", email[:email.find('@')])

# ==============================
# 3. Modify Strings
# ==============================
print("\n3. Modify Strings (Mengubah String)")

# Huruf besar/kecil
nama = "fasbir sabran"
print("Original:", nama)
print("Upper:", nama.upper())
print("Title:", nama.title())

# Hapus spasi di pinggir
teks = "   Hello World   "
print(f"\nOriginal: '{teks}'")
print(f"Strip: '{teks.strip()}'")

# Ganti kata
kalimat = "Saya suka Java"
print("\nOriginal:", kalimat)
print("Replace:", kalimat.replace("Java", "Python"))

# ==============================
# 4. Concatenate Strings
# ==============================
print("\n4. Concatenate Strings (Menggabungkan String)")

# Pakai +
nama_depan = "Fasbir"
nama_belakang = "Sabran"
nama_lengkap = nama_depan + " " + nama_belakang
print("Gabung pakai + :", nama_lengkap)

# Pakai join() untuk list
mata_kuliah = ["Python", "Java", "Web"]
gabung = " | ".join(mata_kuliah)
print("Gabung pakai join():", gabung)

# Pakai f-string
umur = 19
print("Pakai f-string:", f"Nama: {nama_lengkap}, Umur: {umur}")

# Ulang string
print("Ulang kata:", "Hi! " * 3)

# ==============================
# 5. Format Strings
# ==============================
print("\n5. Format Strings (Membuat Template)")

nama = "Fasbir"
nilai = 85.5678
print(f"Nama: {nama}, Nilai: {nilai:.2f}")  # 2 angka di belakang koma
print(f"Nama: {nama}, Nilai: {nilai:.0f}")  # tanpa desimal
print(f"Persen: {0.85:.1%}")  # format persentase

# Format dengan .format()
print("Nama: {}, IPK: {:.2f}".format(nama, 3.75))

# ==============================
# 6. Escape Characters
# ==============================
print("\n6. Escape Characters (Karakter Khusus)")

print("Baris baru:\nIni baris kedua")
print("Tab:\tNama\tFasbir")
print("Kutip dua: Dia bilang \"Halo\"")
print("Backslash: C:\\Users\\Fasbir")
print(r"Raw string: C:\Users\Fasbir\file.py")  # r di depan untuk raw

# ==============================
# 7. String Methods
# ==============================
print("\n7. String Methods (Fungsi-fungsi String)")

teks = "  Belajar Python Programming  "

# 1. Case methods
print("Upper:", teks.upper())
print("Lower:", teks.lower())

# 2. Check methods
print("\nCek string:")
print("'Python'.isalpha():", "Python".isalpha())      # hanya huruf
print("'123'.isdigit():", "123".isdigit())           # hanya angka
print("'Python123'.isalnum():", "Python123".isalnum()) # huruf & angka

# 3. Search methods
print("\nCari dalam string:")
print("Posisi 'Python':", teks.find("Python"))
print("Jumlah huruf 'a':", teks.count("a"))
print("Awal 'Belajar':", teks.startswith("Belajar"))

# 4. Split & Join
print("\nSplit dan Join:")
daftar_kata = "Python Java C++ JavaScript"
print("Split:", daftar_kata.split())  # jadi list

list_matkul = ["Algoritma", "Struktur Data", "Basis Data"]
print("Join:", " → ".join(list_matkul))

# Contoh praktis semua metode
print("\n=== Contoh Praktis ===")
data_input = "  fasbir,19,Teknik Informatika  "
data_bersih = data_input.strip().upper()
print("Input:", data_input)
print("Bersih:", data_bersih)

data_pisah = data_bersih.split(',')
print("Pisah per koma:", data_pisah)

print("\nData Mahasiswa:")
print(f"Nama: {data_pisah[0].title()}")
print(f"Umur: {data_pisah[1]}")
print(f"Prodi: {data_pisah[2]}")
