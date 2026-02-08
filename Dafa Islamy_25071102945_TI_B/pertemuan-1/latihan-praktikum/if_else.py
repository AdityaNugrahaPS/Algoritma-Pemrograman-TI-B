#sub-bab 'python if'

x = 61
y = 145
if x < y:
  print('nilai x lebih dari y') #if statement menghasilkan kondisi (bernilai booolean), jika kondisi bernilai True maka blok kode didalam if statement akan dieksekusi, jika bernilai False, blok kode diabaikan
#if statement harus diberi identasi agar blok kode dapat dieksekusi, identasi dapat menggunakan spasi atau tab


#sub-bab 'python elif'

a = 66
b = 66
if b > a:
  print("b lebih besar dari a") #karena pernyataan bernilai False maka pengecekan dilanjutkan ke pernyataan selanjutnya
elif a == b:
  print("a dan b bernilai sama") #karena pernyataan bernilai True maka 'a dan b bernilai sama' dicetak


skor = 75
if skor >= 90:
  print("Penilain: A")
elif skor >= 80:
  print("Penilain: B")
elif skor >= 70:
  print("Penilain: C")
elif skor >= 60:
  print("Penilain: D")
# elif statement melakukan pengecekan dari atas kebawah, jika telah ditemukan pernyataan dengan nilai True, blok kode akan dieksekusi dan sisa blok kode lainnya diabaikan


#python else

a = 123
b = 23
if a < b:
  print('Nilai a lebih kecil dari b') #karena pernyataan bernilai False maka pengecekan dilanjutkan ke pernyataan selanjutnya
else:
  print('Nilai a lebih besar dari b') #karena pernyataan bernilai True maka 'Nilai a lebih besar dari b' dicetak

temperatur = 22
if temperatur > 30:
  print("Hari ini cuacanya panas")
elif temperatur > 20:
  print("Hari ini cuacanya hangat")
elif temperatur > 10:
  print("Hari ini cuacanya sejuk")
else:
  print("Hari ini cuacanya dingin")


#sub-bab 'shorthand if'

x = 6
y = 16
if x < y: print ('x lebih kecil dari y') #jika hanya ada satu pernyataan yang ingin di eksekusi, pernyataan tersebut dapat diletak pada baris yang sama dengan if statement

x = 6
y = 16
print('X') if x > y else print('Y') #jika terdapat satu pernyataan untuk if dan satu untuk else, pernyataan dapat diletak pada baris yang sama dengan menggunakan conditional expression atau biasa disebut "ternary operator"

a = 10
b = 20
lebihBesar = a if a > b else b
print('Bilangan yang lebih besar adalah', lebihBesar)

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #conditional expression dapat digabung dalam satu baris

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value) #operator ternary berguna untuk penugasan yang sederhana dan pernyataan pengembalian


#sub-bab 'logical operators'

'''
and = mengembalikan True hanya jika kedua pernyataan bernilai True
or = mengembalikan True jika setidaknya satu pernyataan bernilai True
not = kebalikan dari hasil, jika hasil True maka output nya False
'''

#penggunaan operator logika 'and'
x = 6
y = 66
z = 666
if x < y and y < z:
  print('Kedua pernyataan benar')

#penggunaan opertaor logika 'or'
x = 6
y = 66
z = 666
if x < y or y > z:
  print('Setidaknya satu pernyataan benar')

#penggunaan operator logika 'not'
x = 6
y = 66
if not x > y:
  print('x tidak lebih besar dari y')

#penggunaan gabungan operator logika
umur = 18
siswa = False
punyaKupon = True
if (15 < umur or umur > 30) and not siswa or punyaKupon:
  print('Diskon diterima')


#sub-bab 'nested if'

#pernyataan if dapat ditumpuk dan disebut sebagai nested if
x = 16
if x > 10:
  print('Lebih dari 10,')
  if x > 20:
    print('dan juga lebih dari 20')
  else:
    print('tetapi tidak lebih dari 20')

#terkadang nested if dapat disederhanakan dengan menggunakan operator logika 'and 
temperatur = 30
cuacaCerah = True
if temperatur > 25:
  if cuacaCerah:
    print('Cuaca sangat cerah hari ini')

temperatur = 30
cuacaCerah = True
if temperatur > 25 and cuacaCerah:
  print('Cuaca sangat cerah hari ini')


#sub-bab 'pass statement'

#if statement tidak boleh kosong, tetapi jika if statement ingin dibuat kosong atau tidak melakukan apa-apa, dapat menggunakan pass statement
x = 6
y = 66
if x < y:
  pass

'''
pass statement berguna ketika :
- saat membuat struktur kode tetapi belum mengimplementasikan logikanya
- saat sebuah pernyataan diperlukan secara sintaksis tetapi tidak diperlukan tindakan apa pun
- sebagai tempat penampung untuk kode di masa mendatang selama pengembangan
- dalam fungsi atau kelas kosong yang direncanakan untuk diimplementasikan nanti
'''

nilai = 50

if nilai < 0:
  print('Bilangan merupakan bilangan negatif')
elif nilai == 0:
  pass # Zero case - no action needed
else:
  print("Bilangan merupakan bilangan positif")