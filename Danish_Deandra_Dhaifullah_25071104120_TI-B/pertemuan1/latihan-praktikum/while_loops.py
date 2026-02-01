#WHILE

#it runs the commands as long as the condition is true

i = 1
while i <= 20: # selama i tidak sama dengan 20
    print(i) # akan print i mulai dari 1
    if i == 10: 
     break #break digunakan untuk menghentikan programnya saat kondisi diatas dipenuhi
    i += 1 # ini supaya diline selanjutnya i akan ditambah dengan 1

j = 0
while j <= 10:
   j += 1
   if j == 5:
     continue # continue untuk menghentikan iterasi dan mulai dari kondisi di atas tapi angka diatas tidak dihitung print
   print(j)

k = 1
while i <= 15:
   print(i)
   i += 1
else: # bisa gunakan else statement untuk mengeprint perintah
   print("i is no longer less than 15")
 