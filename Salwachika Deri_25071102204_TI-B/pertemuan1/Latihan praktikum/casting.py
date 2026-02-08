'''
Casting adalah proses mengubah satu tipe data ke tipe data lain.
Contohnya: dari teks ke angka, atau dari angka ke teks.
'''

#string to integer==================================================================================
string = '1'
string_to_numbers = int(string)
print(type (string))
print(type (string_to_numbers))

usia = '19'
usia_int = int(usia)
print(type(usia))
print(type(usia_int))

#integer to float==================================================================================
ukuransepatu = 38
ukuransepatu_float = float(ukuransepatu)
print(type(ukuransepatu))
print(type(ukuransepatu_float))

#number to string==================================================================================
nilai = 90
teks = str(nilai)

#string to float===================================================================================
harga = "12.5"
harga_float = float(harga)

#boolean casting====================================================================================
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False
print(bool("hi"))   #True
