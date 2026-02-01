#OPERATORS

print(12 + 13.4) #operators are used to perform operations on variables and values the plus is an example of one

op1 = 23 # you can sign a value to a variable and then use it with an operator
op2 = op1 - 15.6
op3 = op2 / op1

print(op3)

#ARITHMETIC
num1 = 12.7
num2 = 23.3

print(num1 + num2)#addition
print(num1 - num2)#subtraction
print(num1 * num2)#multiplication
print(num1 / num2)#division returns a float
print(num1 % num2)#modulus
print(num1 ** num2)#exponentiation
print(num1 // num2)#floor division returns an integer rounded down

#ASSIGNMENT
x = 15.5 #x sama dengan 15.5
y= 12
x += 12.5 # x = x + 12.5
x -= 12.5#x = x - 12.5
x *= 12.5#x = x * 12.5
x /= 12.5#x = x / 12.5
x %= 12.5#x = x % 12.5
x //= 12.5#x = x // 12.5
x **= 12.5#x = x ** 12.5
y &= 10#x = 3
y |= 7#x = x | 12.5
y ^= 5#x = x ^ 12.5
y >>=12#x = x >> 12.5
y <<=17#x = x << 12.5
print(x:=125)#x = 3 print(x)

#COMPARISON
#returns true or false
a = 128
b = 64

print(a == b)# if same = true
print(a != b)#if not same = true
print(a > b)#true if a is bigger than b
print(a < b)#true if a is smaller than b
print(a >= b)#true if a is bigger than b including the same number
print(a <= b)#true if a is smaller than b including the same number
print(8 < b < 80)#you can also chain the comparison
print(12 < a and b > 60)

#LOGICAL
#and,or,not

i = 137
print(i < 150 and i > 100) # both have to be true 
print(i < 100 or i > 100) # one hase to be true 
print(not(i < 150 and i > 100)) # just negates the answer if true becomes false vice versa 

#IDENTITY
j = ['Avatar', 'Gravity Falls', 'Pluribus']
k = ['Avatar', 'Gravity Falls', 'Pluribus']
l = j

print(j is l) # true if object/variable is the same
print(j is k) #this is not true because j is not the same as k as in the variables
print(j == k) # true if the memory inside the object is the same
print(j is not k) #true if object/variable is not the same

#MEMBERSHIP
string1 = "Never thought i'd have it this good"
print("Never" in string1) # checks if "Never" is contained inside of the string if yes = true
print("Dream" in string1) #this is false because "Dream" is not contained inside of the string
print("Good" not in string1) # this is true because even though "good"is inside the string "Good" is different from "good"

#BITWISE
#this one is based on the binary of the values
print(7 & 5) # with & it compares the bits and if both are 1 it sets it to one but if one has 0 it turns to 07 in binary is 0111 and 5 in binary is 0101 that means with & it becomes 0101 which is 5
print(10 | 7) # with |(or) if atleast one bit has one it sets it to 1 so 10 in binary 1010 and 7 is 0111 that means it becomes 1111 which is 15 in binary
print(7 ^ 5) # ^ (XOR) sets it to 1 if only is 1 else it becomes 0 7 is 0111 and 5 is 0101 so it becomes 0010 which is 2
print(~7) #in bit 7 is 0111 so if you use negation it becomes -(1000) which is -(8)