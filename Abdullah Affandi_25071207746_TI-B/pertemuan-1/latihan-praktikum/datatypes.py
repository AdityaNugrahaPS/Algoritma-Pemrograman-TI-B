"""
Python datatypes
"""

# Tipe Data Numerik
x = 5          # int - bilangan bulat
y = 2.5        # float - bilangan desimal
z = 1j         # complex - bilangan kompleks

# Tipe Data String
nama = "Abdullah"      # str - teks
kata = 'Affandi'       # str - teks dengan petik satu

# Tipe Data Boolean
benar = True           # bool - nilai kebenaran benar
salah = False          # bool - nilai kebenaran salah

# Tipe Data List
buah = ["apel", "jeruk", "mangga"]     # list - kumpulan terurut dan dapat diubah
angka = [1, 2, 3, 4, 5]                # list - kumpulan angka

# Tipe Data Tuple
warna = ("merah", "hijau", "biru")     # tuple - kumpulan terurut dan tidak dapat diubah
koordinat = (10, 20)                   # tuple - kumpulan nilai tetap

# Tipe Data Set
himpunan_angka = {1, 2, 3, 4, 5}       # set - kumpulan unik tanpa urutan
himpunan_huruf = {"a", "b", "c"}       # set - kumpulan karakter unik

# Tipe Data Dictionary
data_mahasiswa = {"nama": "Abdullah", "usia": 20, "jurusan": "TI"}  # dict - pasangan kunci-nilai (key-value)
nilai = {"matematika": 95, "fisika": 87, "kimia": 92}               # dict - nilai pelajaran

# Tipe Data Range
rentang = range(5)                     # range - urutan angka dari 0 hingga 4
rentang_awal_akhir = range(2, 8)       # range - urutan angka dari 2 hingga 7

# Tipe Data Bytes
data_byte = b"hello"                   # bytes - deretan byte
data_bytearray = bytearray(5)          # bytearray - array byte yang dapat diubah
data_memoryview = memoryview(b"hello") # memoryview - tampilan memori dari objek byte

# Tipe Data None
kosong = None                          # NoneType - merepresentasikan tidak ada nilai