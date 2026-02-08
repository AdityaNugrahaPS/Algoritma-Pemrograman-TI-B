#menampilkan hasil dari perbandingan ini True atau False
print(10 > 9) 
print(10 == 9)
print(10 < 9)

a = 200
b = 33

if b > a: #bernilai False karena 33 tidak lebih besar dari 200
    print("b lebih besar dari a") #jika b lebih besar daripada a, maka akan menampilkan "b lebih besar dari a"
else:
    print("b tidak lebih besar dari a") #jika tidak, maka akan menampilkan "b tidak lebih besar dari a"

#evaluate values and variable
#cara-cara menampilkan nilai boolean
print(bool("Hi"))
print(bool(335))

x = "Hey"
z = 15
print(bool(x))
print(bool(z))

#most value are True
print(bool("Chreisos Heirs"))
print(bool(33.550))
print(bool(["Dannie", "Evey"]))

#most value are False
print(bool(None))
print(bool(0))
print(bool([]))

#membuat fungsi dengan mengembalikan nilai boolean
def myFunction() :
  return True #sebuah fungsi dengan nilai True

if myFunction(): #jika jika funsi bernilai True, maka tampilkan "YES"
  print("YES!") 
else:
  print("NO!") #jika fungsi bernilai False, maka tampilkan "NO"