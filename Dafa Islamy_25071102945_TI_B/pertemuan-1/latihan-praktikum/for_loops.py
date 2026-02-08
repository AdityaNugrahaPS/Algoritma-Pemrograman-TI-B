#for loop digunakan untuk mengulang suatu urutan (baik berupa list, tuple, dictionary, set, atau string)

kendaraan = ['Motor', 'Mobil', 'Sepeda']
for x in kendaraan:
    print(x) #for loop tidak memerlukan variabel pengindeksan yang diatur sebelumnya

#string dapat diiterasi, karena berisi susunan karakter
for x in 'Dafa':
    print(x)

#break statement dapat menghentikan perulangan
kendaraan = ['Motor', 'Mobil', 'Sepeda']
for x in kendaraan:
    print(x)
    if x == 'Mobil':
        break

#continue statement dapat mengehentikan iterasi saat ini dan akan lanjut ke iterasi selanjutnya
kendaraan = ['Motor', 'Mobil', 'Sepeda']
for x in kendaraan:
    if x == 'Mobil':
        continue
    print(x)

#fungsi range() digunakan untuk melakukan pengulangan sekumpulan kode sebanyak jumlah tertentu yang dimulai dari 0 lalu bertambah 1 dan berakhir pada angka yang ditentukan
for x in range(7): #range(7) berisi nilai mulai dari 0-6, jadi angka didalam range tidak termasuk
    print(x)

for x in range(2,7): #range(2,7) berisi nilai mulai 2 hingga 6
    print(x)
    
for x in range(2,20,4): #umumnya penambahan pada fungsi range adalah 1, tetapi bisa diubah dengan menambahkan parameter ketiga
    print(x)

#else statement dapat ditambahkan didalam for loop, tetapi tidak akan berjalan jika didalam for loop terdapat break statement
for x in range(6):
    print(x)
else:
    print(('Selesai'))

#for loop didalam for loop disebut sebagai nested loop
kendaraan = ['Motor', 'Mobil', 'Sepeda']
warna = ['Merah', 'Kuning', 'Hijau']
for x in kendaraan:
    for y in warna:
        print(x, y)

#for loop tidak boleh kosong, tetapi jika ingin dibuat kosong atau tidak melakukan apa-apa, dapat menggunakan pass statement
for x in [0, 1, 2]:
    pass