#Bagian ini berisi cara mencetak output ke layar

#Untuk mencetak output, kita bisa memakai print(""), atau print('')
print("File ini adalah output.py")

#Untuk mencetak variabel, bisa menggunakan + atau menggunakan f diawal untuk memakai banyak variabel sekaligus
#Pakai {} untuk memakai lebih dari 1 variabel
Nama = "Kiell"
Nama1= 'Ilyas'

print('namaku adalah '+ Nama)
print(f"{Nama} lebih jago dari {Nama1}")

#Kalau ingin mencetak di 1 baris yang sama, bisa memakai parameter end
print("Hai nama saya upin ", end= '')
print("dan ini adik saya ipin")

#kita bisa juga langsung print angka didalam perintah print ini
print(5)
print(5+1)
print("hari ini aku akan berumur", 35, "tahun")