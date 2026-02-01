# ==============================
# booleans.py
# Belajar boolean di Python
# ==============================

# 1. Boolean values
benar = True
salah = False
print(benar)   # True
print(salah)   # False

# 2. Evaluasi ekspresi
print(10 > 5)   # True
print(10 == 5)  # False
print(10 < 5)   # False

# 3. Boolean dalam if statement
x = 10
y = 5

if x > y:
    print("x lebih besar dari y")  # Ini akan dieksekusi

# 4. Fungsi bool()
print(bool("Hello"))  # True
print(bool(15))       # True
print(bool(0))        # False
print(bool(""))       # False
print(bool([]))       # False
print(bool({}))       # False

# 5. Operasi logika
a = True
b = False

print(a and b)   # False
print(a or b)    # True
print(not a)     # False

# 6. Contoh gampang
usia = 18
punya_ktp = True

if usia >= 17 and punya_ktp:
    print("Bisa membuat SIM")
else:
    print("Belum bisa membuat SIM")