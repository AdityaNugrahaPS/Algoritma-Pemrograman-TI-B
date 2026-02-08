#BOOLEAN
"""
menggunakan fungsi bool() untuk mengevaluasi nilai, lalu menghasilkan keluaran berupa True atau False
"""

#contoh
#mengevaluasi sebuah string dan sebuah angka
print(bool("namaku rania"))
print(bool(25))

"""
hasil dari keluaarn di atas akan menjadi true,
karena tidak ada nilai pembanding ataupun bukan sebuah inputan kosong
"""

#kita kana mencoba mengevaluasi dua variabel

kata1 = "RANIA"
kata2 = "89402"

print(bool(kata1))
print(bool(kata2))

"""
hasil dari keluaarn di atas akan menjadi true,
karena tidak ada nilai pembanding ataupun bukan sebuah inputan kosong
"""

'''
nilai akan dievaluasi menjadi true, jika ada isi nya, contoh:
    - semua string adalah True, kecuali string kosong
    - angka apapun adalah True, kecuali 0
    - semua list, tuple, set, dict adalah True, kecuali yang kosong.
'''
#contoh
print(bool("ini true"))
print(bool(83649))
print(bool(['kata', 9379, 796.8]))
print(bool({'nama': 'rania', 'kelas' : 'TI B'}))

'''
nilai akan dievaluasi menjadi false, jika tidak ada isinya, contoh:
seperti (), [], {}, "", angka 0, dan nilai None
'''
#contoh
print(bool())
print(bool({}))
print(bool([]))
print(bool(0))
print(bool(None))

''' 
ada nilai dievaluasi menjadi False, karena memiliki objek yang dibuat dari 
kelas dengan __len__fungsi yang mengembalikan 0 atau False
'''
#contoh
class contoh():
  def __len__(pernyataan):
    return 0

kata = contoh()
print(bool(kata))

#FUNGSI DAPAT MENGEMBALIKAN NILAI
def contohbool() :
  return True

print(contohbool())

'''kita juga bisa membuat beberapa aksi'''
#contoh
def Rania() :
  return True

if Rania():
  print("Saya")
else:
  print("BUkan Saya")

#kita juga bisa menggunakan boolean untuk menentukan apakah suatu objek memiliki tipe data tertentu
contohbool2 = "ini coba"
print(isinstance(contohbool2, str)) #mengecek apakah variabel contohbool2 itu memili tipe data string atau tidak

#BOOLEAN DONE
