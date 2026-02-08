
#untuk menampilkan output, kita bisa menggunakan perintah print()

#cara penulisan untuk menampilkan output bertipe data string
nama = 'Rania' #tanda kutip untuk string boleh menggunakan (""), atau ('')

'''
untuk menampilkan output, kita bisa menggunakan beberapa metode, berikut metode yang dapat
kita gunakan : 
'''

#METODE 1
#untuk mencetak beberapa kata yang sama tetapi terpisah di kodenya, bisa kita gunakan parameter end =
#berikut contohnya:

print("ini teks pertama yang akan di gabung dengan", end="")
print('ini teks keduanya yang akan di gabung dengan teks pertama')

# METODE 2, karena kita sudah mengisi variabel nama dengan 'Rania', berikut beberapa cara pemanggilannya: 
print('Hallo, nama saya ' +nama) #dengan memanggill variabel dengan +
# METODE 3
print(f"Hello nama saya {nama}") #dengan memanggil variabel degan kurung kurawal {}
# METODE 4
print('Hello nama saya',nama) #dengan memanggil variabel dengan tanda koma, lalu nama variabel

namateman = 'fildza'

# METODE 5
print(f"{nama} punya teman, namanya {namateman}") #dengan mengetik f sebelum kata katanya, lalu variabel yang di panggil menggunakan kurung kurawal {}



"""
 PRINT NUMBERS
selain tipe data string, kita juga bisa mencetak angka dalam program, nama tipe datanya adalah Numbers.
jika string harus diapit oleh tanda kutip, Numbers tidak perlu
"""

#contoh mencetak Angka

print(3)
print(3829)




# METODE 6 kita akan menambahkan variabel umur untuk dicetak bersama dengan variabel nama (DI MIX NUMBERS DAN TEXT)
umur1 = 18
umur2 = 19
print (f"{nama} berumur {umur1} tahun 2025, tahun 2026 {umur2} tahun")

namateman2 ='najwa'

# METODE 7
print(f'si {nama} lagi belajar ngoding menggunakan python dengan {namateman}, dan {namateman2}.')



'''
kita juga bisa melakukan operasi aritmatika di program ini, jika di bahasa pemprograman lain, kita
harus mendeklarasikan tipe data, di Python kita tidak perlu melakukan itu. berikut contohnya
'''
angka = 2 #mengisi nilai 2 ke variabel angka
angkalagi = 3 #mengisi nilai 3 ke variabel angkalagi
print(angka + angkalagi) #hasil pertambahan dari 2 + 3
print(angka - angkalagi) #hasil pengurangan dari 2 - 3
#materi operasi aritmatika akan dijelaskan lebih lanjut di bab operator

#OUTPPUT DONE
