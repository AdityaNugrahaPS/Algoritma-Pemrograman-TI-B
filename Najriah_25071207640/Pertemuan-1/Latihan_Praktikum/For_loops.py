#1. For Loops
'''
Loop for digunakan untuk mengulangi urutan 
'''
print("--For Loops--") #Menampilkan header

#Cetak setiap teman di dalam daftar
friends = ["arum", "endang", "desty"]
for x in friends:
  print(x)

#2. Break Statement
'''
Dengan pernyataan break kita dapat menghentikan loop sebelum memutar semua item
'''
print("\n--Break Statement--") #Menampilkan header

#Keluar dari Loops jika x adalah "endang"
friends = ["arum", "endang", "desty"]
for x in friends:
  print(x)
  if x == "endang":
    break
  
#3. Continue Statement
'''
Dengan pernyataan Continue kita dapat menghentikan iterasi loop saat ini, 
dan melanjutkan ke pernyataan berikutnya
'''
print("\n--Continue Statement--") #Menampilkan header

#Jangan mencetak "endang"
friends = ["arum", "endang", "desty"]
for x in friends:
  if x == "endang":
    continue
  print(x)

#4. Else in For Loops
'''
Kata kunci else dalam perulangan for menentukan blok kode yang akan dieksekusi saat loop selesai
'''
print("\n--Else in For Loops--") #Menampilkan header

#Cetak semua angka dari 0 hingga 5, dan cetak pesan saat perulangan telah berakhir
for x in range(6):
  print(x)
else:
  print("Finally finished!")

#5. Nested Loops
'''
Perulangan bersarang adalah perulangan di dalam perulangan.
'''
print("\n--Nested Loops--") #Menampilkan header

tinggi = 5
for i in range(1, tinggi + 1):
    for j in range(i):
        print("*", end="")
    print()

#6. Pass Statement
'''
Perulangan for tidak boleh kosong, tetapi jika karena suatu alasan kamu memiliki 
perulangan tanpa isi, masukkan pernyataan pass untuk menghindari terjadinya galat (error).
'''
print("\n--Pass Statement--")

for x in [0, 1, 2]:
  pass