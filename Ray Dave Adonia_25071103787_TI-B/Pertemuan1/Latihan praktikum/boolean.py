# Boolean values
print("-Boolean_")
print(1 > 2) # Terdiri dari True atau False.
print(1 == 2)
print(1 < 2)
print(" ")

## Dengan kondisi
x = 10
y = 20
if x > y:
    print("x lebih besar dari y.")
else:
    print("y tidak lebih besar dari y.")
print(" ")

# Evaluate value and variables
## True
print("Untuk True:")
x = 3
y = "Ayam"
print(bool(x)) # Semua angka selain 0 bernilai True
print(bool(y)) # String bernilai True, kecuali jika string itu kosong
# List, tuple, set, dan dictionary bernilai True, kecuali jika kosong
print(bool("abc"))
print(bool(222))
print(bool([1, 2, 3]))
print(" ")

## False
print("Untuk False:")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool())
print(bool([]))
print(bool(()))
print(bool({}))