"""
Python for loops
"""

# 1. For loop dengan list
buah = ["apel", "jeruk", "mangga", "pisang"]
print("1. For loop dengan list:")
for item in buah:
    print(f"Buah: {item}")

# 2. For loop dengan string
kata = "Python"
print("\n2. For loop dengan string:")
for huruf in kata:
    print(f"Huruf: {huruf}")

# 3. For loop dengan range()
print("\n3. For loop dengan range():")
for i in range(5):  # Mencetak angka 0 sampai 4
    print(f"Angka: {i}")

# 4. For loop dengan range(start, stop)
print("\n4. For loop dengan range(start, stop):")
for i in range(2, 8):  # Mencetak angka 2 sampai 7
    print(f"Angka: {i}")

# 5. For loop dengan range(start, stop, step)
print("\n5. For loop dengan range(start, stop, step):")
for i in range(1, 10, 2):  # Mencetak angka ganjil dari 1 sampai 9
    print(f"Angka: {i}")

# 6. For loop dengan indeks menggunakan enumerate()
print("\n6. For loop dengan enumerate():")
for indeks, item in enumerate(buah):
    print(f"Indeks {indeks}: {item}")

# 7. For loop dengan tuple
koordinat = [(1, 2), (3, 4), (5, 6)]
print("\n7. For loop dengan tuple:")
for x, y in koordinat:
    print(f"Koordinat: ({x}, {y})")

# 8. For loop bersarang (nested for loop)
print("\n8. For loop bersarang:")
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 9. For loop dengan dictionary
data_mahasiswa = {"nama": "Abdullah", "jurusan": "TI"}
print("\n9. For loop dengan dictionary:")
for kunci, nilai in data_mahasiswa.items():
    print(f"{kunci}: {nilai}")

# 10. For loop dengan set
warna = {"merah", "hijau", "biru"}
print("\n10. For loop dengan set:")
for w in warna:
    print(f"Warna: {w}")

# 11. For loop dengan fungsi zip() untuk menggabungkan dua list
nama = ["Andi", "Budi", "Citra"]
umur = [20, 22, 21]
print("\n11. For loop dengan zip():")
for n, u in zip(nama, umur):
    print(f"{n} berumur {u} tahun")

# 12. For loop dengan break
print("\n12. For loop dengan break:")
for i in range(10):
    if i == 5:
        break
    print(f"Angka: {i}")

# 13. For loop dengan continue
print("\n13. For loop dengan continue:")
for i in range(7):
    if i == 3:
        continue
    print(f"Angka: {i}")

# 14. For loop dengan else
print("\n14. For loop dengan else:")
for i in range(3):
    print(f"Angka: {i}")
else:
    print("Loop selesai tanpa break")

# 15. For loop untuk membuat list baru (list comprehension)
kuadrat = [x**2 for x in range(1, 6)]
print(f"\n15. List comprehension hasil: {kuadrat}")

# 16. For loop dengan reversed()
print("\n16. For loop dengan reversed():")
for i in reversed(range(5)):
    print(f"Angka terbalik: {i}")

# 17. For loop dengan sorted()
angka_acak = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\n17. For loop dengan sorted(): {angka_acak}")
for angka in sorted(angka_acak):
    print(f"Angka terurut: {angka}")

# 18. For loop dengan sorted() terbalik
print("\n18. For loop dengan sorted() terbalik:")
for angka in sorted(angka_acak, reverse=True):
    print(f"Angka terurut terbalik: {angka}")

# 19. For loop untuk iterasi dengan indeks tertentu
print("\n19. For loop untuk iterasi dengan indeks tertentu:")
for i in range(len(buah)):
    print(f"Buah ke-{i}: {buah[i]}")

# 20. For loop dengan fungsi len() dan range()
print("\n20. For loop dengan len() dan range():")
for i in range(len(kata)):
    print(f"Huruf ke-{i}: {kata[i]}")