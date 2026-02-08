'''
wadah untuk menyimpan data di dalam program. di python tipe data tidak dituliskan
'''

x = 5   #menyimpan data 5
y = "John"  #menyimpan data string
print(x)
print(y)

#casting
#jika ingin men-spesifik kan tipe data
x = str(3)
y = int(3)

#variables name
myvar = "salwa"
my_var = "salwa"
_my_var = "salwa"
myVar = "salwa"
MYVAR = "salwa"
myvar2 = "salwa"

#Multiple Values
x, y, z = "exile", "bejelwed", "august"
print(x)
print(y)
print(z)

a, b, c = "taylor swift"
print(a)
print(b) 
print(c)

#Unpack a Collection
album = ['taylor swift', 'hindia', 'bernadya']
x, y, z = album
print(x)
print(y)
print(z)

#output variables
x = 'saya suka belajar bahasa inggris'
print(x)

#global variabel
x = "mudah"
def myfunc():
  print("bahasa python itu " + x)
myfunc()


