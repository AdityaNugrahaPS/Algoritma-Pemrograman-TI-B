#TIPE TIPE DATA DALAM PYTHON
'''setiap variabel pasti ada tipe data, berikut macam macam tipe data yang ada di Python'''

#1 Numbers
'''Dalam Numbers, ada tiga numerik yang tersedia dalam Python, yaitu:
1. Integer
    yaitu tipe data yang berisi bilangan bulat, mau itu positif atau negatif
2. Float
    yaitu tipe data yang berisi bilangan desimal
3. Complex
    yaitu tipe data yang berisi bilangan kompleks dengan ditulis huruf "j" sebagai bagian imajiner'''

#contoh integer
print(3)
print(-4)
print(867492)

#contoh float
print(3.2)
print(-4.5)


#contoh complex
print(6j)
print(3+9j)

'''
untuk mengetahui apa tipe data suatu variabel, berikan perintah berikut:
'''

#1. Integer
contohinteger1 = 38
contohinteger2 = -92

print(type(contohinteger1))
print(type(contohinteger2))

#2. float
contohfloat1 = 3.5
contohfloat2 = -582.7

print(type(contohfloat1))
print(type(contohfloat2))

#3. complex
contohcomplex1 = 8j
contohcomplex2 = 23 + 9j

print(type(contohcomplex1))
print(type(contohcomplex2))

#KITA BISA MENGKONVERSI TIPE DATA
#mengubah tipe data yang sekarang menjadi sebuah tipe data baru
#contoh : yang awalnya a itu int, menjadi float

contohkonversi1 = 3 #ini tipe datanya int
print(type(contohkonversi1))

contohkonversi2 = 3.5 #ini tipe datanya float
print(type(contohkonversi2))

contohkonversi3 = 35j #ini tipe datanya complex
print(type(contohkonversi3))


#SEKARANG KITA AKAN MENGKONVERSI SETIAP TIPE DATA
contoh_setelah_konversi1 = float(contohkonversi1) #yang awalnya int menjadi float
print(contoh_setelah_konversi1)

contoh_setelah_konversi2 = int(contohkonversi2) #yang awalnya float menjadi int
print(contoh_setelah_konversi2)

contoh_setelah_konversi3 = complex(contohkonversi1) #yang awalnya int menjadi complex
print(contoh_setelah_konversi3)

#NUMBER DONE

