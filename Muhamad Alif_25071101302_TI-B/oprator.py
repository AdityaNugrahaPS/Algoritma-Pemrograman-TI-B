# Python Oprator
'''Operator digunakan untuk melakukan operasi pada variabel dan nilai.

Pada contoh di bawah ini, kita menggunakan operator + untuk menjumlahkan dua nilai:'''
print(5+5)

a = 2 + 2
b = a + 2
c = a + b

#arithmetic oprator
# Operator aritmatika digunakan dengan nilai numerik untuk melakukan operasi matematika umum:
a = 10
b = 3

#oprasi tambah
hasil = a + b
print(a,'+',b,'=',hasil,type(hasil))

#oprasi pengurangan
hasil = a - b
print(a,'-',b,'=',hasil,type(hasil))

#oprasi perkalian
hasil = a * b
print(a,'*',b,'=',hasil,type(hasil))

#oprasi pembagian
hasil = a / b
print(a,'/',b,'=',hasil,type(hasil))

#oprasi eksponen (pangkat)
hasil = a ** b
print(a,'**',b,'=',hasil,type(hasil))

#oprasi moduls (sisa bagi)
hasil = a % b
print(a,'%',b,'=',hasil,type(hasil))

#oprasi floar division (pembagian bulat ke bawah)
hasil = a // b
print(a,'//',b,'=',hasil,type(hasil))

#prioritas oprasi, operational precedence
'''
1. ()
2. eksponen **
3. perkalian dll * / ** & //
4. pertambahan dan pengurangan + -
'''
x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print(x, '**', y, '*', z, '+', x, '/', y, '-', y, '%', z, '//', x, '=', hasil,type(hasil))

hasil = x + y * z
print(x,'+',y,'*',z, '=',hasil,type(hasil))

#oprator komperasi
x = 5
y = 6

a = 10
b = 20

bigger = a if a > b else b
print('bigger is',bigger)

# Assignment Oprator
# Operator penugasan digunakan untuk menetapkan nilai ke variabel:
'''
=  (sama dengan)	             x = 5	       >>        x = 5	
+= (ditambah)	                 x += 3	       >>        x = x + 3	
-= (dikurang)	                 x -= 3	       >>        x = x - 3	
*=	(dikali)                     x *= 3	       >>        x = x * 3	
/=	(dibagi)                     x /= 3	       >>        x = x / 3	
%=	(sisa bagi)                  x %= 3	       >>        x = x % 3	
//=	(pembagian bulat kebawah)    x //= 3       >>	     x = x // 3	
**=	(pangkat)                    x **= 3       >>	     x = x ** 3	
&=	(AND)                        x &= 3	       >>        x = x & 3	
|=	(Or)                         x |= 3	       >>        x = x | 3	
^=	(XOR)                        x ^= 3	       >>        x = x ^ 3	
>>=	(shif kanan)                 x >>= 3       >>	     x = x >> 3	
<<=	(shif kiri)                  x <<= 3       >>	     x = x << 3	
:=	                             print(x := 3) >>	     x = 3 
                                                         print(x)
'''
# The walrus oprator
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

# Comparison Oprator
 # Operator perbandingan digunakan untuk membandingkan dua nilai:
'''
==	Equal	x == y	
!=	Not equal	x != y	
>	Greater than	x > y	
<	Less than	x < y	
>=	Greater than or equal to	x >= y	
<=	Less than or equal to	x <= y
'''

x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

# Chaining Comparison Operators
print(1 < x < 10)

print(1 < x and x < 10)

# Logical Oprator
# Operator logika digunakan untuk menggabungkan pernyataan bersyarat:
'''
'and' 	    Mengembalikan nilai True jika kedua pernyataan tersebut benar.	x < 5 and  x < 10	
'or'	    Mengembalikan nilai True jika salah satu pernyataan benar.	    x < 5 or x < 4	
'not'	    Balikkan hasilnya, mengembalikan False jika hasilnya benar.	    not(x < 5 and x < 10)
'''

# Uji apakah suatu angka lebih besar dari 0 dan kurang dari 10:
# and
x = 5

print(x > 0 and x < 10)

# or
x = 5

print(x < 5 or x > 10)

# not
x = 5

print(not(x > 3 and x < 10))

# identity Oprator
# Operator identitas digunakan untuk membandingkan objek, bukan apakah objek tersebut sama, tetapi apakah objek tersebut benar-benar objek yang sama, dengan lokasi memori yang sama:
'''
'is' 	    Mengembalikan nilai True jika kedua variabel adalah objek yang sama.	x is y	
'is not'	Mengembalikan True jika kedua variabel bukan objek yang sama.	        x is not y
'''
# is
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

# is not
x = ["apple", "banana"]
y = ["apple", "banana"]

print(x is not y)

