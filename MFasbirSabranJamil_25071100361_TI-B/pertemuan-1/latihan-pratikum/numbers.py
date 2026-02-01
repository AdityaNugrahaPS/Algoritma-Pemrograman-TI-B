# ==============================
# numbers.py
# Belajar angka di Python
# ==============================

# 1. Integer
x = 10
y = -5
z = 0
print(f"x = {x}, y = {y}, z = {z}")

# 2. Float
a = 3.14
b = -2.5
c = 4.0
print(f"a = {a}, b = {b}, c = {c}")

# 3. Complex
d = 3 + 5j
e = 2j
f = -1j
print(f"d = {d}, e = {e}, f = {f}")

# 4. Konversi tipe
g = 10      # int
h = float(g)  # menjadi float
i = complex(g)  # menjadi complex
print(f"g = {g}, h = {h}, i = {i}")

# 5. Operasi matematika
num1 = 20
num2 = 3

print(f"Penjumlahan: {num1} + {num2} = {num1 + num2}")
print(f"Pengurangan: {num1} - {num2} = {num1 - num2}")
print(f"Perkalian: {num1} * {num2} = {num1 * num2}")
print(f"Pembagian: {num1} / {num2} = {num1 / num2}")
print(f"Pembagian bulat: {num1} // {num2} = {num1 // num2}")
print(f"Modulus: {num1} % {num2} = {num1 % num2}")
print(f"Pangkat: {num1} ** {num2} = {num1 ** num2}")

# 6. Random number
import random
print(f"Angka random 1-10: {random.randint(1, 10)}")