#FOR LOOPS (Untuk melakukan iterasi atau pengulangan secara berurutan sesuai apa yang tertera. Adapun list, tuple, string atau dict)

hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"] #Nama-nama hari akan dideklarasikan lebih dulu
for a in hari: #Kemudian setelah mendeklarasikan syntax for-loops, nama-nama hari yang sebelumnya dideklarasikan akan dicetak ulang
  print(a) #Syntax untuk mencetak nama-nama hari yang sudah dideklarasikan

#FOR LOOPS DENGAN BREAK

hari = ["senin", "selasa", "rabu", "kamis", "jumat", "sabtu", "minggu"] #Deklarasikan nama-nama hari terlebih dulu
for a in hari:
  print(a)
  if a == "kamis": #Loop akan berhenti ketika a adalah hari kamis
    break

#FOR LOOPS DENGAN RANGE()

for a in range(10): #Range(10) artinya bukan mencetak angka 1 sampai 10, namun angka 0 sampai 9. Karena di dalam parameter, angka awal tidak ditentukan, maka default angka pertama adalah 0 dan bukan 1
  print(a)

#Contoh lain

for a in range(1, 10): #Karena pada parameter sudah ditentukan angka untuk urutan pertama, yaitu angka 1, maka output akan menghasilkan angka 1 sampai 9
  print(a)

#FOR LOOPS DENGAN ELSE

for a in range(10):
  print(a)
else:
  print("Selesai dijalankan.")

#Note: else tidak akan dieksekusi jika loop dihentikan oleh break