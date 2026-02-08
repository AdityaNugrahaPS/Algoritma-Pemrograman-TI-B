# While
print("-While-")
i = 0
while i <= 20:
    print(i)
    i += 5
print('')

# Break
print("-Break-")
i = 0
while i < 30:
    print(i)
    if i >= 21:
        break # Berakhir lewat 21
    i += 7
print("")

# Continue
print("-Continue-")
i = 0
while i < 10:
    i += 1
    if i == 4: # Dilampaui
        continue
    print(i)
print("")

# Else
print("-Else-")
i = 10
while i <= 50:
    print(i)
    i += 4
else:
    print("Melebihi 50.") 