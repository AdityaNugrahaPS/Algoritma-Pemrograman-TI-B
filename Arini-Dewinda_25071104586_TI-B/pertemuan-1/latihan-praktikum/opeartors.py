#operator

"""
operator digunakan untuk melakukan operasi pada variabel dan nilai.
"""

#operator aritmatika: melakukan operasi matematika

a = 10
b = 3

print(a + b) #penjumlahan
print(a - b) #pengurangan
print(a * b) #perkalian
print(a / b) #pembagian
print(a % b) #sisa bagi

#assignment operator: memberi nilai ke variabel

x = 5
x += 3
x *= 2

print(x)

#operator perbandingan: membandingkan dua nilai

tinggi = 186

print(tinggi > 160)
print(tinggi == 184)
print(tinggi != 173)

#operator logika

capek = 90
ngantuk = True

if capek > 80 and ngantuk : #operator AND bernilai true jika kedua value true
    print("Kamu butuh tidur!") 

if capek > 80 or ngantuk : #operator OR bernilai true jika salah satu value true
    print("Kamu butuh istirahat!")

if not capek : #operator NOT membalikkan nilai, jika true maka false
    print("Jangan malas!")

#identity operator: mengecek apakah dua variabel menunjuk ke objek yang sama

a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)
print(a is c)

#membership opeartor: mengecek keberadaan kata

kata = "risol mayo lezat"

print("risol" in kata)
print("mayo" not in kata)

#bitwise operator: digunakan untuk operasi biner

x = 5   # 101
y = 3   # 011

print(x & y)
print(x | y)

#operator precedence: menentukan urutan eksekusi operator

hasil = 10 + 2 * 3
print(hasil)











