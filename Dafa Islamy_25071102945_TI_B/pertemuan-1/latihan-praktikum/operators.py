#sub-bab 'python operator'

print(16 + 6) #output akan menghasilkan penjumlahan 16 + 6 yaitu 22

#operator dapat digunakan untuk melakukan operasi antara varibel dengan nilai
sum1 = 16 + 6
sum2 = sum1 + 20
sum3 = sum2 + sum1
print(sum3)


#sub-bab 'arithmetic operators'

'''
+ : addition
- : substraction
* : multiplication
/ : division
% : modulus
** : exponentiation
// : floor division
'''

x = 16
y = 6
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

a = 25
b = 4
print(a / b) #division selalu menghasilkan float
print(a // b) #floor division selalu menghasilkan int dan pembulatan selalu kebawah


#sub-bab 'assignment operators'

'''
=
+=
-=
*=
/=
%=
//==
**==
&=
|=
^=
>>=
<<=
:=
'''

x += 4
print(x)

x = 100
print(not(x > 55 or x > 101))

#walrus operator (:=) berguna untuk memasukkan nilai ke variabel sekaligus digunakan dalam sebuah ekspresi
numbers = [1, 2, 3, 4, 5]
if (count := len(numbers)) > 3: #count berisi 5 dan 5 > 3
    print(f"List has {count} elements") #maka output akan menampilkan 'List has 5 elements'


#sub-bab 'comparison operators'

'''
== (equal)
!= (not equal)
> (greater than)
>= (greater than or equal to)
< (less than)
<= (less than or equal to)
'''

#output berupa nilai boolean
x = 6
y = 3
print(x == y)
print(x != y)
print(x > y)
print(x >= y)
print(x < y)
print(x <= y)

#opeator perbandingan dapat digabungkan
x = 6
print(1 < x < 7)
print(1 < x and x < 7)


#sub-bab 'logical operators'

'''
and : output True jika kedua pernyatan bernilai true
or : output True jika setidaknya salah satu pernyataan bernilai true
not : kebalikan dari hasil, jika pernyataan bernilai True maka hasil bernilai False serta sebaliknya
'''

x = 6
print(1 < x and x < 10) #output akan bernilai True karena kedua pernyataan bernilai true

x = 6
print(1 < x or x < 10) #output akan bernilai True karena setidaknya satu pernyataan bernilai true

x = 6
print(not(1 < x and x < 10)) #output akan bernilai False karena pernyataan bernilai true


#sub-bab 'identity operators'

'''
is : output bernilai True jika kedua variabel memiliki objek yang sama
is not : output bernilai True jika kedua variabel memiliki objek yang tidak sama
'''

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z) #output akan bernilai True karena x dan z memiliki objek yang sama
print(x is y) #output akan bernilai False karena lokasi memori x dan y berbeda walaupun memiliki isi yang sama
print(x == y) #output akan bernilai True karena x dan y memiliki nilai yang sama


#sub-bab 'membership operators'

'''
in : output bernilai True jika nilai yang dicari ditemukan dalam urutan
not in : output bernilai True jika nilai yang dicari tidak ditemukan dalam urutan
'''

kendaraan = ['Motor', 'Mobil', 'Sepeda']
print('Sepeda' in kendaraan) #output akan bernilai True karena benar 'Sepeda' berada didalam list
kendaraan = ['Motor', 'Mobil', 'Sepeda']
print('Truk' in kendaraan) #output akan bernilai False karena 'Truk' tidak berada didalam list

kendaraan = ['Motor', 'Mobil', 'Sepeda']
print('Truk' not in kendaraan) #output akan bernilai True karena benar 'Truk' tidak berada didalam list
kendaraan = ['Motor', 'Mobil', 'Sepeda']
print('Sepeda' not in kendaraan) #output akan bernilai False karena 'Sepeda' berada didalam list


#sub-bab 'bitwise operators'

'''
& (AND) : mengubah setiap bit menjadi 1 jika kedua bit adalah 1
| (OR) : mengubah setiap bit menjadi 1 jika setidaknya salah satu bit adalah 1
^ (XOR) : mengubah setiap bit menjadi 1 jika hanya satu bit bernilai 1
~ (NOT) : membalikkan semua bit
<< (Zero fill left shift) : geser ke kiri dengan memasukkan angka nol dari kanan dan biarkan bit paling kiri hilang
>> (Signed right shift) : geser ke kanan dengan mendorong salinan bit paling kiri dari kiri, dan biarkan bit paling kanan hilang
'''

print(6 & 3) #bit 6 adalah 110 dan bit 3 adalah 011, opeartor & akan membandingkan dan mendapat hasil 010 yaitu 2
print(6 | 3) #bit 6 adalah 110 dan bit 3 adalah 011, opeartor | akan membandingkan dan mendapat hasil 111 yaitu 7
print(6 ^ 3) #bit 6 adalah 110 dan bit 3 adalah 011, opeartor ^ akan membandingkan dan mendapat hasil 101 yaitu 5
print(~(6 & 3)) #hasil ~(6 & 3) adalah ~2, rumus ~x = -(x+1), sehingga didapat ~2 adalah -3


#sub-bab 'operator precedence'

'''
precedence order
() : parentheses
** : exponentiation
+x, -x, ~x : unary plus, unary minus, and bitwise NOT
*, /, //, % : multiplication, division, floor division, and modulus
+, - : addition and subtraction
<<, >> : bitwise left and right shifts
& : bitwise AND
^ : bitwise XOR
| : bitwise OR
==, !=, >, >=, <, <=, is, is not, in, not in  : comparisons, identity, and membership operators
not : logical NOT
and : AND
or : OR
'''