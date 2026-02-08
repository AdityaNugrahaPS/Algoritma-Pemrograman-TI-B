'''
Soal 4 (Perulangan)

Buat sebuah program Python yang:
1. Menggunakan perulangan for
2. Menampilkan bilangan dari 1 sampai 10
3. Menghitung dan menampilkan jumlah dari bilangan 1 sampai 10
'''

total = 0

for x in range(0, 11):
    print(x) #output akan menghasilkan urutan angka mulai dari 0 sampai 10, 11 tidak termasuk
    total += x

print('Jumlah =', total) #output = Jumlah = 55