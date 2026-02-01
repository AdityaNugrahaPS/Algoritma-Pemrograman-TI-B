"""
Python match
"""

"""
_: adalah nilai lainnya, mirip dengan "default"
"""
# Contoh 1: Match sederhana dengan angka
def cek_angka(nilai):
    match nilai:
        case 1:
            return "Satu"
        case 2:
            return "Dua"
        case 3:
            return "Tiga"
        case _:
            return "Lainnya"

print("1. Match sederhana dengan angka:")
print(cek_angka(2))
print(cek_angka(5))

# Contoh 2: Match dengan string
def cek_hari(hari):
    match hari:
        case "Senin":
            return "Awal minggu"
        case "Jumat":
            return "Akhir minggu kerja"
        case "Sabtu" | "Minggu":
            return "Hari libur"
        case _:
            return "Hari biasa"

print("\n2. Match dengan string:")
print(cek_hari("Jumat"))
print(cek_hari("Minggu"))
print(cek_hari("Rabu"))

# Contoh 3: Match dengan kondisi
def cek_usia(usia):
    match usia:
        case x if x < 18:
            return "Masih muda"
        case x if x < 60:
            return "Dewasa"
        case _:
            return "Lansia"

print("\n3. Match dengan kondisi:")
print(cek_usia(15))
print(cek_usia(30))
print(cek_usia(70))

# Contoh 4: Match dengan pola tuple
def cek_koordinat(point):
    match point:
        case (0, 0):
            return "Titik asal"
        case (0, y):
            return f"Di sumbu Y pada posisi {y}"
        case (x, 0):
            return f"Di sumbu X pada posisi {x}"
        case (x, y):
            return f"Titik di ({x}, {y})"
        case _:
            return "Bukan koordinat valid"

print("\n4. Match dengan pola tuple:")
print(cek_koordinat((0, 0)))
print(cek_koordinat((0, 5)))
print(cek_koordinat((3, 0)))
print(cek_koordinat((2, 4)))

# Contoh 5: Match dengan list
def cek_list(items):
    match items:
        case []:
            return "List kosong"
        case [a]:
            return f"Satu item: {a}"
        case [a, b]:
            return f"Dua item: {a} dan {b}"
        case [a, b, c]:
            return f"Tiga item: {a}, {b}, dan {c}"
        case _:
            return "Lebih dari tiga item"

print("\n5. Match dengan list:")
print(cek_list([]))
print(cek_list([1]))
print(cek_list([1, 2]))
print(cek_list([1, 2, 3]))
print(cek_list([1, 2, 3, 4]))

"""
type.__name__: mengarah ke tipe data
see: https://docs.python.org/3/reference/datamodel.html#type.__name__
"""
# Contoh 6: Match untuk menentukan jenis data
def cek_jenis_data(data):
    match data:
        case int():
            return f"Ini adalah integer: {data}"
        case str():
            return f"Ini adalah string: {data}"
        case list():
            return f"Ini adalah list dengan {len(data)} item"
        case dict():
            return f"Ini adalah dictionary dengan {len(data)} pasangan kunci-nilai"
        case _:
            return f"Jenis data tidak dikenal: {type(data).__name__}"

print("\n6. Match untuk menentukan jenis data:")
print(cek_jenis_data(42))
print(cek_jenis_data("Hello"))
print(cek_jenis_data([1, 2, 3]))
print(cek_jenis_data({"a": 1, "b": 2}))

# Contoh 7: Match dalam aplikasi sederhana (kalkulator)
def kalkulator(operasi, a, b):
    match operasi:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            if b != 0:
                return a / b
            else:
                return "Tidak bisa dibagi dengan nol"
        case _:
            return "Operasi tidak dikenal"

print("\n7. Match dalam aplikasi kalkulator:")
print(kalkulator("+", 5, 3))
print(kalkulator("*", 4, 6))
print(kalkulator("/", 10, 2))
print(kalkulator("%", 10, 3))

print("\nSelesai!")