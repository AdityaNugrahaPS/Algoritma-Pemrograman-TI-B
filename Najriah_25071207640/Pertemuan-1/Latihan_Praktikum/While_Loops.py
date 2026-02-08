#1. While Loops
'''
Dengan perulangan while, kita dapat menjalankan sekumpulan pernyataan selama 
suatu kondisi bernilai benar (true).
'''
print("--While Loops--") #Menampilkan header

#Cetak i selama saya kurang dari 6
i = 1
while i < 6: 
  print(i)
  i += 1

#2. Break Statement
'''
Dengan pernyataan break kita dapat menghentikan loop bahkan jika sementara kondisi benar
'''
print("\n--Break Statement--") #Menampilkan header

#Keluar dari loop saat i = 3
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

#3. Continue Statement
'''
Dengan pernyataan Continue kita dapat menghentikan iterasi saat ini, 
dan lanjutkan dengan iterasi berikutnya.
'''
print("\n--Continue Statement--") #Menampilkan header

#Lanjutkan ke iterasi berikutnya jika i = 3
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#4. Else Statement
'''
Dengan pernyataan else kita dapat menjalankan blok kode sekali 
ketika kondisi tidak lagi benar.
'''
print("\n--Else Statement--") #Menampilkan header

#Mencetak pesan setelah kondisinya salah
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")