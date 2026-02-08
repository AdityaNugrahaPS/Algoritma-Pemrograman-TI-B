#calling a function
def my_function(): #my_function aadalah nama sebuah fungsi
    print("Goodbye Amphoreus") #output akan kosong jika kode hanya berhenti sampai disini

my_function() #output baru akan muncul ketika fungsi dipanggil
my_function()
my_function()

#contoh lain menggunakan return
def fahrenheit_to_celsius(fahrenheit):
  return (fahrenheit - 32) * 5 / 9

print(fahrenheit_to_celsius(33))
print(fahrenheit_to_celsius(77))
print(fahrenheit_to_celsius(55))

#return values
def sapa():
   return "Hello, hi"

print(sapa())

#pass statement
def sapaan():
   pass

#argument
def my_function(fname): #fungsi dengan satu argument
  print(fname + " Landau") #Landau adalah argument

my_function("Sevral")
my_function("Gepard")
my_function("Lynx")

#parameter vs argument
def my_function(name): #'name' adalah parameter
   print("Hello", name)

my_function("Geppy") #'Geppy' adalah argument

#number of arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Lynx", "Landau")

#default parameters values
def heroes(name = "partner"): #default dari parameter name adalah 'partner'
   print("Hello,", name)

heroes("Navendra")
heroes("Dan Heng")
heroes() #jika tidak ada argument, maka akan otomatis memanggil default parameter
heroes("Marchie")

#keywors argument
def pet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

pet(animal = "cat", name = "Kitty")

#positional argument
def pet(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)
#pemanggilan argument tanpa kata kunci
pet("cat", "Kitty") #positional argument harus memiliki urutan yang tepat

#mixing positional and keyword arguments
def pet(animal, name, age):
  print("I have a", age, "year old", animal, "named", name) #menggabungkan positional dan keyword argument
#argument positional harus berada sebelum keyword argument
pet("cat", name = "Kitty", age = 3)

#passing different data types
def my_function(name):
  for fruit in name:
    print(fruit)

my_fruits = ["stawberry", "anggur", "semangka"]
my_function(my_fruits)

def AE_members(person):
  print("Nama:", person["nama"])
  print("Usia:", person["usia"])

memberAE = {"nama": "Himeko", "usia": 29}
AE_members(memberAE)

#return values
def hitung(x, y):
  return x + y

hasil = hitung(9, 3)
print(hasil)

#returning different data types
def chreisos_heirs():
  return ["Castorice", "Tribbie", "Cerydra"] #fungsi yang mengembalikan list

name = chreisos_heirs()
print(name[0])
print(name[1])
print(name[2])