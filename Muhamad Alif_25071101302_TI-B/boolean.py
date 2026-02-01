# print(10 > 9)
# print(10 == 9)
# print(10 < 9)

a = 470
b = 40

if b > a:
  print("true")
else:
  print("false")

# Most Values are True
'''dievaluasi sebagai True jika memiliki semacam konten.

Semua string adalah True, kecuali string kosong.

Semua angka adalah True, kecuali 0.

Semua daftar, tuple, set, dan kamus adalah True, kecuali yang kosong.'''

bool("abc")
bool(123)
bool(["apple", "cherry", "banana"])

#Some Values are False
'''tidak banyak nilai yang dievaluasi menjadi False, kecuali nilai kosong, 
seperti (), [], {}, "", angka 0, dan nilai None. Dan tentu saja nilai 
False dievaluasi menjadi False.'''
bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})

'''Satu nilai lagi, atau objek dalam hal ini, 
dievaluasi menjadi False, dan itu terjadi jika 
Anda memiliki objek yang dibuat dari kelas dengan 
fungsi __len__ yang mengembalikan 0 atau False:'''

class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# not, or, and, xor

# Functions can Return a Boolean
'''Anda dapat membuat fungsi yang mengembalikan nilai Boolean:'''
def myFunction() :
  return True

print(myFunction())

'''Anda dapat menjalankan kode berdasarkan jawaban 
Boolean dari suatu fungsi:'''
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

'''Python juga memiliki banyak fungsi bawaan yang 
mengembalikan nilai boolean, seperti fungsi 
isinstance(), yang dapat digunakan untuk menentukan 
apakah suatu objek memiliki tipe data tertentu:'''
x = 200
print(isinstance(x, int))

#NOT
a = True
c = not a
print('data a =',a)
print('data c =',c)

#OR
a = True
b = False
c = a or b
print(a,'or',b,'=',c)

#and
a = True
b = False
c = a and b
print(a,'and',b,'=',c)

#xor
a = True
b = False
c = a ^ b
print(a,'xor',b,'=',c)