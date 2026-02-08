# Arithmetic operators
x = 35
y = 8
print("-Operator aritmatika-")
print(x + y) # Penambahan
print(x - y) # Pengurangan
print(x * y) # Perkalian
print(x / y) # Pembagian
print(x % y) # Modulus
print(x ** y) # Eksponen / pangkat
print(x // y) # Pembagian dibulatkan
print(" ")

# Assignment operators
print("-Assignment operators-")
x = 13
x += 5; print(x)
x -= 5; print(x)
x *= 5; print(x)
x /= 5; print(x)
x %= 5; print(x)
x //= 5; print(x)
x **= 5; print(x)
print(" ")

# Comparison operators
print("-Operator perbandingan-")
x = 5
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)
print(" ")

# Logical operators
print("-Operator logis-")
x = 5
print(x > 0 and x < 10)
print(x > 0 or x < 10)
print(not(x > 3 and x < 10))
print(' ')

# Identity operators
print("-Operator identitas-")
x = ["kucing", "anjing"]
y = ["kucing", "anjing"]
z = x
print(x is y) # is memeriksa apakah kedua variabel tertuju pada objek yang sama
print(x == y) # == memerksa apakah kedua variabel setara
print(x is z)
print(" ")

# Membership operators
print("-Membership operators-")
taman = ["pohon", "kolam", "lampu"]
print("kolam" in taman) # in memeriksa jika "kolam" termasuk dalam taman dan mengeluarkan  nilai True jika benar
print("bangku" not in taman) # not in memeriksa jika "bangku" tidak termasuk dalam taman dan mengeluarkan nilaik True jika benar