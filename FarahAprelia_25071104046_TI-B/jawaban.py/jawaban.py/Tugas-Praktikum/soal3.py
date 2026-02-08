#If Else

nilai = range(1, 101) #Menggunakan range 1 - 101 agar angka 100 ikut terhitung namun 101 tidak
skor = 75

if skor >= 60: #Jika skor lebih besar atau sama dengan 60
  print("Lulus") #Cetak "Lulus"
  if skor < 60: #Jika skor kurang dari 60
    print("Tidak Lulus") #Cetak "Tidak Lulus"
  else:
    pass #Pass hanya sebagai placeholder dan tidak bernilai apapun (null)