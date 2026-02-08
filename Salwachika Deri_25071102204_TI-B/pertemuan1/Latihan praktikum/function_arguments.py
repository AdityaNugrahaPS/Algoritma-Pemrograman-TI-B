#function argumen 
'''
Arguments adalah data/nilai yang dikirim ke dalam fungsi saat fungsi dipanggil.
Arguments ditulis di dalam tanda kurung saat memanggil fungsi dan dipisahkan dengan koma.
'''
#contoh
def my_function(fnama):         #fnama=parameter
    print(fnama + " Refsnes")
my_function("Emil")             #emil, bagas, gilang = arguments
my_function("bagas")
my_function("gilang")

#parameter vc argumen
'''
Parameter → variabel di definisi fungsi
Argument → nilai asli saat memanggil fungsi
'''
def my_function(nama):   # nama = parameter
    print("Hello", nama)
my_function("Emil")      # Emil = argumen

#number argument
#jumlah argumen harus sesuai dengan jumlah parameter
def my_function(fnama, lnama):
    print(fnama + " " + lnama)
my_function("Emil", "Refsnes")

#default parameter value
def my_function(negara="indonesia"):
    print("saya berasal dari ", negara)
my_function("indonesia")
my_function()

#keyword arguments
#Urutan tidak berpengaruh jika memakai keyword.
def my_function(peliharaan, nama):
    print("saya mempunyai peliharaan ", peliharaan)
    print("peliharaan saya", peliharaan + "'bernama'", nama)
my_function(animal="kucing", name="Buddy")

#positional arguments
#Argument dikirim tanpa menyebut nama parameter.
#urutan sangat pentig
my_function("dog", "Buddy")

#Menggabungkan Positional & Keyword Arguments
#positional harus didepan
def my_function(animal, name, age):
    print("I have a", age, "year old", animal, "named", name)
my_function("dog", name="Buddy", age=5)

#Mengirim Berbagai Tipe Data
#argumen bisaa mengirim data apa saja
    #a. List sebagai argument
def my_function(fruits):
    for fruit in fruits:
        print(fruit)
my_function(["apple", "banana", "cherry"])

    #b. Dictionary sebagai argument
def my_function(person):
    print("Name:", person["name"])
    print("Age:", person["age"])
my_function({"name": "Emil", "age": 25})

#return value
def my_function(x, y):
    return x + y
result = my_function(5, 3)
print(result)

#return banyak data
    #return list
def my_function():
    return ["apple", "banana", "cherry"]
fruits = my_function()
print(fruits[0])

    #return tuple
def my_function():
    return (10, 20)
x, y = my_function()
print(x, y)

#Positional-Only Arguments (/)
#Argument harus berdasarkan posisi, tidak boleh pakai keyword
def my_function(name, /):
    print("Hello", name)
my_function("Emil")

#Keyword-Only Arguments (*)
def my_function(*, name):
    print("Hello", name)
my_function(name="Emil")