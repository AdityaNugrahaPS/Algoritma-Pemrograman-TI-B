# # tandanya pecahan dari materinya
#create variable

x = 6
y  = 'tujuah'
z = 7
print(x)
print(y)

print()

#casting#
x = str(7) #harusnya aoutputnya bgini '7'
y = int(7)
z = float (7)

print(x)
print(y)
print(z)
print()

#get the type shii,wkwkw jk broo

x = 5
y = 'faris ganteng'
print(type(y))
print(type(x))
print()


#variable name
var = 'faris'

#camel case  
'''
Each word, except the first, starts with a capital letter:
'''
myVariableName = "Faris"

#pascal case
'''
Each word starts with a capital letter:
'''
MyVariableName = "Faris"

#snake case
'''
Each word is separated by an underscore character
'''
my_variable_name = "Faris"

print()

#ASSIGN MULTIPLE VALUES#
'''
If you have a collection of values in a list, tuple etc.
Python allows you to extract the values into variables. This is #called unpacking.
'''
fruits = ["apple", "mango", "pineaple"]

x, y, z = fruits
print(x)
print(z)
print(y)
print()

#Output VAriables#
x = "anaconda"
y = "python"
z = "Tardigarde"

print(x, y ,z)
print()

x = "anaconda "
y = "python " #give the blank to get some space in the output
z = "Tardigarde"
print(x + y + z)
print()

#GLOBAL VARIABLE#
x = "awful"

def myfunc():
    x = "cool"
    print("Fortran is " + x)

myfunc()
print("Fortran is " + x)
print()