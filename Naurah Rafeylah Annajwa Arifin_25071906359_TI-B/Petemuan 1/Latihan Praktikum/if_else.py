# if statement

a = 336
b = 55
if a > b:
    print("a lebih besar dari b")

#untuk menampilkan beberapa pernyataan dalam satu if
nilai = 90
if nilai >= 90:
    print("kamu lulus") 
    print("kamu berhasil menyelesaikan ujian")
    print("selamat!")

# elif statement

nilai = 90
if nilai >= 90:
    print("nilai A")
elif nilai >= 75:
    print("nilai B")
elif nilai >= 60:
    print("nilai C")
elif nilai >= 50:
    print("nilai D")
elif nilai < 50:
    print("nilai E")

# else statement

suhu = 27
if suhu < 10:
    print("suhu sangat dingin")
elif suhu <= 30:
    print("suhu normal")
else :
    print("suhu sangat panas")

# short hand if
y = 33
z = 550
if y < z : print("33 tidak lebih besar dari 550")

#if else dalam satu baris
a = 77
b = 90
print("b") if a > b else print(a)

#if else dengan assigment value
x = 335
y = 60
besaran = x if x > y else y
print("lebih besar", besaran)

# logical operators
usia = 43
if usia >= 17 and usia < 25:
    print("remaja akhir")
if usia < 12 or usia > 60:
    print("anak-anak atau lansia")
if not usia < 18:
    print("dewasa")

# nested if
username = "Navendra"
password = "Dannie's gf"

if username == "Navendra":
    if password == "Dannie's gf": #if yang memiliki percabangan
        print("login successful!")
    else:
        print("wrong password!")
else:
    print("username not found")

# pass statement
a = 7
b = 10
if a > b:
    pass