'''
while loop adalah perulangan yang akan terus berjalan selama suatu kondisi bernilai True.
'''

#while loop
i = 1   #nilai awal
while i < 10:   #syarat/batas
    print(i)
    i += 1  #agar i terus bertambah dan berhenti

    #break : untuk menghentikan loop
    #dipakai untuk keluar dari loop walaupun kondisi masih True.
i = 1
while i < 10:
    print(i)
    if i == 7:  #saat i=7 maka loop langsung berhenti
        break
    i += 1
    
    #continue : untuk melewati iterasi saat ini dan lanjut ke iterasi berikutnya
i = 0
while i < 6:
    i += 1
    if i == 3:  #angka 3 dilewati/tidak dicetak
        continue
    print(i)   

    #else : else akan dijalankan kalau loop selesai (tanpa break).
angka = 3
while angka > 0:
    print("hitung:", angka)
    angka += 1
else:
    print("hitungan selesai")