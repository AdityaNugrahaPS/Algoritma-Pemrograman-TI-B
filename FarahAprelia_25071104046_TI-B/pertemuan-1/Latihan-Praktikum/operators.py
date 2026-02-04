#ARITMETHIC OPERATORS

x = 19
y = 7

print(x + y) #Simbol + adalah operator penjumlahan
print(x - y) #Simbol - adalah operator pengurangan
print(x / y) #Simbol / adalah operator pembagian
print(x * y) #Simbol * adalah operator perkalian
print(x % y) #Simbol % adalah operator sisa
print(x ** y) #Simbol ** adalah operator pangkat
print(x // y) #Simbol // adalah operator pembulatan ke bawah atau floor

#ASIGGNMENT OPERATORS (Digunakan untuk menetapkan value ke dalam suatu variabel)

'''
OPERATOR    CONTOH          SAMA SEPERTI
=       	x = 4	        x = 4
+=	        x += 5	        x = x + 5
-=	        x -= 5	        x = x - 5	
*=	        x *= 6	        x = x * 6	
/=	        x /= 6	        x = x / 6	
%=	        x %= 7	        x = x % 7	
//=	        x //= 7	        x = x // 7
**=     	x **= 8	        x = x ** 8
&=	        x &= 8	        x = x & 8	
|=	        x |= 9	        x = x | 9	
^=	        x ^= 9	        x = x ^ 9	
>>=	        x >>= 3	        x = x >> 3	
<<=	        x <<= 3	        x = x << 3	
:=	        print(x := 2)	x = 2 print(x)
'''

#COMPARISON OPERATORS
'''
== (Sama besar dengan)
!= (Tidak sama besar dengan)
< (Lebih kecil dari)
> (Lebih besar dari)
<= (Lebih kecil atau sama dengan)
>= (Lebih besar atau sama dengan)
'''

x = 10
y = 5

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#LOGICAL OPERATORS

x = 5

print(x > 5 or x < 15)
print(x < 5 and x > 15)
print(not(x > 3 and x < 10))

'''
Floor =  pembulatan ke bawah
Ceiling = pembulatan ke atas
'''

#IDENTITY OPERATORS

'''
is (Mengembalikan True ketika kedua variabel menunjukkan ke arah objek yang memiliki lokasi memori yang sama)
is not (Mengembalikan True ketika kedua variabel bukan merupakan objek yang berada di memori yang sama)

Berbeda dengan == yang mengecek apakah value dalam suatu variabel sama
'''
x = ["apel", "pisang"]
y = ["apel", "pisang"]
z = x

print(x is z) #Mengembalikan True karena objek di dalam variabel x dan z terletak di lokasi memori yang sama
print(x is y) #Mengembalikan False karena kedua objek berada di lokasi memori yang berbeda, walau isinya sama persis sekalipun
print(x == y) #Mengembalikan True karena isi kedua objek sama walaupun lokasi memorinya, berbeda dengan is yang harus sama pula lokasi memorinya

x = ["apel", "pisang"]
y = ["apel", "pisang"]

print(x is not y) #Mengembalikan True karena walaupun valuenya sama, namun berada di lokasi memori yang berbeda

#MEMBERSHIP OPERATORS

'''
in (Mengembalikan True jika value yang dimaksud terdaftar ke dalam objek secara spesifik)
not in (Mengembalikan True jika value yang dimaksud tidak terdaftar ke dalam objek secara spesifik)
'''

buah = ["apel", "pisang", "ceri"]
print("pisang" in buah) #Mengembalikan True karena pisang terdefinisi sebelumnya

buah = ["apel", "pisang", "ceri"]
print("nanas" not in buah) #Mengembalikan True karena nanas tidak terdefinisi sebelumnya

#BITWISE OPERATORS

'''
&    AND                                            Mengatur setiap bit menjadi 1 jika kedua bit adalah 1                                                       x & y
|    OR                                             Mengatur setiap bit menjadi 1 jika salah satu dari dua bit adalah 1                                         x | y
^    XOR                                            Mengatur setiap bit menjadi 1 jika hanya satu dari dua bit yang adalah 1                                    x ^ y
~    NOT                                            Membalikkan semua bit                                                                                       ~x
<<   Pergeseran ke kiri dengan pengisian nol        Geser ke kiri dengan memasukkan nol dari kanan dan biarkan bit paling kiri hilang                           x << 2
>>   Pergeseran ke kanan dengan tanda               Geser ke kanan dengan memasukkan salinan bit paling kiri dari kiri, dan biarkan bit paling kanan hilang     x >> 2
'''

#OPERATORS PRECEDENCE

'''
()                  Tanda kurung
**                  Perpangkatan
+x -x ~x            Plus unary, minus unary, dan NOT bitwise
* / // %            Perkalian, pembagian, pembagian lantai, dan modulus
+ -                 Penjumlahan dan pengurangan
<< >>               Pergeseran bitwise kiri dan kanan
&                   AND bitwise
^                   XOR bitwise
|                   OR bitwise
== != > >= < <=     Operator perbandingan, identitas, dan keanggotaan
not                 NOT logis
and                 AND
or                  OR
'''