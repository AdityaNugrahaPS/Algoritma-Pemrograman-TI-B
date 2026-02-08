'''
Boolean adalah tipe data yang hanya punya dua nilai, yaitu true (benar) dan false (salah).
biasanya dibuat untuk membuat keputusan dalam program.
'''

#boolean values
print(10 > 9)
print(10==9) 
print(10 < 9)

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#evaluates values dan variabel
  #bisa mengevaluasi angka, teks, atau variabel menjadi Boolean dengan bool().  
print(bool("pagi"))
print(bool(200))
print(bool(0))  #false, karena python melihat apakah nilainya “kosong/tidak ada” atau “ada”. 
                

x = 30
y = 15
print(bool(x))
print(bool(y))

#Most Values are True
  #semua nilai dianggap true juka memiliki isi atau konten/tidak kosong
print(bool("pqr"))
print(bool(345))
print(bool(["mangga", "jambu", "pisang"])) 

#Some Values are False
  #nilai yang dievaluasi false hanya nilai kosong, seperti contoh berikut:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({})) 
  #objek dievaluasi menjadi False, jika Anda memiliki objek yang dibuat dari kelas dengan fungsi __len__ yang mengembalikan 0
class Kotak:
    def __len__(self):
        return 0
kotak = Kotak()
print(bool(kotak)) 

#Functions can Return a Boolean
  #sebuah fungsi bisa mengembalikan nilai Boolean menggunakan return True atau return False.
def lampu_nyala():
    return True

print(lampu_nyala())