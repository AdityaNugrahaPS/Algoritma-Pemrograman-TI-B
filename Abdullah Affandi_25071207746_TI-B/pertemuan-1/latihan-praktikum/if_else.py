"""
Python conditional (if-else)
"""

# 1. If sederhana
nilai = 85
print("1. If sederhana:")
if nilai >= 75:
    print("Anda lulus!")

# 2. If-else
nilai = 65
print("\n2. If-else:")
if nilai >= 75:
    print("Anda lulus!")
else:
    print("Anda tidak lulus!")

# 3. If-elif-else
nilai = 90
print("\n3. If-elif-else:")
if nilai >= 90:
    print("Nilai Anda A")
elif nilai >= 80:
    print("Nilai Anda B")
elif nilai >= 70:
    print("Nilai Anda C")
else:
    print("Nilai Anda D")

# 4. Nested if (if bersarang)
umur = 20
nilai = 85
print("\n4. Nested if (if bersarang):")
if umur >= 18:
    print("Anda sudah dewasa")
    if nilai >= 75:
        print("Dan Anda lulus")
    else:
        print("Tapi Anda tidak lulus")
else:
    print("Anda belum dewasa")

# 5. If dengan operator logika (and)
username = "admin"
password = "12345"
print("\n5. If dengan operator logika (and):")
if username == "admin" and password == "12345":
    print("Login berhasil")
else:
    print("Login gagal")

# 6. If dengan operator logika (or)
cuaca = "hujan"
print("\n6. If dengan operator logika (or):")
if cuaca == "hujan" or cuaca == "mendung":
    print("Bawa payung")
else:
    print("Cuaca cerah")

# 7. If dengan operator logika (not)
online = False
print("\n7. If dengan operator logika (not):")
if not online:
    print("Status offline")
else:
    print("Status online")

# 8. If dengan operator perbandingan
angka = 15
print("\n8. If dengan operator perbandingan:")
if angka > 10 and angka < 20:
    print(f"{angka} berada di antara 10 dan 20")

# 9. If dengan operator keanggotaan (in)
buah = ["apel", "jeruk", "mangga"]
print("\n9. If dengan operator keanggotaan (in):")
if "jeruk" in buah:
    print("Jeruk ada dalam daftar buah")

# 10. If dengan operator identitas (is)
a = [1, 2, 3]
b = [1, 2, 3]
c = a
print("\n10. If dengan operator identitas (is):")
if a is c:
    print("a dan c adalah objek yang sama")
if a is not b:
    print("a dan b adalah objek berbeda")

# 11. Ternary operator (one-liner if-else)
nilai = 80
status = "Lulus" if nilai >= 75 else "Tidak Lulus"
print(f"\n11. Ternary operator: {status}")

# 12. If dengan kondisi kompleks
usia = 25
pekerjaan = "mahasiswa"
print("\n12. If dengan kondisi kompleks:")
if (usia >= 18 and usia <= 30) and (pekerjaan == "mahasiswa" or pekerjaan == "pelajar"):
    print("Anda termasuk dalam kategori pemuda pelajar")

# 13. If dengan kondisi string
nama = "Abdullah"
print("\n13. If dengan kondisi string:")
if len(nama) > 5:
    print(f"Nama {nama} tergolong panjang")
else:
    print(f"Nama {nama} tergolong pendek")

# 14. If dengan kondisi list
angka_list = [1, 2, 3, 4, 5]
print("\n14. If dengan kondisi list:")
if len(angka_list) > 3:
    print(f"List memiliki lebih dari 3 elemen: {len(angka_list)} elemen")

# 15. If dengan kondisi boolean
is_student = True
is_working = False
print("\n15. If dengan kondisi boolean:")
if is_student and not is_working:
    print("Mahasiswa aktif yang tidak sedang bekerja")

# 16. Elif untuk mengecek banyak kondisi
suhu = 30
print("\n16. Elif untuk mengecek banyak kondisi:")
if suhu < 0:
    print("Sangat dingin")
elif suhu < 20:
    print("Dingin")
elif suhu < 30:
    print("Hangat")
elif suhu < 40:
    print("Panas")
else:
    print("Sangat panas")

# 17. If dengan fungsi
def cek_bilangan(angka):
    if angka > 0:
        return "Positif"
    elif angka < 0:
        return "Negatif"
    else:
        return "Nol"

print(f"\n17. If dengan fungsi: {cek_bilangan(-5)}")

# 18. If untuk validasi input
input_angka = "123"
print("\n18. If untuk validasi input:")
if input_angka.isdigit():
    print(f"Input adalah angka: {int(input_angka)}")
else:
    print("Input bukan angka")

# 19. If dengan kondisi range
angka = 25
print("\n19. If dengan kondisi range:")
if angka in range(20, 30):
    print(f"{angka} berada dalam range 20-29")

# 20. Pass
angka = 1
print("\n20. If dengan pass:")
if angka > 0:
    pass  # Tidak melakukan apa-apa jika kondisi terpenuhi
else:
    print("Angka tidak positif")