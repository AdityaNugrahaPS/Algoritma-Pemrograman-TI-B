# Bolleans merupakan tipe data yang hanya memiliki dua nilai, yaitu True dan False
Nikah = False
Jomblo = True
print(type(Nikah))  #output: bool
print(type(Jomblo))  #output: bool

# kita bisa melakukan operasi logika pada tipe data boolean
if Jomblo and not Nikah:
    print("When yhh")  #output: When yhh


suka = True
tidakSuka = False
Aku = True
Kamu = True

if Aku == suka and Kamu == suka:
    print("will you be My mine?")  #output: will you be My mine?
elif Aku == suka and Kamu == tidakSuka:
    print("infokan Gym Terdekat bradar")  #output: infokan Gym Terdekat bradar
else:
    print("cari yang lain aja deh...") #output: cari yang lain aja deh...


# kita juga bisa mengkonversi tipe data lain ke boolean dengan fungsi bool()
print(bool(1))        #output: True   (karena 1 dianggap True)
print(bool(0))        #output: False  (karena 0 dianggap False)
print(bool(-5))       #output: True   (karena selain 0 dianggap True)
print(bool(""))       #output: False  (karena string kosong dianggap False)
print(bool("Alam"))   #output: True   (karena string tidak kosong dianggap True)

# intinya selama ada isinya berarti true, kalau kosong berati false




