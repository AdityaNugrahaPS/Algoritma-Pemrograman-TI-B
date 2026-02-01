# ==============================
# operators.py
# Belajar operator di Python
# ==============================

# ==============================
# Python Operators
# ==============================
print("=== Python Operators ===")

# Operator adalah simbol untuk melakukan operasi pada variabel dan nilai
print("Operator digunakan untuk operasi matematika, perbandingan, dll")

# ==============================
# Arithmetic Operators
# ==============================
print("\n=== Arithmetic Operators (Operator Aritmatika) ===")

a = 15
b = 4

print(f"a = {a}, b = {b}")
print(f"Penjumlahan (+):  {a} + {b}  = {a + b}")
print(f"Pengurangan (-):  {a} - {b}  = {a - b}")
print(f"Perkalian (*):    {a} * {b}  = {a * b}")
print(f"Pembagian (/):    {a} / {b}  = {a / b}")
print(f"Modulus (%):      {a} % {b}  = {a % b}  (sisa bagi)")
print(f"Pangkat (**):     {a} ** {b} = {a ** b} ({a} pangkat {b})")
print(f"Floor Division (//): {a} // {b} = {a // b} (pembagian bulat)")

# ==============================
# Assignment Operators
# ==============================
print("\n=== Assignment Operators (Operator Penugasan) ===")

x = 10
print(f"x = {x}")

x += 5    # x = x + 5
print(f"x += 5  → x = {x}")

x -= 3    # x = x - 3
print(f"x -= 3  → x = {x}")

x *= 2    # x = x * 2
print(f"x *= 2  → x = {x}")

x /= 4    # x = x / 4
print(f"x /= 4  → x = {x}")

x %= 3    # x = x % 3
print(f"x %= 3  → x = {x}")

# ==============================
# Comparison Operators
# ==============================
print("\n=== Comparison Operators (Operator Perbandingan) ===")

nilai1 = 85
nilai2 = 70

print(f"nilai1 = {nilai1}, nilai2 = {nilai2}")
print(f"Sama dengan (==):      {nilai1} == {nilai2}  → {nilai1 == nilai2}")
print(f"Tidak sama (!=):       {nilai1} != {nilai2}  → {nilai1 != nilai2}")
print(f"Lebih besar (>):       {nilai1} > {nilai2}   → {nilai1 > nilai2}")
print(f"Lebih kecil (<):       {nilai1} < {nilai2}   → {nilai1 < nilai2}")
print(f"Lebih besar sama (>=): {nilai1} >= {nilai2}  → {nilai1 >= nilai2}")
print(f"Lebih kecil sama (<=): {nilai1} <= {nilai2}  → {nilai1 <= nilai2}")

# Contoh dengan string
nama1 = "Fasbir"
nama2 = "Sabran"
print(f"\nString comparison: '{nama1}' == '{nama2}' → {nama1 == nama2}")

# ==============================
# Logical Operators
# ==============================
print("\n=== Logical Operators (Operator Logika) ===")

usia = 19
nilai = 85
status_mahasiswa = True

print(f"usia = {usia}, nilai = {nilai}, status_mahasiswa = {status_mahasiswa}")

# AND (kedua kondisi harus True)
print(f"\nAND (dan):")
print(f"usia >= 17 AND nilai >= 75 → {usia >= 17 and nilai >= 75}")
print(f"usia > 20 AND status_mahasiswa → {usia > 20 and status_mahasiswa}")

# OR (salah satu kondisi True)
print(f"\nOR (atau):")
print(f"usia >= 21 OR nilai >= 80 → {usia >= 21 or nilai >= 80}")
print(f"usia < 18 OR nilai < 60 → {usia < 18 or nilai < 60}")

# NOT (kebalikan)
print(f"\nNOT (bukan):")
print(f"NOT status_mahasiswa → {not status_mahasiswa}")
print(f"NOT (nilai < 70) → {not (nilai < 70)}")

# ==============================
# Identity Operators
# ==============================
print("\n=== Identity Operators (Operator Identitas) ===")

list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 referensi ke list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = {list3}")

# is (cek apakah objek yang sama)
print(f"\nlist1 is list3 → {list1 is list3}")      # True (objek sama)
print(f"list1 is list2 → {list1 is list2}")      # False (objek berbeda)
print(f"list1 == list2 → {list1 == list2}")      # True (nilai sama)

