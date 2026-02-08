#arithmatic operators
x = 15
y = 5

print(x + y) #tanda + adalah operator penjumlahan
print(x - y) #tanda - adalah operator pengulangan
print(x * y) #tanda * adalah operator perkalian
print(x / y) #tanda / adalah operator pembagian
print(x % y) #tanda % adalah operator sisa hasil bagi
print(x ** y) #tanda ** adalah operator pangkat
print(x // y) #tanda // adalah opetor pembulatan kebawah atau floor

#assignment operators
print(x = 3)

x = 5
x += 3 #assignment menggunakan operasi aritmatika +
print(x) 

y = 10
y -= 5 #assignment menggunakan operasi aritmatika -
print(y)

z = 15
z *= 7 #assignment menggunakan operasi aritmatika *
print(z)

a = 25
a /= 5 #assignment menggunakan operasi aritmatika /
print(a)

b = 37
b //= 3 #assignment menggunakan operasi aritmatika //
print(b)

c = 17
c %= 2 #assignment menggunakan operasi aritmatika %
print(c)


d = 24
d **= 2 #assignment menggunakan operasi aritmatika **
print(d)

x = 5
x &= 3 #assignment menggunakan operator bitwise &
print(x)

y = 7
y |= 5 #assignment menggunakan operator bitwise |
print(y)

z = 9
z ^= 3 #assignment menggunakan operator bitwise ^
print(z)

a = 15
a >>= 3 #assignment menggunakan operator bitwise >>
print(a)

b = 25
b <<= 5 #assignment menggunakan operator bitwise <<
print(b)

c = 17
print(c := 3) #assignment menggunakan walrus operator

#comparison operators
x = 7
y = 3

print(x == y) #menyatakan apakah x sama besarnya atau nilainya dengan y
print(x != y) #menyatakan bahwa nilai x tidak sama dengan y
print(x > y) #menyatakan apakah x lebih besar dari y
print(x < y) #menyatakan apakah x lebih kecil dari y
print(x >= y) #menyatakan apakah x lebih besar atau sama dengan y
print(x <= y) #menyatakan apakah x lebih kecil atau sama dengan y

#logical operators
print(x > 5 or x > 10) #bernilai benar jika kedua pernyataan benar
print(x < 5 and x > 10) #bernilai benar jika salah satu pernyataan benar
print(not(x > 7 and x < 10)) #membalikkan hasil, jika pernyataan benar maka bernilai False

#identity operators
# 1. oprator is (True apabila kedua variabel menunjuk pada objek yang sama)
a = [1,2,3]
b = a
c = [1,2,3]

print(a is b) #menyatakan True karena a dan b menunjuk pada isi dan objek yang sama
print(a is c) #menyatakan False karena karena menunjuk pada objek yang berbeda
print(a == c) #menyatakan True karena a bernilai sama dengan c

# 2. operator is not (True jika kedua variabel tidak menunjuk pada objek yang sama)
print(a is not c)
print(b is not c)

#membership operators
hero = ["Phainon", "Stelle", "Cyrene"]
print("Cyrene" in hero) #menyatakan Cyrene terdapat dalam objek hero
print("Lygus" not in hero) #menyatakan Lygus tidak terdapat dalam objek hero

#bitwise operators
print(5 & 3) #operator & hasilnya 1 jika dua-duanya 1
print(5 | 3) #operator | hasilnya 1 jika salah satunya 1
print(5 ^ 3) #operator ^ hasilnya 1 jika berbeda
print(~5) #operator ~ membalikkan semua bit
print(5 << 1) #operator << menggeser bit kekiri (dikali 2)
print(5 >> 1) #operator >> menggeser bit kekanan (dibagi 2)

#operator precedence
print((3+5)-(3+5)) #tanda kurung menjadi prioritas eksekusi
print(2 + 3 * 4) #perkalian dikerjakan lebih dulu
print(5 + 3 << 1) #penjumlahan dikerjakan lebih dahulu
print(3 + 5 - 5 + 6) #urutan penjumlahan dan pengurangan sama, maka langsung eksekusi dari kiri ke kanan

#urutan prioritas
print("()", "**", "+,-,~", "*, /, //, %", "+,-", "<<, >>", "&", "^", "|", "== != > < >= <=", "not", "and", "or") #tanda kurung, pangkat, unary +,-,~, kali, bagi, floor, sisa hasil bagi, penjumlahan dan pengurangan, bitwise shift, bitwise and, bitwise xor, bitwise or, perbandingan, logical not, and, or