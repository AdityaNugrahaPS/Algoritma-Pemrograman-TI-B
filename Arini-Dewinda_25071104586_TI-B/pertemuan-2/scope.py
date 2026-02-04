#local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#global scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)