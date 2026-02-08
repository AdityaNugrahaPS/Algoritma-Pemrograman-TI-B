# Buat sebuah program Python yang:
# 1. Menyimpan sebuah nilai ujian (0–100) ke dalam variabel
# 2. Jika nilai lebih besar atau sama dengan 60, tampilkan:
# Lulus
# Jika nilai kurang dari 60, tampilkan:
# Tidak Lulus

import random

nilai = random.randint(1,100) # Memasukkan Bilangan Bulat secara acak ke dalam nilai
print("Nilai:", nilai)

if nilai >= 60:
    print("Selamat, Anda Lulus!")
else:
    print("Maaf, Anda tidak Lulus")
