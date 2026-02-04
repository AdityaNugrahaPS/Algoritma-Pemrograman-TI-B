#### Berikut ini merupakan cara" membuat syntax

### 1. Indentasi
## Cara yg benar
if 8*8 == 6*4:
    print('that simple')
else :
    print('yang waras ya')

## Cara yg salah
# kita tidak bisa menggunakan try except biasa karena kesalahan terjadi saat proses kompilasi. jadi, sebelum kode dijalankan proses telah dihentikan
salahIndentasi = ''' 
if 'aku' == 'dia':
print("Kita bersama selamanya")
else :
print("Kita takkan bisa bersatu")
''' # di blok kode diatas jika mengabaikan simbol petik, dapat dilihat bahwa terdapat kesalahan berupa tidak adanya indentasi yang dapat menyebabkan pengecualian IndentationError
try :
    exec(salahIndentasi) # Dengan fungsi exec() ini kita bisa menjalankan kode baru saat program sedang dijalankan, jadi bisa terhindar dari kesalahan compiler gagal membaca program
except IndentationError: # Menangkap jika mendapatkan pengecualian IndentationError maka dia akan mengeksekusi blok kode dibawahnya
    print("Ini merupakan contoh yang salah karena tidak adanya indentasi")

#=============================================================================================================#

### 2. Variabels
# Di Python, sudah tidak diperlukan lagi untuk mendeklarasikan tipe data diawal variabel dikarenakan sudah menggunakan tipe data yang dinamis
nama = 'Alam'
umur = 18
tinggi = 1,66
mahasiswaAktif = True

#=============================================================================================================#

### 3. Comments
# Dalam Python, comment dilakukan menggunakan simbol hash atau yang biasa dipanggil hashtag '#' dan diikuti dengan kalimat yang menjelaskan sesuatu atau sebagai dokumentasi
# halo, aku adalah comment## contoh membuat intruksi
# 1.
print("1 + 1 = 2")

# 2.
nama = 'alam' 


#=============================================================================================================#
#=============================================================================================================#


## Terdapat 2 cara dalam membuat beberapa Intruksi atau statement
# 1.Cara biasa
print('Halo')
print('apa kabar?')
print('pinjam dulu 100')

# 2. dengan semicolon (jarang digunakan)
print('halo'); print('Apa kabar?'); print('pinjam dulu 100') # Jika tidak dipisah dengan semicolon maka akan menghasilkan SyntaxError
