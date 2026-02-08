#IF_ELSE

'''
Docstring for if_else
ada banyak kondisi yang berdasarkan logika matematika    
Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
'''

#ditulus menggunakan if statement
x = 25
y = 75
if x > y: # if_else menggunakan True dan False
    print("x is bigger than y") # jadi jika x > y true ini akan di print
elif x < y:
    print("x is lesser than y") # tulis elif untuk menentukan kondisi lain 
else:
    print("x and y are the same") # else untuk jika kedua kondisi diatas tidak dipenuhi
 

car_status = True
if car_status:
   print("The car is running") # bisa menulis banyak line dalam if statement
   print("You can start driving")

month = 10
if month == 1:
    print("January")
elif month == 2:
    print("February")
elif month == 3:
    print("March")
elif month == 4:
    print("April")
elif month == 5:
    print("May")
elif month == 6:
    print("June")
elif month == 7:
    print("July")
elif month == 8:
    print("August")
elif month == 9:
    print("September")
elif month == 10:
    print("October")
elif month == 11:
    print("November")
elif month == 12:
    print("December")
else:
    print("Not a valid month")

#shorthand if
phone_status = True 
print("Phone is on") if phone_status else print("Phone is off") # bisa menulis statement dalam satu line

#Assign a value dengan shorthand if
max1 = 100
max2 = 200
maximum = max1 if max1 > max2 else max2
print("The maximum capacity is", maximum)

#Logical operators and,or,not
age = 21
money = 30
sober = True
if age > 18 and money > 10 and sober: # and artinya semua kondisi harus true untuk menghasilkan true
    print("You are of age")
    print("You have the money")
    print("You can buy the apple juice")

skill = True
wealthy = False
if skill or wealthy: # kalau or hanya satu harus true
    print("You can beat the level")

a = 25
b = 100
if not a > b: # check jika a tidak besar dari b
    print("a is lesser than b")

level = 50
is_prestieged = False
hasKey = True

if (level >= 50) and is_prestieged or hasKey: #and, or dan not, bisa digabung
    print("You can open the door")

#Nested IF
Age = 18
if Age > 12:
    print("You are not a child") 
    if Age >= 18: # nested if artinya ada if statement dalam if statement
        print("You are atleast an adult")
        if Age >= 65:
            print("You are an elder")
        else:
            print("You are not alive")

beat_hades = 10
reunited_orpheus = True
avg_affection_over_5 = True
if beat_hades >= 10:
    print("You have beaten hades enough")
    if reunited_orpheus: # bisa pakai boolean statement juga
     if avg_affection_over_5:
      print("You have unlocked the True Ending")

