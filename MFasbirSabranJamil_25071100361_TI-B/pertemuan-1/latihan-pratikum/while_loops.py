# ==============================
# while_loops.py
# Belajar perulangan while di Python
# ==============================

# 1. While loop dasar
i = 1
while i <= 5:
    print(f"Perulangan ke-{i}")
    i += 1

# 2. While dengan break
i = 1
while i <= 10:
    print(i)
    if i == 5:
        print("Berhenti di 5")
        break
    i += 1

# 3. While dengan continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        print("Lewati 3")
        continue
    print(i)

# 4. While dengan else
i = 1
while i <= 3:
    print(f"Iterasi {i}")
    i += 1
else:
    print("Perulangan selesai")

# 5. Contoh: Menghitung mundur
print("Hitung mundur:")
countdown = 5
while countdown > 0:
    print(countdown)
    countdown -= 1
print("GO!")

# 6. Contoh: Validasi input
password = ""
while password != "rahasia":
    password = input("Masukkan password: ")
print("Password benar!")