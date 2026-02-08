#1 Python variable
x = 7
y = 10
print(x)
print(y)


'''
Variabel tidak perlu dideklarasikan dengan tipe tertentu,
bahkan tipenya bisa diubah setelah ditetapkan.
'''
z = 30 # z bertipe integer
z = "Ally" # z berubah menjadi tipe string
print(z)


'''
Bila ingin menggunakan tipe data spesifik untuk suatu variabel, 
bisa dengan melakukan casting.
'''
a = int(6) #akan menghasilkan 6
b = str(6) #akan menghasilkan '6'
c = float(6) #akan menghasilkan 6.0

print("--Casting--") #Menampilkan header
print(a)
print(b)
print(c)


'''
Untuk menampilkan tipe data dari suatu variabel, bisa dengan menggunakan type().
'''
print("\n--Get The Type--") #Menampilkan header
print(type(a))
print(type(b))
print(type(c))

#2. Variable name
'''
Aturan penamaan variabel pada bahasa pemrograman Python
1. Nama variabel harus dimulai dengan huruf atau karakter garis bawah (_)
2. Nama variabel tidak boleh dimulai dengan angka
3. Nama variabel hanya boleh berisi karakter alfanumerik dan garis bawah (A-z, 0-9, dan _ )
4. Nama variabel peka terhadap huruf besar/kecil
5. Nama variabel tidak boleh berupa salah satu kata kunci Python.
'''

#Contoh penamaan variabel yang tepat
print("\n--Variable Name--") #Menampilkan header
myLove = "Nala"
my_love = "Nala"
_my_Love = "nala"
mylove = "Nala"
MyLove = "Nala"

print(myLove)
print(my_love)
print(_my_Love)
print(mylove)
print(MyLove)

#3. Assign multiple values
'''
Mengisi beberapa variabel dalam satu baris.
'''
husband, wifey, lovers = "Jaeha Kim", "Aihara Mei", "Eiser" #Memuat 3 variabel sekaligus dalam satu baris
print("\n--Many Values to Multiple Variables--") #Menampilkan header
print(husband)
print(wifey)
print(lovers)


'''
Mengisi nilai yang sama dalam beberapa variabel.
'''
buah = bulat = manis = "Jeruk" #Ketiga variabel memilki nilai yang sama (Jeruk)
print("\n--One Value to Multiple Variables")
print(buah)
print(bulat)
print(manis)


'''
Jika terdapat kumpulan nilai dalam 'List', 'Tuple', dll. 
Python memungkinkan untuk mengekstrak nilai menjadi variabel. 
Ini disebut membongkar (Unpacking)
'''
name = ["Endang", "Arum", "Desty", "Tsabita"]
d, e, f, g = name
print("\n--Unpacking--") #Menampilkan header
print(d)
print(e)
print(f)
print(g)

#4. Output Variables
'''
Fungsi print digunakan untuk menampilkan variabel.
'''
text = "Hello everyone!"
print(text)


'''
Dalam fungsi ini, bisa menampilkan beberapa variabel sekaligus 
dengan memisahkan menggunakan tanda koma (,).
'''
h = "Hello"
i = "Everyone!"
print(h, i)


'''
Bisa juga menggunakan operator untuk menghasilkan Beberapa variabel.
'''
h = "Hello"
i = "Everyone"
print(h + i)


'''
Jika nilai berupa angka, penggunaan operator tambah (+)
akan menghasilkan operasi Matematika
'''
A = 4
B = 5
print(A + B)

#5. Global Variables
'''
Variabel yang dibuat diluar sebuah fungsi disebut Variabel Global.
Variabel Global bisa digunakan di dalam maupun di luar fungsi
'''
d = "Endang"

def myfunc() :
    print("\n--Global Variables--")
    print("Her name is " + d)

myfunc()


'''
Jika membuat variabel dengan nama yang sama di dalam dan fungsi, 
variabel ini akan bersifat lokal, dan hanya dapat digunakan di dalam fungsi. 
Variabel global dengan nama yang sama akan tetap seperti semula, 
global dan dengan nilai aslinya.
'''
husband = "Jaeha Kim" #Variabel global

def myfunc() :
    husband = "Matthias" #Variabel lokal
    print("Oh, how I love " + husband)

myfunc()

print("Oh, how I love " + husband)


'''
Biasanya, ketika membuat variabel di dalam fungsi, variabel tersebut adalah variabel lokal,
dan hanya dapat digunakan di dalam fungsi tersebut. Untuk membuat variabel global di dalam fungsi, 
Anda dapat menggunakan kata kunci 'global'.
'''
def myfunc() :
    global j
    j = "love" # j adalah Variabel Global, walaupun dibuat di dalam fungsi
    
myfunc()

print("How I " + j + " her") #Variabel j bisa digunakan diluar fungsi


'''
Kata kunci 'global' juga digunakan untuk mengubah nilai variabel global di dalam fungsi.
'''
j = "lover"

def myfunc() :
    global j
    j = "hate" #Nilai j berubah

myfunc()

print("How I " + j + " him")