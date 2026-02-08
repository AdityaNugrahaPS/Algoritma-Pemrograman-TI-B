#python operators
    #aritmatika
a = 15
b = 4
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
print(a // b)

    #assignment operator
a = 15
b = 4
a += b
print(a)
a -= b
print(a)
a *= b
print(a)
a /= b
print(a)

    #comparison operator
x = 5
y = 3
print(x == y)   #sama dengan
print(x != y)   #tidak sama dengan
print(x > y)    #lebih dari/besar dari
print(x < y)    #kurang dari/kecil dari
print(x >= y)   #besar dari sama dengan
print(x <= y)   #kecil dari sama dengan

#logical operator
'''
Operator	Deskripsi
and	        Mengembalikan True jika kedua pernyataan bernilai True
or	        Mengembalikan True jika salah satu pernyataan bernilai True
not	        Membalikkan hasil, mengembalikan False jika hasilnya True
'''
x = 5
print(x > 0 and x < 10)

x = 5
print(x < 5 or x > 10)

#identity operator
'''
Operator	Deskripsi	
is	        Mengembalikan True jika kedua variabel menunjuk ke objek yang sama	
is not	    Mengembalikan True jika kedua variabel tidak menunjuk ke objek yang sama
'''
a = [1, 2]
b = [1, 2]
print(a == b)   #true (nilainya sama)
print(a is b)   #false (objek berbeda)

#membership operator
'''
Operator	Deskripsi	Contoh
in	        Mengembalikan True jika suatu nilai ada di dalam objek/urutan (sequence)	
not in	    Mengembalikan True jika suatu nilai tidak ada di dalam objek/urutan (sequence)
'''
teks = "Python"
print("P" in teks)      # True
print("z" not in teks)  # True

#bitwise operator
#menggunakan binary
print(6 & 3)
print(6 | 3)
print(6 ^ 3)

#precedence operator
#urutan prioritas operator yang menentukan operator mana yang dihitung lebih dulu dalam sebuah ekspresi.
'''
urutan operator
()                      → Tanda kurung
**                      → Pangkat
+x, -x, ~x              → Unary operator
*, /, //, %             → Perkalian & pembagian
+, -                    → Penjumlahan & pengurangan
<<, >>                  → Bitwise shift
&                       → Bitwise AND
^                       → Bitwise XOR
|                       → Bitwise OR
==, !=, >, <, >=, <=    → Perbandingan
not                     → Logika NOT
and                     → Logika AND
or                      → Logika OR
= , +=, -=, dll         → Assignment
'''
print((6 + 3) - (6 + 3))    #dalam kurung kemudian dijumlahkan
print(100 + 5 * 3)          #perkalian kemudian penjumlahan