# is not (cek apakah bukan objek yang sama)
print(f"\nlist1 is not list2 → {list1 is not list2}")  # True

# Contoh dengan None
data = None
print(f"\ndata is None → {data is None}")
print(f"data is not None → {data is not None}")

# ==============================
# Membership Operators
# ==============================
print("\n=== Membership Operators (Operator Keanggotaan) ===")

daftar_matkul = ["Algoritma", "Struktur Data", "Basis Data", "Python"]
nama = "Fasbir Sabran"

print(f"daftar_matkul = {daftar_matkul}")
print(f"nama = '{nama}'")

# in (apakah ada di dalam)
print(f"\n'Python' in daftar_matkul → {'Python' in daftar_matkul}")
print(f"'Java' in daftar_matkul → {'Java' in daftar_matkul}")
print(f"'bir' in nama → {'bir' in nama}")  # Cek substring

# not in (apakah tidak ada di dalam)
print(f"\n'Java' not in daftar_matkul → {'Java' not in daftar_matkul}")
print(f"'Algoritma' not in daftar_matkul → {'Algoritma' not in daftar_matkul}")

# Contoh dengan dictionary
data_mahasiswa = {'nama': 'Fasbir', 'nim': '122501234', 'prodi': 'TI'}
print(f"\ndata_mahasiswa = {data_mahasiswa}")
print(f"'nama' in data_mahasiswa → {'nama' in data_mahasiswa}")
print(f"'alamat' in data_mahasiswa → {'alamat' in data_mahasiswa}")

# ==============================
# Bitwise Operators
# ==============================
print("\n=== Bitwise Operators (Operator Bitwise) ===")

# Bitwise bekerja pada level bit (binary)
a = 10  # Binary: 1010
b = 4   # Binary: 0100

print(f"a = {a} (binary: {bin(a)})")
print(f"b = {b} (binary: {bin(b)})")

print(f"\nAND (&):   {a} & {b} = {a & b}   ({bin(a & b)})")
print(f"OR (|):    {a} | {b} = {a | b}    ({bin(a | b)})")
print(f"XOR (^):   {a} ^ {b} = {a ^ b}    ({bin(a ^ b)})")
print(f"NOT (~):   ~{a} = {~a}      ({bin(~a & 0xF)})  # 4-bit representation")
print(f"Shift kiri (<<):  {a} << 1 = {a << 1}  ({bin(a << 1)})")
print(f"Shift kanan (>>): {a} >> 1 = {a >> 1}  ({bin(a >> 1)})")

# ==============================
# Operator Precedence
# ==============================
print("\n=== Operator Precedence (Prioritas Operator) ===")

print("Urutan prioritas (dari tertinggi):")
print("1. **                    (pangkat)")
print("2. ~ + -                 (bitwise NOT, unary plus/minus)")
print("3. * / // %              (perkalian, pembagian, modulus)")
print("4. + -                   (penjumlahan, pengurangan)")
print("5. << >>                 (shift bit)")
print("6. &                     (bitwise AND)")
print("7. ^ |                   (bitwise XOR, OR)")
print("8. < <= > >= == !=       (perbandingan)")
print("9. is is not             (identitas)")
print("10. in not in            (keanggotaan)")
print("11. not                  (logika NOT)")
print("12. and                  (logika AND)")
print("13. or                   (logika OR)")

# Contoh perhitungan dengan prioritas
result = 10 + 5 * 2 ** 2 / 4 - 1
print(f"\nContoh: 10 + 5 * 2 ** 2 / 4 - 1")
print(f"Langkah 1: 2 ** 2 = 4       (pangkat)")
print(f"Langkah 2: 5 * 4 = 20       (perkalian)")
print(f"Langkah 3: 20 / 4 = 5.0     (pembagian)")
print(f"Langkah 4: 10 + 5.0 = 15.0  (penjumlahan)")
print(f"Langkah 5: 15.0 - 1 = 14.0  (pengurangan)")
print(f"Hasil: {result}")

# Gunakan kurung untuk mengatur prioritas
result2 = (10 + 5) * 2 ** 2 / (4 - 1)
print(f"\nDengan kurung: (10 + 5) * 2 ** 2 / (4 - 1) = {result2}")