"""
Python operators
"""

# 1. Operator Aritmatika
print("1. Operator Aritmatika:")
a = 10
b = 3
print(f"Penjumlahan: {a} + {b} = {a + b}")
print(f"Pengurangan: {a} - {b} = {a - b}")
print(f"Perkalian: {a} * {b} = {a * b}")
print(f"Pembagian: {a} / {b} = {a / b}")
print(f"Modulus: {a} % {b} = {a % b}")
print(f"Pangkat: {a} ** {b} = {a ** b}")
print(f"Pembagian bulat: {a} // {b} = {a // b}")

# 2. Operator Perbandingan
print("\n2. Operator Perbandingan:")
x = 5
y = 8
print(f"Sama dengan: {x} == {y} adalah {x == y}")
print(f"Tidak sama dengan: {x} != {y} adalah {x != y}")
print(f"Lebih besar: {x} > {y} adalah {x > y}")
print(f"Lebih kecil: {x} < {y} adalah {x < y}")
print(f"Lebih besar atau sama: {x} >= {y} adalah {x >= y}")
print(f"Lebih kecil atau sama: {x} <= {y} adalah {x <= y}")

# 3. Operator Logika
print("\n3. Operator Logika:")
p = True
q = False
print(f"AND: {p} and {q} adalah {p and q}")
print(f"OR: {p} or {q} adalah {p or q}")
print(f"NOT: not {p} adalah {not p}")

# 4. Operator Penugasan
print("\n4. Operator Penugasan:")
c = 15
print(f"c = {c}")
c += 5
print(f"c += 5, maka c = {c}")
c -= 3
print(f"c -= 3, maka c = {c}")
c *= 2
print(f"c *= 2, maka c = {c}")
c /= 4
print(f"c /= 4, maka c = {c}")

# 5. Operator Identitas
print("\n5. Operator Identitas:")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print(f"list1 is list2: {list1 is list2}")  # False karena objek berbeda
print(f"list1 is list3: {list1 is list3}")  # True karena referensi sama
print(f"list1 is not list2: {list1 is not list2}")  # True karena objek berbeda

# 6. Operator Keanggotaan
print("\n6. Operator Keanggotaan:")
buah = ["apel", "jeruk", "mangga"]
print(f"'jeruk' in buah: {'jeruk' in buah}")  # True
print(f"'pisang' not in buah: {'pisang' not in buah}")  # True

# 7. Operator Bitwise
print("\n7. Operator Bitwise:")
m = 6  # dalam biner: 110
n = 2  # dalam biner: 010
print(f"AND bitwise: {m} & {n} = {m & n}")  # 010 = 2
print(f"OR bitwise: {m} | {n} = {m | n}")  # 110 = 6
print(f"XOR bitwise: {m} ^ {n} = {m ^ n}")  # 100 = 4
print(f"NOT bitwise: ~{m} = {~m}")  # -(6+1) = -7
print(f"Left shift: {m} << 1 = {m << 1}")  # 1100 = 12
print(f"Right shift: {m} >> 1 = {m >> 1}")  # 011 = 3

# 8. Kombinasi operator dalam ekspresi
print("\n8. Kombinasi operator dalam ekspresi:")
hasil = (a + b) * x - y / 2
print(f"({a} + {b}) * {x} - {y} / 2 = {hasil}")

# 9. Operator dalam konteks boolean
print("\n9. Operator dalam konteks boolean:")
nilai = 85
lulus = nilai >= 75
print(f"Jika nilai = {nilai}, maka lulus = {lulus}")

# 10. Operator ternary (conditional expression)
print("\n10. Operator ternary:")
status = "Lulus" if nilai >= 75 else "Tidak Lulus"
print(f"Status: {status}")