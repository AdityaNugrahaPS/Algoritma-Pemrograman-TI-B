#kita inisialisasi duluu geng variabel penampung
jumlah = 0

#loop untuk menampilkan angka dan menghitung total
for i in range(1,11):
    print(i)
    jumlah += i

                                #ini ada masalah indentasi yang tidak sengaja saya temukan
print(f'jumlah ={jumlah} ')    #jika kita menuliskan print dengan sejajar dengan for maka phyton menganggap
                                #ini bukan bagian dari pengulangan

