print(10 > 9) #output akan menghasilkan True karena 10 > 9
print(10 == 9) #output akan menghasilkan False karena 10 != 9
print(10 < 9) #output akan menghasilkan False karena 10 > 9


a = 200
b = 33

if b > a:
    print('b is greater than a')
else :
    print('b is not greater than a')


print(bool('Hello')) #semua string akan menghasilkan True kecuali string kosong
print(bool(1234)) #semua angka akan menghasilkan True kecuali 0
print(bool(['Motor', 'Mobil', 'Sepeda'])) #semua list, tuple, set dan dictionary akan menghasilkan True kecuali yang isinya kosong

x = 'Hello'
y = 1234
z = ['Motor', 'Mobil', 'Sepeda']
print(bool('Hello'))
print(bool(1234))
print(bool(['Motor', 'Mobil', 'Sepeda']))

#output akan menghasilkan False
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


#fungsi bisa mengembalikan nilai boolean
def function() :
  return True
print(function()) #output akan menghasilkan 'True'

def function() :
  return False
print(function()) #output akan menghasilkan 'False'

def myFunction() :
  return True
if myFunction():
  print("YES!") #output akan menghasilkan "YES!" karena fungsi berisi return True
else:
  print("NO!") #jika fungsi berisi return False, "NO!" akan ditampilkan ke layar

x = 200
print(isinstance(x, int)) #output akan menghasilkan True karena benar bahwa 200 merupakan biangan bulat (int)