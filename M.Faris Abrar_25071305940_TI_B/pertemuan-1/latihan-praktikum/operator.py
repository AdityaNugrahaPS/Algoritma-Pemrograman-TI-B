##
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 6:
    print(f"List has {count} elements")

else :
    print("list has no elements")
print()
##
temp = -2
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("algorithm progamming is cancelled")
else:
    print("algorithm programming is still scheduled")
print()

##
temp = 10
is_sunny = True

if temp >= 28 and is_sunny:
    print("it is HOT outside")
    print("and sunny ")
elif temp <= 0 and is_sunny:
    print("it is COLD outside")
    print("and sunny ")
elif  28 > temp > 0 and is_sunny:
    print("it is WARM outside")
    print("and sunny ") 
print()

