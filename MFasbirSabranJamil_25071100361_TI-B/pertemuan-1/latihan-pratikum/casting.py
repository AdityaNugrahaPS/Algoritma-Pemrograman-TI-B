# ==============================
# casting.py
# Belajar casting (konversi tipe) di Python
# ==============================

# 1. Casting ke integer
x = int(3.14)      # 3
y = int("100")     # 100
z = int(True)      # 1
print(f"int(3.14) = {x}")
print(f"int('100') = {y}")
print(f"int(True) = {z}")

# 2. Casting ke float
a = float(10)      # 10.0
b = float("3.14")  # 3.14
c = float(False)   # 0.0
print(f"float(10) = {a}")
print(f"float('3.14') = {b}")
print(f"float(False) = {c}")

# 3. Casting ke string
d = str(100)       # "100"
e = str(3.14)      # "3.14"
f = str(True)      # "True"
print(f"str(100) = '{d}'")
print(f"str(3.14) = '{e}'")
print(f"str(True) = '{f}'")

# 4. Casting ke boolean
g = bool(1)        # True
h = bool(0)        # False
i = bool("Hello")  # True
j = bool("")       # False
print(f"bool(1) = {g}")
print(f"bool(0) = {h}")
print(f"bool('Hello') = {i}")
print(f"bool('') = {j}")

# 5. Contoh gampang
angka_string = "50"
angka_integer = int(angka_string)
hasil = angka_integer * 2
print(f"{angka_string} * 2 = {hasil}")