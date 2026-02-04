#Perbedaan local scope dan global scope
#Global scope tidak bisa dipanggil ke local scope, namun local scope bisa dipanggil ke global, dan konstanta

#Local scope
def myfunc():
  x = 300
  print(x)

myfunc()

#Lambda
x = lambda a : a + 10
print(x(5))

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

#Fungsi rekursif (pemanggilan terhadap diri sendiri)
def countdown(n): #Fungsi dengan nama fungsi countdown dengan parameter n
  if n <= 0:
    print("Done!") #Jika n sudah besar sama dengan 0, maka akan print ini
  else:
    print(n)
    countdown(n - 1) #Nilai dikurang 1

countdown(5) #Pemanggilan fungsi countdown

def factorial(n): #Fungsi dengan nama fungsi factorial 
  if n == 0 or n == 1:
    return 1 #Return pasti akan selalu bernilai 1 agar hasil pengurangan tidak minus atau negatif
  else:
    return n * factorial(n - 1) #Pemanggilan ganda

print(factorial(5))

'''
Dalam python, variabel def itu ambigu. Jadi jenis tipe data yang dipanggil akan tergantung pada return.
'''