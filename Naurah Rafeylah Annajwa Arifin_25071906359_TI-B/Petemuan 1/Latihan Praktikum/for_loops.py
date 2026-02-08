#for loop
hero = ["Phainon", "Cyrene", "Navendra"] #list hero
for x in hero:
    print(x) #untuk menampilkan setiap hero dalam daftar

#looping through a string
for x in "Anaxa":
    print(x)

#the break statement
hero = ["Phai", "Cery", "Aven"]
for x in hero:
    print(x)
    if x == "cery": #loop berhenti ketika mencapai "cery"
     break

#the continue statement
hero = ["phai", "cery", "aven"]
for x in hero:
   if x == "cery": #untuk melewati "cery"
      continue
   print(x)

#the range function
for x in range(7): #akan menampilkan rentang angka dari 0 sampai 6
   print(x)

for x in range(2, 7): #akan menampilkan rentang angka dari 2 sampai 6
   print(x)

for x in range(3, 30, 3): #akan menampilkan rentang angka dari 2 sampai 30 dengan kelipatan 3
   print(x)

#else in for loop
for x in range(7):
   print(x)
else:
   print("finish")

#nested else
element = ["Wind", "Imaginary", "Physical"]
char = ["Dan Heng", "Danil", "Terrae"]
for x in element:
   for y in char:
      print(x, y)

#the pass statement
for x in [0,1,2]:
  pass