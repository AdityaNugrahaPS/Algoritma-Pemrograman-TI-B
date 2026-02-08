#Bagian ini menjelaskan cara memanipulasi string atau teks

a = "Halo semuanya!"

#Pertama adalah slice, yang bisa mengambil sebagian karakter yang kita mau
print(a[2:7]) #artinya kita mengambil hanya dari indeks 2 sampai 7

#Kedua adalah modify, kita bisa memodifikasi string sesuai perintah kita
print(a.upper())           #agar teks menjadi huruf besar semua
print(a.lower())           #agar teks menjadi huruf kecil semua
print(a.replace("H", "J")) #agar mengganti huruf H dengan huruf J

#Ketiga adalah penggabungan string
b = "Hai"
c = "semua"
d = b + " " + c #yang kosong untuk spasi
print(d)