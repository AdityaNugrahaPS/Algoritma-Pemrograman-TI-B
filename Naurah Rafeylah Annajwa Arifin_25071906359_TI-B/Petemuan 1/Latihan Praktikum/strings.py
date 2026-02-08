#string bisa ditulis dengan tanda petik dua maupun tunggal
print("Amphoreus")
print('Amphoreus')

#quotes inside quotes
#bisa menambahkan tanda kutip lagi didalam string asalkan tidak sama dengan tanda kutip yang mengelilingi string tersebut
print("It's me, Khaslana")
print("yes, 'Khaslana'")
print('yes, "Khaslana"')

#assign string to variable
a = "Cyrene"
print(a)

#multiline strings
#menambahkan string ke variable menggunakan tiga tanda petik dua
a = """ A hero is in everyone's heart.
Embrace it and chase after the sun.
See you at the next pale dawn,
partner. """
print(a)

#menambahkan string ke variable menggunakan tiga tanda petik tunggal
a = ''' A hero is in everyone's heart.
Embrace it and chase after the sun.
See you at the next pale dawn,
partner. '''
print(a)

#strings are array
a = "Phainon"
print(a[3]) #menampilkan array string indeks ke 3

#looping through a string
for x in "flame": #pengulangan dalam kata 'flame'
    print(x) #menampilkan pengulangan x

#string lenght
#mendapatkan panjang sebuah string
a = "Phainon Khaslana"
print(len(a)) #menampilkan panjang string a

#check string
#cara  mengecek apakah sebuah kata terdapat dalam string
txt = "Don't be afraid to fall, just run!"
print("fall" in txt) #menampilkan hasil pengecekan kata pada string

#cara lain dengan menggunakan keyword if
txt = "Don't be afraid to fall, just run!"
if "fall" in txt:
    print("ya, kata 'fall' ada didalam teks")

#check if not
#jika kosa kata tidak terdapat dalam string
txt = "Don't be afraid to fall, just run!"
print("go" not in txt)

#menggunakan keyword if
txt = "Don't be afraid to fall, just run!"
if "go" not in txt:
    print("tidak ada kata 'go' didalam teks")


