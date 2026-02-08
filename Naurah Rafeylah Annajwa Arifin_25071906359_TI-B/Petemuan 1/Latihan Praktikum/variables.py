x = 3 #variabel bertipe int
y = "Evernight" #variabel bertipe str
print(x)
print(y)

#casting
x = str(7) #mengubah int menjadi str
y = int(7) #tetap menjadi int
z = float(7) #mengubah int menjadi float

#variable name
myname = "Evy"
my_name = "Evy"
_my_name = "Evy"
myName ="Evy"
MYNAME = "Evy"
myname2 = "Evy"

#mutiple variable
x, y, z = "Evernight", "Terrae", "Dhil"
print(x)
print(y)
print(z)

x = y = z = "Evernight"
print(x)
print(y)
print(z)

#unpack a collection
country = ["Xianzhou", "Penacony", "Amphoreus"]
a, b, c = country
print(a)
print(b)
print(c)

#output variable
x = "Hello, World!"
print(x)

x = "Hello"
y = "World!"
print(x, y)

x = "Hello"
y = "World!"
print(x + y)

#global variable
x = "peak!"

def myfunc():
  print("Amphoreus is " + x)

myfunc()