#while loop dapat menjalankan serangkaian pernyataan selama kondisi masih bernilai True
i = 1
while i < 7:
    print(i)
    i += 1

#break statement dapat menghentikan loop walaupun kondisi masih bernilai True
i = 1
while i < 7:
    print(i)
    if i == 4:
        break #loop akan berhenti ketika i = 4
    i += 1

#continue statement dapat menghentikan iterasi saat ini dan akan lanjut ke iterasi selanjutnya
i = 0
while i < 7:
    i += 1
    if i == 4:
        continue
    print(i)

#else statement dapat menjalankan blok kode sekali ketika kondisi sudah bernilai False
i = 1
while i < 7:
    print(i)
    i += 1
else:
    print('i sudah tidak lebih kecil dari 7')