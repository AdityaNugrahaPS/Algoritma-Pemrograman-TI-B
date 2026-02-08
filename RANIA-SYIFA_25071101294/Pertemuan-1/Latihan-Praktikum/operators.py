#OPERATOR PADA BAHASA PEMPROGRAMAN PYTHON

a = 100
b = 30

"A. OPERASI ARITMATIKA"
'''
digunakan dengan nilai numerik untuk melakukan operasi matematika umum
'''
#1. operator pertambahan (+)
print(a + b) #melakukan tambah antara variabel a dan b

#2. operator pengurangan (-)
print(a-b) #melakukan kurang antara variabel a dan b

#3. operator perkalian (*)
print(a*b) #melakukan perkalian antara variabel a dan b

#4. operator pembagian (/)
print(a/b) #melakukan pembagian antara variabel a dan b

#5. operator modulus (%)
print (a % b) #melakukan modullus anatar variabel a dan b

#6. operator pangkat (**)
print(a**b) #melakukan perpangkatan antara variabel a dan b

#7. operator floor division / pembagian mengembakian bilangan bulat ke bawah (//)
print(a//b) #melakukan floor division antara variabel a dan b

"B. OPERASI PENUGASAN"
'''
digunakan untuk memberi atau mengubah nilai sebuah variabel
'''
#1. operator (=)
inicontoh1 = 20 #variabel inicontoh1 diisi dengan nilai 20
print(inicontoh1)

#2. operator (+=)
inicontoh1 += 30 #variabel inicontoh1 yang nilai awal nya itu 20, ditambah lagi nilainya dengan 30
print(inicontoh1)

#3. operator (-=)
inicontoh1 -= 10 #variabel inicontoh1 yang nilainya menjadi 50, di kurang 10 menjadi 40
print(inicontoh1)

#4. operator (*=)
inicontoh1 *= 2 #variabel inicontoh1 yang nilainya menjadi 40, dikali 2 menjadi 80
print(inicontoh1)

#5. operator (/=)
inicontoh1 /= 5 #variabel inicontoh1 yang nilainya 80, dibagi 5 menjadi 16
print(inicontoh1)

#6. operator (%=)
inicontoh1 %= 3 #hasil sisa bagi dari 16 % 3, sama dengan 1
print(inicontoh1)

#7. operator (//=)
inicontoh2 = 80
inicontoh2 //= 3 #variabel inicontoh2 dibulatkan ke bawah, hasilnya 26
print(inicontoh2)

#8. operator (**=)
inicontoh2 **= 3 #variabel inicontoh2 dipangkatkan 3, menjadi 17576
print(inicontoh2)

#9. operator bitewise 
"""&=, |=, ^=, >>=, <<="""

#10. operator walrus 
'''
menetapkan nilai ke variabel sebagai bagian dari ekspresi yang lebih besar
'''
nama = ['fildza', 'najwa', 'syifa', 'salwa', 'naurah', 'farah']

if (teman := len(nama)) > 3:
    print(f"ada {teman} temanku")


"C. OPERATOR PERBANDINGAN"
'operasi untuk membandingkan dua buah nilai, menghasilkan nilai True atau False'
nilai1 = 20
nilai2 = 20
nilai3 = 10

#1. operator (==)
'untuk memandingkan apakah dua buah variabel memiliki dua nilai yang sama'
'Hasil akan True jika variabel memiliki nilai yang sama'
'hasil akan False jika variabel memiliki nilai tidak sama'
print(nilai1 == nilai2) #hasilnya True
print(nilai1 == nilai3) #hasilnya False

#2. operator(!=)
'untuk memandingkan apakah dua buah variabel memiliki dua nilai yang tidak sama'
'Hasil akan True jika variabel memiliki nilai tidak sama'
'hasil akan False jika variabel memiliki nilai sama'
print(nilai1 != nilai2) #hasilnya False
print(nilai1 != nilai3) #hasilnya True

#3. operator (>)
'untuk memandingkan apakah dua buah variabel, apakah variabel pertama lebih besar dari pada variabel kedua'
'nilai yang ada dakam variabel tidak termasuk dalam rentang pembandingan'
'Hasil akan True jika variabel pertama lebih besar daripada variabel kedua'
'hasil akan False jika variabel Pertama lebih kecil daripada variabel kedua'
print(nilai1 > nilai3) #hasilnya True
print(nilai3 > nilai2) #hasilnya False

#4. operator (<)
'untuk memandingkan apakah dua buah variabel, apakah variabel pertama lebih kecil dari pada variabel kedua'
'nilai yang ada didalam variabel tidak termasuk dalam rentang pembandingan'
'Hasil akan True jika variabel pertama lebih kecil daripada variabel kedua'
'hasil akan False jika variabel Pertama lebih besar daripada variabel kedua'
print(nilai1 < nilai3) #hasilnya False
print(nilai3 < nilai2) #hasilnya True

#5. operator (>=)
'untuk memandingkan apakah dua buah variabel, apakah variabel pertama lebih besar dari pada variabel kedua'
'nilai yang ada didalam variabel termasuk dalam rentang pembandingan'
'Hasil akan True jika variabel pertama lebih besar daripada variabel kedua'
'hasil akan False jika variabel Pertama lebih kecil daripada variabel kedua'
print(nilai1 >= nilai3) #hasilnya True
print(nilai3 >= nilai2) #hasilnya False

#6. operator (<=)
'untuk memandingkan apakah dua buah variabel, apakah variabel pertama lebih kecil dari pada variabel kedua'
'nilai yang ada didalam variabel termasuk dalam rentang pembandingan'
'Hasil akan True jika variabel pertama lebih kecil daripada variabel kedua'
'hasil akan False jika variabel Pertama lebih besar daripada variabel kedua'
print(nilai1 <= nilai3) #hasilnya False
print(nilai3 <= nilai2) #hasilnya True

#KITA JUGA BISA MENGGABUNGKAN OPERATOR PERBANDINGAN
print(1 < nilai1 < 30) #artinya, nilai yang ada di dalam variabel nilail1, itu lebih besar dari 1, tetapi lebih kecil dari 30

"D. OPERATOR LOGIKA"
'operator ini digunakan ketika membandingkna pernyataan bersyarat'

logika = 6

#1. konjungsi (and)
'''
menguji apakah suatu nilai benar pada setiap kondisi
output akan True jika dua pernyataan benar
output akan False jika ada satu pernyataan yang salah
'''

print(1 < logika and logika > 5) 
'''uji coba nilai yang ada di dalam logika lebih besar dari pada 1 
dan lebih besar dari pada 5, karena 6 lebih besar dari 1 dan 5, maka hasilnya akan True'''

print(logika == 3 and logika > 4)
'''
uji coba nilai yang ada di dalam logika sama degan 3 dan lebih besar dari 6,
karena 6 tidak sama dengan 3, tetapi lebih beaar dari 4, nilai keluarannya adalah False, karena
salah satu dari pernyataan itu salah
'''

#2. Disjungsi (or)
'''
menguji apakah setidaknya ada suatu nilai benar pada setiap kondisi
output akan True jika ada salah satu pernyataan benar
output akan False jika ada tidak ada pernyataan yang benar
'''
print(1 < logika or logika > 5) 
'''uji coba nilai yang ada di dalam logika lebih besar dari pada 1 
ATAU lebih besar dari pada 5, karena 6 lebih besar dari 1 dan 5, maka hasilnya akan True'''

print(logika == 3 or logika > 4)
'''
uji coba nilai yang ada di dalam logika sama degan 3 ATAU lebih besar dari 6,
karena 6 tidak sama dengan 3, tetapi lebih beaar dari 4, nilai keluarannya adalah True, karena
salah satu dari pernyataan itu Benar
'''
print(logika == 2 or logika < -3)
'''
uji coba nilai yang ada di dalam logika sama degan 2 ATAU lebih kecil dari -3,
karena 6 tidak sama dengan 2, dan lebih kecil dari -3, nilai keluarannya adalah False,
karena tidak ada pernyataan yang benar
'''

#3. Negasi (Not)
'''
mengubah nilai dari yang awalnya
TRUE menjadi FALSE, dan sebaliknya
'''
x = 90

print(not(x > 3 and x < 100)) #harusnya kan hasil dari konjungsi True, tapi karena ada not
#maka nilai kebenarannya menjadi False

"E. OPERATOR IDENTITAS"
'membandingkan dua variabel, apakah keduannya benar - benar sama, dengan lokasi yang sama'
#1. is

X = ["ini nilai 1", "ini nilai 2"]
y = ["ini nilai 1", "ini nilai 2"]
z = X

print(X is z) #menjadi True karena z == X
print(X is y) #menjadi False karena X bukan y


print(X == y) #menjadi True karena nilai X sama dengan y


#2. is not
X = ["ini nilai 1", "ini nilai 2"]
y = ["ini nilai 1", "ini nilai 2"]
z = X



print(X is not z) #menjadi False karena z == X
print(X is not y) #menjadi True karena X bukan y

"F. OPERATOR KEANGGOTAAN"
'menguji apakah suatu urutan terdapat dalam suatu objek'
#1. in
X = ["ini nilai 1", "ini nilai 2", "ini nilai 3"]

print("ini nilai 1" in X) #menjadi True karena "ini nilai 1" ada dalam X
print("ini nilai 5" in X) #menjadi False karena "ini nilai 1" tidak ada dalam Xs

#2. not in
X = ["ini nilai 1", "ini nilai 2", "ini nilai 3"]

print("ini nilai 1" not in X) #menjadi False karena "ini nilai 1" ada dalam X
print("ini nilai 5" not in X) #menjadi True karena "ini nilai 1" tidak ada dalam X

"G. OPERATOR BITWISE"
'untuk membandingkan angka (biner)'

#1. operator &
"""
Operator & membandingkan setiap bit dan menetapkannya menjadi 1 jika keduanya bernilai 1,
jika tidak, nilainya ditetapkan menjadi 0
"""
# The & operator compares each bit and set it to 1 if both are 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 2 = 0010

print(6 & 3)

#2. operator |
'''
Operator | membandingkan setiap bit dan menetapkannya menjadi 1 
jika salah satu atau kedua bit bernilai 1,
 jika tidak, nilainya ditetapkan menjadi 0:
'''

# The | operator compares each bit and set it to 1 if one or both is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 7 = 0111

print(6 | 3)

#3. operator ^
'''
Operator ^ membandingkan setiap bit dan menetapkannya menjadi 1 jika hanya satu yang bernilai 1,
 jika tidak (jika keduanya bernilai 1 atau keduanya bernilai 0) maka nilainya ditetapkan menjadi 0:
'''
# The ^ operator compares each bit and set it to 1 if only one is 1, otherwise it is set to 0
# 6 = 0110
# 3 = 0011
# --------
# 5 = 0101

print(6 ^ 3)


"URUTAN PRIORITAS OPERATOR"
#--- INI MATERI DARI W3SCHOOL ---
'''
()	Parentheses	
**	Exponentiation	
+x  -x  ~x	Unary plus, unary minus, and bitwise NOT	
*  /  //  %	Multiplication, division, floor division, and modulus	
+  -	Addition and subtraction	
<<  >>	Bitwise left and right shifts	
&	Bitwise AND	
^	Bitwise XOR	
|	Bitwise OR	
==  !=  >  >=  <  <=  is  is not  in  not in 	Comparisons, identity, and membership operators	
not	Logical NOT	
and	AND	
or	OR
'''

#OPERATORS DONE