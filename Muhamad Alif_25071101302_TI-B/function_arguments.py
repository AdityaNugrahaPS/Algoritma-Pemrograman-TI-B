# Python Function Arguments
# Arguments
'''
Informasi dapat diteruskan ke fungsi sebagai argumen.
Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. Anda dapat menambahkan argumen sebanyak yang Anda inginkan, cukup pisahkan dengan koma.
Contoh berikut memiliki fungsi dengan satu argumen (fname). Saat fungsi dipanggil, kita meneruskan nama depan, yang digunakan di dalam fungsi untuk mencetak nama lengkap:'''

def my_function(fname):
  print(fname + " Refsnes")

my_function("Emil")
my_function("Tobias")
my_function("Linus")

# Parameters vs Arguments
def my_function(name): # name is a parameter
  print("Hello", name)

my_function("Emil") # "Emil" is an argument

# Number of Arguments
def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

'''def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil") {eror}'''

# Default Parameter Values
def my_function(name = "friend"):
  print("Hello", name)

my_function("Emil")
my_function("Tobias")
my_function()
my_function("Linus")

print('================')
def my_function(country = "Norway"):
  print("I am from", country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# Keyword Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(animal = "dog", name = "Buddy")

print('===================')
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function(name = "Buddy", animal = "dog")

# Positional Arguments
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("dog", "Buddy")

print('==================')
def my_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

my_function("Buddy", "dog")

# Mixing Positional and Keyword Arguments
def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

# Passing Different Data Types
def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

print('==================')
def my_function(person):
  print("Name:", person["name"])
  print("Age:", person["age"])

my_person = {"name": "Emil", "age": 25}
my_function(my_person)

# Return Values
def my_function(x, y):
  return x + y

result = my_function(5, 3)
print(result)

# Returning Different Data Types
def my_function():
  return ["apple", "banana", "cherry"]

fruits = my_function()
print(fruits[0])
print(fruits[1])
print(fruits[2])

print('===============')
def my_function():
  return (10, 20)

x, y = my_function()
print("x:", x)
print("y:", y)

# Positional-Only Arguments
def my_function(name, /):
  print("Hello", name)

my_function("Emil")

print('===============')
def my_function(name):
  print("Hello", name)

my_function(name = "Emil")

'''
def my_function(name, /):
  print("Hello", name)

my_function(name = "Emil")
'''

# Keyword-Only Arguments
def my_function(*, name):
  print("Hello", name)

my_function(name = "Emil")

print('=======================')
def my_function(name):
  print("Hello", name)

my_function("Emil")

'''def my_function(*, name):
  print("Hello", name)

my_function("Emil")
'''

# Combining Positional-Only and Keyword-Only
def my_function(a, b, /, *, c, d):
  return a + b + c + d

result = my_function(5, 10, c = 15, d = 20)
print(result)