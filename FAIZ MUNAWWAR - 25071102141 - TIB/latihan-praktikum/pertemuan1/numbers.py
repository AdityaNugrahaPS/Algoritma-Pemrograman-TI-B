# Ada tiga type number yaitu:
x = 10    # int
y = 23.5  # float
z = 32e1   # complex

# Mengubah dari integer menjadi float
a = float(x)

# Mengubah Float menjadi integer
b = int(y)

# Mengubah integer menjadi complex
c = complex(x)

# Mengprint hasil yang telah di ubah
print(a)
print(b)
print(c)

# Untuk menunjukkan type number setelah di ubah
print(type(a))
print(type(b))
print(type(c))

# Python juga memiliki modul untuk memanggil angka secara acak (Random Number)
import random

print(random.randrange(1, 10))