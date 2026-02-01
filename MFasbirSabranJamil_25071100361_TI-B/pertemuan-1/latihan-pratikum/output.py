# ==============================
# output.py
# Belajar output di Python
# ==============================

# 1. Output dasar dengan print()
print("Selamat belajar Python!")

# 2. Print beberapa variabel
nama = "Fasbir"
umur = 19
print("Nama:", nama, "Umur:", umur)

# 3. Print dengan separator
print("Apel", "Jeruk", "Mangga", sep=", ")

# 4. Print tanpa newline (end parameter)
print("Hello ", end="")
print("World!")

# 5. Format string dengan f-string
print(f"Nama: {nama}, Umur: {umur} tahun")

# 6. Format string dengan .format()
print("Nama: {}, Umur: {}".format(nama, umur))