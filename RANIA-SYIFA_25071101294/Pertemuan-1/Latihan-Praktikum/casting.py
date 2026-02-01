


'''tugas, buatkan semua tipe data lalu dikonver, 
nth itu float ke string, int ke float, dll'''

#MARI KITA MENGKONVERSI TIAP TIPE DATA KE TIPE DATA LAINNYA
a = 40 #variabel a bertipe data integer
print(a)
print(type(a))
b = 5.7 #variabel b bertipe data float
print(b)
print(type(b))
c = '1211' #variabel c bertipe data string
print(c)
print(type(c))

'KITA KONVERSI KAN YAA'
#1 integer -> float
contohkonver1 = float(a) #tipe data awal int , lalu diubah menjadi tipe data float
print(contohkonver1)
print(type(contohkonver1))

#2 float -> integer
contohkonver2 = int(b) #tipe data awal float, lalu diubah menjadi tipe data int
print(contohkonver2)
print(type(contohkonver2))

#3 integer -> string
contohkonver3 = str(a)  #tipe data awal int, lalu diubah menjadi tipe data string
print(contohkonver3)
print(type(contohkonver3))

#4 float -> string
contohkonver4 = str(b) #tipe data awal float, alu diubah menjadi tipe data string
print(contohkonver4)
print(type(contohkonver4))

#5 string -> int
contohkonver5 = int(c) #tipe data awal string, lalu diubah menjadi tipe data int
print((contohkonver5))
print(type(contohkonver5))

#6 string -> float
contohkonver6 = float(c) #tipe data awal string, lalu diubah menjadi tipe data float
print(contohkonver6)
print(type(contohkonver6))

d = [1,2,3,4] #list
print(d)
print(type(d))

e = {11,12,13,14} #set
print(e)
print(type(e))

f = (21,22,23,24) #tuple
print(f)
print(type(f))

g = {"x": "Rania", "y":3} #dict
print(g)
print(type(g))

#7 string -> list
contohkonver7 = list(c) #tipe data awal string, lalu diubah menjadi tipe data list
print(contohkonver7)
print(type(contohkonver7))

#8 string -> tuple #tipe data awal string, lalu diubah menjadi tipe data tuple
contohkonver8 = tuple(c)
print(contohkonver8)
print(type(contohkonver8))

#9 string -> set #tipe data awal string, lalu diubah menjadi tipe data set
contohkonver9 = set(c)
print(contohkonver9)
print(type(contohkonver9))

#10 list -> tuple #tipe data awal list, lalu diubah menjadi tipe data tuple
contohkonver10 = tuple(d)
print(contohkonver10)
print(type(contohkonver10))

#11 list -> set #tipe data awal list, lalu diubah menjadi tipe data set
contohkonver11 = set(d)
print(contohkonver11)
print(type(contohkonver11))

#12 tuple -> list #tipe data awal tuple, lalu diubah menjadi tipe data list
contohkonver12 = list(f)
print(contohkonver12)
print(type(contohkonver12))

#13 dict -> list #tipe data awal dict, lalu diubah menjadi tipe data list
contohkonver13 = list(g)
print(contohkonver13)
print(type(contohkonver13))

#14 dict -> tuple #tipe data awal dict, lalu diubah menjadi tipe data tuple
contohkonver14 = tuple(g)
print(contohkonver14)
print(type(contohkonver14))

#CASTING DONE