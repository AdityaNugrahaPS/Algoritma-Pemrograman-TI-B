# ==============================
# match.py
# Belajar match case di Python
# ==============================

# 1. Match case sederhana
status = "success"

match status:
    case "success":
        print("Operasi berhasil!")
    case "error":
        print("Terjadi error")
    case "pending":
        print("Masih dalam proses")
    case _:
        print("Status tidak dikenali")

# 2. Match dengan nilai
angka = 3

match angka:
    case 1:
        print("Satu")
    case 2:
        print("Dua")
    case 3:
        print("Tiga")  # Ini akan dieksekusi
    case 4 | 5 | 6:
        print("Empat, Lima, atau Enam")
    case _:
        print("Angka lain")

# 3. Match dengan kondisi
nilai = 85

match nilai:
    case n if n >= 90:
        print("Grade: A+")
    case n if n >= 80:
        print("Grade: A")  # Ini akan dieksekusi
    case n if n >= 70:
        print("Grade: B")
    case n if n >= 60:
        print("Grade: C")
    case _:
        print("Grade: D")

# 4. Match dengan list/tuple
data = ("admin", "1234")

match data:
    case ("admin", password):
        print(f"Login admin dengan password: {password}")
    case ("user", password):
        print(f"Login user dengan password: {password}")
    case _:
        print("Login gagal")