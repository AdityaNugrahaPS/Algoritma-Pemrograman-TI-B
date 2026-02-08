#for loops = execute a block of code a fixed number of times. 
#            you can iterate over a range, string, sequence, etc.     


for x in reversed ( range (1, 11) ):
    print(x)

print("Teknik Satu!")
print()

for x in range (1, 11, 2) :
    print(x)
print()

for x in range (1, 21) :
    if x == 15:
        continue
    else:
        print(x)