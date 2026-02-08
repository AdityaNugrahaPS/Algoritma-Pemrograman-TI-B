'''
for loop dipakai untuk mengulang setiap item di dalam suatu kumpulan data (list, string, dll) dan menjalankan kode satu per satu untuk setiap elemen.
'''

jari = ['jempol','telunjuk', 'kelingking', 'tengah', 'manis', 'kelingking']
for j in jari:
    print(j)

#looping pada string
#String juga bisa di-loop karena isinya huruf-huruf.
for x in "salwa":
    print(x)

#break pada for 
#break dipakai untuk menghentikan loop sebelum semua data diproses.
jari = ['jempol','telunjuk', 'kelingking', 'tengah', 'manis', 'kelingking']
for j in jari:
    print(j)
    if j == "manis":
        break

#continue pada for
#dipakai untuk melewati satu indeks, lanjut ke berikutnya
jari = ['jempol','telunjuk', 'kelingking', 'tengah', 'manis', 'kelingking']
for j in jari:
    if j == "manis":
        continue
    print (j)

#range( function)
#untuk membuat urutan angka
for i in range(20):     
    print(i)
for i in range(50, 1000):       #angka dimulai di tentukan yaitu dari 50
    print(i)

#else pada for
#dijalankan jika loop selesai (tanpa break).  
for i in range(3):
    print(i)
else:
    print("Loop selesai")

#Nested Loop (Loop di dalam Loop)
#satu loop di luar, di dalamnya ada loop lagi.
warna = ["pink", "biru"]
buah = ["mangga", "semangka"]
for w in warna:
    for b in buah:
        print(w, b)
     
#pass Statement
#jika struktur harus ada, tapi belum mau isi kodenya.
for i in range(3):
    pass