## A. Operator aritmatika
a = 10
b = 5
print("Penjumlahan:", a + b)         #output: 15
print("Pengurangan:", a - b)         #output: 5
print("Perkalian:", a * b)           #output: 50
print("Pembagian:", a / b)           #output: 2.0
print("Pembagian (floor):", a // b)  #output: 2
print("Modulus:", a % b)             #output: 0
print("Pangkat:", a ** b)            #output: 100000

# perbedaan pembagian (/) dan pembagian floor (//)
c = 7
d = 3
print("Pembagian:", c / d)           #output: 2.3333333333333335
print("Pembagian (floor):", c // d)  #output: 2  dibulathkan ke bawah



## B. Assignment Operators
x = 10
print("Nilai awal x:", x)  #output: 10
print("x += 5:", x := x + 5)  #output: 15
print("x -= 3:", x := x - 3)  #output: 12
print("x *= 2:", x := x * 2)  #output: 24
print("x /= 4:", x := x / 4)  #output: 6.0
print("x //= 2:", x := x // 2)  #output: 3.0
print("x %= 2:", x := x % 2)  #output: 1.0
print("x **= 3:", x := x ** 3)  #output: 1.0



## C. Operator perbandingan
x = 10
y = 5
print("x == y:", x == y)   #output: False
print("x != y:", x != y)   #output: True
print("x > y:", x > y)     #output: True
print("x < y:", x < y)     #output: False
print("x >= y:", x >= y)   #output: True
print("x <= y:", x <= y)   #output: False


## D. Operator Logika
a = True
b = False
print("a and b:", a and b)   #output: False
print("a or b:", a or b)     #output: True
print("not a:", not a)       #output: False
print("not b:", not b)       #output: True


## E. Operator Identitas
x = [1, 2, 3]
y = x
z = [1, 2, 3]  
print("x is y:", x is y)          #output: True
print("x is z:", x is z)          #output: False
print("x is not z:", x is not z)  #output: True


## F. Operator Keanggotaan
buah = ['apel', 'jeruk', 'mangga']
print("ada apel dalam buah:", 'apel' in buah)         #output: True
print("ada pisang dalam buah:", 'pisang' in buah)     #output: False
print("ada pisang dala buah:", 'pisang' not in buah)  #output: True

## G. Prioritas Operator
# Prioritas operator menentukan urutan evaluasi dalam sebuah ekspresi
# Berikut adalah urutan prioritas operator dari yang tertinggi hingga terendah:
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication *, Division /, Floor Division //, Modulus %
# 4. Addition +, Subtraction -
# 5. Comparison Operators (==, !=, >, <, >=, <=)
# 6. Logical NOT not
# 7. Logical AND and
# 8. Logical OR or