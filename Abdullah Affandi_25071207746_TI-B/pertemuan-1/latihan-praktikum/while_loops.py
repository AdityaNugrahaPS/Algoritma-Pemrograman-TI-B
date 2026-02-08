"""
Python while loops
"""

# 1. While loop sederhana
print("1. While loop sederhana:")
i = 1
while i <= 5:
    print(f"Angka: {i}")
    i += 1

# 2. While loop dengan break
print("\n2. While loop dengan break:")
j = 1
while j <= 10:
    print(f"Angka: {j}")
    if j == 5:
        break
    j += 1

# 3. While loop dengan continue
print("\n3. While loop dengan continue:")
k = 0
while k < 5:
    k += 1
    if k == 3:
        continue
    print(f"Angka: {k}")

# 4. While loop dengan else
print("\n4. While loop dengan else:")
l = 1
while l <= 3:
    print(f"Angka: {l}")
    l += 1
else:
    print("Loop selesai!")

# 5. While loop untuk validasi input
print("\n5. While loop untuk validasi input:")
password = ""
while password != "python123":
    password = input("Masukkan password (ketik 'python123' untuk lanjut): ")
    if password != "python123":
        print("Password salah, coba lagi!")
print("Password benar!")

# 6. While loop untuk counter mundur
print("\n6. While loop untuk counter mundur:")
counter = 5
while counter > 0:
    print(f"Hitung mundur: {counter}")
    counter -= 1
print("Selesai!")

# 7. While loop dengan kondisi boolean
print("\n7. While loop dengan kondisi boolean:")
game_active = True
score = 0
while game_active:
    score += 10
    print(f"Score: {score}")
    if score >= 50:
        game_active = False
print("Game selesai!")

# 8. While loop untuk menghitung jumlah
print("\n8. While loop untuk menghitung jumlah:")
angka = 1
jumlah = 0
while angka <= 10:
    jumlah += angka
    angka += 1
print(f"Jumlah dari 1 sampai 10: {jumlah}")

# 9. While loop untuk mencari elemen
print("\n9. While loop untuk mencari elemen:")
daftar = ["apel", "jeruk", "mangga", "pisang"]
cari = "mangga"
indeks = 0
ditemukan = False

while indeks < len(daftar) and not ditemukan:
    if daftar[indeks] == cari:
        ditemukan = True
        print(f"{cari} ditemukan di indeks {indeks}")
    indeks += 1

if not ditemukan:
    print(f"{cari} tidak ditemukan dalam daftar")

# 10. Nested while loop
print("\n10. Nested while loop:")
baris = 1
while baris <= 3:
    kolom = 1
    while kolom <= 3:
        print(f"({baris},{kolom})", end=" ")
        kolom += 1
    print()  # Baris baru
    baris += 1