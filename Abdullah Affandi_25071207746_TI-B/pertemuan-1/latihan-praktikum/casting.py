"""
Python casting
"""

# 1. Casting ke Integer (int)
# Dari string ke integer
string_angka = "10"
konversi_string_ke_int = int(string_angka)  # Mengubah string "10" menjadi integer 10

# Dari float ke integer
float_angka = 3.9
konversi_float_ke_int = int(float_angka)    # Mengubah float 3.9 menjadi integer 3 (dibulatkan ke bawah)

# Dari boolean ke integer
boolean_true = True
boolean_false = False
konversi_bool_ke_int_true = int(boolean_true)   # Mengubah True menjadi 1
konversi_bool_ke_int_false = int(boolean_false) # Mengubah False menjadi 0

# 2. Casting ke Float (float)
# Dari string ke float
string_desimal = "3.14"
konversi_string_ke_float = float(string_desimal)  # Mengubah string "3.14" menjadi float 3.14

# Dari integer ke float
integer_angka = 5
konversi_int_ke_float = float(integer_angka)      # Mengubah integer 5 menjadi float 5.0

# Dari boolean ke float
konversi_bool_ke_float_true = float(True)         # Mengubah True menjadi 1.0
konversi_bool_ke_float_false = float(False)       # Mengubah False menjadi 0.0

# 3. Casting ke String (str)
# Dari integer ke string
angka_integer = 123
konversi_int_ke_string = str(angka_integer)       # Mengubah integer 123 menjadi string "123"

# Dari float ke string
angka_float = 4.56
konversi_float_ke_string = str(angka_float)       # Mengubah float 4.56 menjadi string "4.56"

# Dari boolean ke string
konversi_bool_ke_string_true = str(True)          # Mengubah True menjadi string "True"
konversi_bool_ke_string_false = str(False)        # Mengubah False menjadi string "False"

# 4. Casting ke Boolean (bool)
# Dari string ke boolean
string_kosong = ""
string_berisi = "hello"
konversi_string_ke_bool_kosong = bool(string_kosong)    # String kosong menjadi False
konversi_string_ke_bool_berisi = bool(string_berisi)    # String berisi menjadi True

# Dari integer ke boolean
nol = 0
non_nol = 5
konversi_int_ke_bool_nol = bool(nol)              # 0 menjadi False
konversi_int_ke_bool_non_nol = bool(non_nol)      # Angka selain 0 menjadi True

# Dari float ke boolean
nol_float = 0.0
non_nol_float = 3.14
konversi_float_ke_bool_nol = bool(nol_float)      # 0.0 menjadi False
konversi_float_ke_bool_non_nol = bool(non_nol_float)  # Float selain 0.0 menjadi True

# Contoh casting dalam operasi matematika
harga_barang = "15000"  # String yang mewakili angka
diskon = "1000"         # String yang mewakili angka
total_pembayaran = int(harga_barang) - int(diskon)  # Casting string ke int untuk operasi aritmatika

# Casting untuk pembulatan
angka_desimal = 7.89
angka_dibulatkan = int(angka_desimal)  # Membuang bagian desimal, hasil: 7

# Casting untuk konversi dari dan ke bentuk biner
angka_biasa = 42
angka_ke_biner = bin(angka_biasa)      # Mengubah integer ke representasi biner: '0b101010'
biner_ke_angka = int("101010", 2)      # Mengubah string biner ke integer: 42

# Casting untuk konversi dari dan ke bentuk heksadesimal
angka_ke_heksa = hex(angka_biasa)      # Mengubah integer ke representasi heksadesimal: '0x2a'
heksa_ke_angka = int("2a", 16)         # Mengubah string heksadesimal ke integer: 42

# Casting untuk konversi dari dan ke bentuk oktal
angka_ke_oktal = oct(angka_biasa)      # Mengubah integer ke representasi oktal: '0o52'
oktal_ke_angka = int("52", 8)          # Mengubah string oktal ke integer: 42