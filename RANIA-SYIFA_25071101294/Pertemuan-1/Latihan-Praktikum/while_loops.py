#Python Loops
""" 
Python memeiliki 2 perintah perulangan dasar
1. While Loops
2. For Loops
"""

#1. WHILE LOOPS
'''
dalam perulangan ini, kita dapat menjalankan program selama kondisi bernilai benar
'''
#contoh
"membuat perulangan, mmencetak nama 'Rania' selama i kurang dari 10"
i = 1
while i < 10:
    print("Rania")
    i += 1 #selama perulangan, i bertambah 1

"pernyataan jeda (break)"
#kata kunci (break)
'fungsi dari break ini untuk menghentikan pengulangan meskipus pernyataan bernilai benar'

#contoh
'membuat keluar dari perulangan ketika i sudah menjadi 3'
i = 1
while 1 < 10:
    print("Syifa")
    if i == 5:
        break
    i += 1

"pernyataan lanjutan (continue)"
#kata kunci (continue)
'fungsi ini dapat menghentikan iterasi saat ini, lalu melanjutkan ke iterasi berikutnya'

#contoh
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

"pernyataan else"
#kata kunci (else)
'menjalankan blok kode sekali saja ketika kondisi tersebut tidak lagi benar'

#contoh
i = 1
while i < 6:
  print('Rania')
  i += 1
else:
  print("Syifa")


#WHILE LOOP DONE