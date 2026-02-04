#python strings#
print("hello WOrld!")
print('world hello')
print()
print("devil in 'me'")
print()
a = 'devil'
print(a)
print()
a = """uivbdhaSVJEHBEDJVSUA
VCBEDSNJHCVGZBCAGBYU
"""
print(a)
print()

#slicingg strings#
x = "woi jokowi!"
print(x[4:11])  #slicing
print(x[:4])    #Slice from start 
print(x[4:]) #slice to the end

x = "woi prabowo"
print(x[-5:-2])     #negative indexing

#modify strings#
a = " Hello world"
print(a.upper())
print(a.lower())
print(a.strip())
print(a.replace("e", "a"))
print(a.split(","))

print()
a = "woi"
b = "jokowi"
c = a + b
print(c)
c = a + " " + b
print(c)
print()

#format strings#
price = 10000
txt = f"the price is {price}"
print(txt)

#escape character#

txt = "my name is \"anthon\" every morning i brush my tits" 
print(txt)

