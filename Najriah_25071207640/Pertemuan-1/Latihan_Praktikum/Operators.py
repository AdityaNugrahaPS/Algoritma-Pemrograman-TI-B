#1. Arithmetic Operators
'''
Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum.
'''
x = 10
y = 4

print("--Arithmetic Operators--") #Menampilkan Header
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

'''
Python memiliki dua operator divisi:
/ - Divisi (mengembalikan float)
// - Pembagian lantai (mengembalikan bilangan bulat)
'''
x = 300
y = 10

print(x / y) #Divisi selalu mengembalikan float

'''
Pembagian lantai selalu mengembalikan bilangan bulat.
Ini membulatkan ke bawah bilangan bulat terdekat.
'''
x = 27
y = 5

print(x // y)

#2. Assignment Operator
'''
Operator penetapan digunakan untuk menetapkan nilai ke variabel.
'''

x = 5
x += 3

print("\n--Assignment Operators--")
print(x)

#The Walrus Operator
'''
Python mempunyain operator :=, yang dikenal sebagai "operator walrus". 
Ini menetapkan nilai ke variabel sebagai bagian dari ekspresi yang lebih besar
'''

numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 4:
    print(f"List has {count} elements")

#3. Comparison Operators
'''
Operator perbandingan digunakan untuk membandingkan dua nilai
Operator perbandingan mengembalikan Benar atau Salah berdasarkan perbandingan
'''

x = 5
y = 3

print("\n--Comparison Operators--") #Menampilkan header
print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

'''
Python memungkinkan untuk menggabungkan beberapa operator perbandingan dalam satu
baris kode agar lebih ringkas dan mudah dibaca.
'''

x = 8

print(3 < x < 10)
print(1 < x and x < 10)

#4. Logical Operators
'''
Operator logis digunakan untuk menggabungkan pernyataan bersyarat.
'''

x = 5

print("\n--Logical Operators--") #Menampilkan header
print(x > 0 and x < 10) #Uji apakah angka lebih besar dari 0 dan kurang dari 10

'''
Membalikkan hasil dengan not.
'''
x = 5

print(not(x > 3 and x < 10))

#5. Identity Operators
'''
Operator identitas digunakan untuk membandingkan objek, bukan jika mereka sama, 
tetapi jika mereka sebenarnya adalah objek yang sama, dengan lokasi memori yang sama
'''

x = ["Arum", "Endang"]
y = ["Arum", "Endang"]
z = x

print("\n--Identity Operators--") #Menampilkan header
print(x is z)
print(x is y)
print(x == y)

'''
Operator is not mengembalikan nilai True jika kedua variabel tidak menunjuk ke objek yang sama.
'''

x = ["Arum", "Endang"]
y = ["Arum", "Endang"]

print(x is not y)

'''
Perbedaan Antara is dan ==
is - Memeriksa apakah kedua variabel mengarah ke objek yang sama dalam memori
== - Memeriksa apakah nilai kedua variabel sama.
'''

x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

#6. Membership Operators
'''
Operator keanggotaan digunakan untuk menguji apakah urutan disajikan dalam objek.
'''

#Contoh 1
friends = ["amel", "endang", "arum"]

print("\n--Membership Operators--") #Menampilkan header
print("endang" in friends) #Memeriksa apakah "endang" ada dalam daftar

#Contoh 2
friends = ["amel", "endang", "arum"]

print("desty" not in friends) #Memeriksa apakah "desty" tidak ada dalam daftar

'''
Operator keanggotaan juga bisa digunakan dengan string
'''

text = "Hi guys"

print("H" in text)
print("guys" in text)
print("z" not in text)

#7. Bitwise Operators
'''
Operator Bitwise digunakan untuk membandingkan angka (biner)
'''

x = 5   # 0101
y = 3   # 0011

print(x & y)    # AND: 1 jika kedua bit bernilai 1
print(x | y)    # OR: 1 jika salah satu bit bernilai 1
print(x ^ y)    # XOR: 1 jika hanya salah satu bit bernilai 1
print(~x)       # NOT: membalik semua bit
print(x << 2)   # Shift kiri 2 bit (dikalikan 2^2)
print(x >> 2)   # Shift kanan 2 bit (dibagi 2^2)

#7. Operators Precedens
'''
Operstor prioritas menggambarkan urutan operasi dilakukan.
'''

#Dibawah ini beberapa contoh penggunaannya
x = 6
y = 3
data = [1, 2, 3]

print((x + y) * 2)      # Parentheses: mengatur urutan operasi
print(x ** y)           # Exponentiation: pangkat
print(x * y)            # Multiplication: perkalian
print(x // y)           # Floor division: pembagian dibulatkan ke bawah
print(x & y)            # Bitwise AND
print(x == y)           # Comparison: sama dengan
print(x in data)        # Membership: cek apakah x ada di data
