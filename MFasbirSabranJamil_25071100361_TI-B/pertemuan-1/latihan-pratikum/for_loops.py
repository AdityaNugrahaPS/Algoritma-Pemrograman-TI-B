# ==============================
# for_loops.py
# Belajar perulangan for di Python
# ==============================

# 1. Loop melalui string
for huruf in "Python":
    print(huruf)

# 2. Loop melalui list
buah = ["Apel", "Jeruk", "Mangga"]
for item in buah:
    print(f"Saya suka {item}")

# 3. Loop dengan range()
print("Angka 0-4:")
for i in range(5):
    print(i)

print("Angka 2-5:")
for i in range(2, 6):
    print(i)

print("Angka genap 0-10:")
for i in range(0, 11, 2):
    print(i)

# 4. Loop dengan break
for i in range(10):
    if i == 5:
        break
    print(i)

# 5. Loop dengan continue
for i in range(5):
    if i == 2:
        continue
    print(i)

# 6. Loop dengan else
for i in range(3):
    print(i)
else:
    print("Loop selesai")

# 7. Nested loop
for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")

# 8. Loop dengan enumerate()
buah = ["Apel", "Jeruk", "Mangga"]
for index, value in enumerate(buah):
    print(f"Index {index}: {value}")