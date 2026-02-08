#shorthand if
a = 5
b = 2
if a > b: print("a is greater than b")


a = 10
b = 20
bigger = a if a > b else b
print("Bigger is", bigger)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")


number = 20
if number > 0:
  print("The number is positive")

#and
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#or
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#not
a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")


age = 21
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")


username = "fufufafa"
password = "sawit123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")



score = 76

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")


x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")





#Pass Statement
a = 33
b = 200

if b > a:
  pass


