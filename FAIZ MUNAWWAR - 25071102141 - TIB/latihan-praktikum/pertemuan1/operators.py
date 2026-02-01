a = 999
b = 2

# Operator Aritmatika
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b)
print(a//b)

x = 5

# Logical
print(x > 0 and x < 10)

print(x < 5 or x > 10)

print(not(x > 3 and x < 10))

# True Or False?
x = True
if x:
  print("Welcome back!")

# Perbandingan
a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

  score = 75
 
if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

a = 5
b = 2
if a > b: print("a is greater than b")

a = 2
b = 330
print("A") if a > b else print("B")

a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")