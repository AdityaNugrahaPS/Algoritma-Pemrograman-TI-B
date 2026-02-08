#WHILE LOOPS TANPA MENGGUNAKAN BREAK

i = 1 #Variabel i memiliki value sebesar 1
while i < 7: #Ketika i lebih kecil dari 7
  print(i) #Cetak i sampai i tidak lebih besar dari 7
  i += 1 #Setiap perulangan, value i akan ditambah 1. Misal i pertama bervalue 1, maka 1 kedua bervalue 1+1 lalu i ketiga bervalue 2+1 dan seterusnya

#WHILE LOOPS DENGAN MENGGUNAKAN BREAK

i = 1 #Variabel i memiliki value sebesar 1
while i < 7: #Ketika i lebih kecil dari 7
  print(i) #Cetak i
  if i == 5: #Jika i sama besar dengan 5, maka hentikan perulangan
    break
  i += 1 #Value i akan ditambah 1 setiap perulangan hingga i sama besar dengan 5

#WHILE LOOPS DENGAN CONTINUE

i = 0 #Variabel i memiliki value sebesar 0
while i < 7: #Ketika i lebih kecil dari 7
  i += 1 #Value i ditambah 1 setiap perulangan
  if i == 4: #Jika value i sama besar dengan 4
    continue #Maka lanjutkan perulangan
  print(i) #Cetak i

#WHILE LOOPS DENGAN ELSE

i = 1 #Variabel i memiliki value sebesar 1
while i < 7: #Ketika i lebih kecil dari 7
  print(i) #Cetak i
  i += 1 #Value i ditambah 1 pada setiap perulangan hingga i memiliki value yang lebih besar dari 7
else:
  print("i is no longer less than 7") #Jika i sudah lebih besar dari 7, maka akan menghasilkan output berikut