# Difference Between is and ==
'''
is - Memeriksa apakah kedua variabel menunjuk ke objek yang sama di memori.
== - Memeriksa apakah nilai kedua variabel sama.
'''
x = [1, 2, 3]
y = [1, 2, 3]

print(x == y)
print(x is y)

# Python Membership Operators
# Operator keanggotaan digunakan untuk menguji apakah suatu urutan terdapat dalam suatu objek:
'''
'in' 	    Mengembalikan nilai True jika urutan dengan nilai yang ditentukan ada dalam objek.	x in y	
'not in'	Mengembalikan True jika urutan dengan nilai yang ditentukan tidak ada dalam objek.	x not in y
'''
# Periksa apakah "pisang" ada dalam daftar:
fruits = ["apple", "banana", "cherry"]

print("banana" in fruits)

# Check if "pineapple" is NOT present in a list:
fruits = ["apple", "banana", "cherry"]

print("pineapple" not in fruits)

# Membership in Strings
'''Operator Membership juga bekerja dengan string:'''
text = "Hello World"

print("H" in text)
print("hello" in text)
print("z" not in text)

# Bitwise Operators
# Operator bitwise digunakan untuk membandingkan angka (biner):
'''
& 	AND	                    Mengatur setiap bit menjadi 1 jika kedua bit tersebut bernilai 1.	             x & y	
|	OR	                    Mengatur setiap bit menjadi 1 jika salah satu dari dua bit bernilai 1.	         x | y	
^	XOR	                    Mengatur setiap bit menjadi 1 jika hanya satu dari dua bit yang bernilai 1.	     x ^ y	
~	NOT	                    Membalikkan semua bit	~x	
<<	Zero fill left shift	Geser ke kiri dengan memasukkan angka nol dari kanan dan biarkan bit paling kiri hilang.	                x << 2	
>>	Signed right shift	    Geser ke kanan dengan mendorong salinan bit paling kiri dari kiri, dan biarkan bit paling kanan hilang.	    x >> 2
'''
# Operator & membandingkan setiap bit dan menetapkannya menjadi 1 jika keduanya bernilai 1, jika tidak, nilainya ditetapkan menjadi 0:
# AND
print(6 & 3)
'''
Representasi biner dari 6 adalah 0110
Representasi biner dari 3 adalah 0011
Kemudian operator & membandingkan bit dan mengembalikan 0010, yang setara dengan 2 dalam desimal.
'''

# OR
# Operator | membandingkan setiap bit dan menetapkannya menjadi 1 jika salah satu atau kedua bit bernilai 1, jika tidak, nilainya ditetapkan menjadi 0:
print(6 | 3)
'''
Representasi biner dari 6 adalah 0110
Representasi biner dari 3 adalah 0011
Kemudian operator | membandingkan bit dan mengembalikan 0111, yang merupakan 7 dalam desimal.
'''

# XOR
# Operator ^ membandingkan setiap bit dan menetapkannya menjadi 1 jika hanya satu yang bernilai 1, jika tidak (jika keduanya bernilai 1 atau keduanya bernilai 0) maka nilainya ditetapkan menjadi 0:
print(6 ^ 3)
'''
Representasi biner dari 6 adalah 0110
Representasi biner dari 3 adalah 0011
Kemudian operator ^ membandingkan bit dan mengembalikan 0101, yang merupakan 5 dalam desimal.
'''

# Operator Precedence
# Prioritas operator menjelaskan urutan pelaksanaan operasi.
# Tanda kurung memiliki prioritas tertinggi, artinya ekspresi di dalam tanda kurung harus dievaluasi terlebih dahulu:
print((6 + 3) - (6 + 3))

# Operator perkalian * memiliki prioritas lebih tinggi daripada operator penjumlahan +, oleh karena itu perkalian dievaluasi sebelum penjumlahan:
print(100 + 5 * 3)

# Precedence Order
# Urutan prioritas dijelaskan dalam tabel di bawah ini, dimulai dengan prioritas tertinggi di bagian atas:
'''
()	        Tanda kurung	
**	        Eksponensial	
+x  -x  ~x	Plus unary, minus unary, dan NOT bitwise	
*  /  //  %	Perkalian, pembagian, pembagian lantai, dan modulus	
+  -	    Penjumlahan dan pengurangan	
<<  >>	    Pergeseran bitwise ke kiri dan ke kanan	
&	        Bitwise AND	
^	        Bitwise XOR	
|	        Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Operator perbandingan, identitas, dan keanggotaan
not	        Logical NOT	
and	        AND	
or	        OR
'''

# Left-to-Right Evaluation
# Jika dua operator memiliki prioritas yang sama, ekspresi dievaluasi dari kiri ke kanan.
'''Penambahan (+) dan pengurangan (-) memiliki prioritas yang sama, oleh karena itu kita mengevaluasi ekspresi dari kiri ke kanan:'''
print(5 + 4 - 7 + 3)
