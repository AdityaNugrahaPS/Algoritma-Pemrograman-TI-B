#Iterasi menggunakan tuple
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit)) #Memanggil apple
print(next(myit)) #Memanggil banana
print(next(myit)) #Memanggil cherry


#Iterasi menggunakan string
mystr = "banana"
myit = iter(mystr)

print(next(myit)) #Memanggil b
print(next(myit)) #Memanggil a
print(next(myit)) #Memanggil n
print(next(myit)) #Memanggil a
print(next(myit)) #Memanggil n
print(next(myit)) #Memanggil a