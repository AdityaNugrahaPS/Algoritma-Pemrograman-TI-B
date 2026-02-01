#sub-bab 'python strings'

#string dapat ditulis dengan tanda petik dua maupun tanda petik satu
print("Dafa")
print('Dafa')

#tanda petik lainnya dapat digunakan didalam string asal tanda yang digunakan berbeda dengan tanda pada pada string
print("it's allright")
print("He is called 'Jhonny'")
print('He is called "Johnny"')

#string dapat dimasukkan kedalam variabel
x = 'Dafa'
print(x)

#banyak string juga dapat dimasukkan kedalam variabel dengan menggunakan tanda petik dua maupun tanda petik satu
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#string merupakan array, jadi karakter didalam array dapat dicari menggunakan indeks yang dimulai dari indeks 0
x = 'Dafa Islamy'
print(x[0]) #output akan menghasilkan 'D' karena indeks ke-0 pada string adalah D

for x in "Dafa Islamy":
  print(x) #perulangan for akan menampilkan tiap karakter dari string

x = 'Dafa Islamy'
print(len(x)) #fungsi len() berguna untuk mengetahui panjang dari sebuah string

teks = 'Perkenalkan nama saya Dafa Islamy'
print("Dafa" in teks) #keyword 'in' berguna untuk pengecekan frasa atau karakter didalam string dan akan menampilkan nilai boolean

teks = 'Perkenalkan nama saya Dafa Islamy'
if 'Dafa' in teks:
  print("Benar, 'Dafa' ada didalam teks") #pengecekan juga dapat menggunakan if statement


#sub-bab 'slicing strings'

x = 'Dafa Islamy'
print(x[2:6]) #output akan menampilkan karakter mulai dari indeks ke-2 sampai indeks ke-5 (indeks ke-6 tidak termasuk)

x = 'Dafa Islamy'
print(x[:6]) #output akan menampilkan karakter mulai dari awal string hingga indeks ke-5 (indeks ke-6 tidak termasuk)

x = 'Dafa Islamy'
print(x[6:]) #output akan menampilkan karakter mulai dari indeks ke-6 hingga akhir string

x = 'Dafa Islamy'
print(x[-6:-2]) #indeks dapat bernilai negatif yang berakibat perhitungan indeks dimulai dari akhir string


#sub-bab 'modify strings'

x = 'dafa islamy'
print(x.upper()) #upper() dapat mengubah seluruh string menjadi upper case

x = 'DAFA ISLAMY'
print(x.lower()) #lower() dapat mengubah seluruh string menjadi lower case

x = ' Dafa Islamy  '
print(x.strip()) #strip() dapat menghapus spasi pada awal dan akhir string

x = 'Dafa Islamy'
print(x.replace('y', 'i')) #replace() dapat mengganti string yang sama menjadi string lain

x = 'Dafa Islamy'
print(x.split()) #split() akan memisahkan setiap frasa atau kalimat dan disimpan didalam list items


#sub-bab 'concatanete strings'

a = 'Dafa'
b = 'Islamy'
c = a + b
print(c) #string dapat digabung menggunakan operator +

a = 'Dafa'
b = 'Islamy'
c = a + " " + b
print(c) #untuk menambahkan spasi diantara string dapat menambahkan " "


#sub-bab 'format strings'

#untuk menggabungkan string dan numbers dapat menggunakan f-string
umur = 18
print(f'Saya berumur {umur} tahun')

harga = 16
print(f'Harga baju itu {harga:.2f} dolar') #.2f akan mengubah harga menjadi bilangan desimal dengan dua angka dibelakang koma


#sub-bab 'escape characters'

txt = "We are the so-called \"Vikings\" from the north."
print(txt) #"Vikings" tidak error walaupun menggunkan tanda petik yang sama dengan string-nya karena menggunakan backslash(\)


#sub-bab 'string methods'

#capitalize() mengubah hanya karakter pertama menjadi huruf besar
#casefold() mengubah string menjadi huruf kecil (versi lebih agresif karena bisa mengubah karakter khusus seperti 'ß' dalam bahasa Jerman menjadi ss)
#center() menaruh string di tengah dengan tambahan karakter di kiri-kanannya
#count() mmenghitung berapa kali sebuah huruf/kata muncul
#encode() mengubah string menjadi format bytes
#endswith() mengecek apakah string diakhiri kata tertentu, hasilnya True atau False
#expandtabs() mengatur ukuran tab (\t) menjadi jumlah spasi tertentu
#find() mencari posisi (indeks) pertama sebuah nilai. Jika tidak ada, hasilnya -1
#format() memasukkan nilai ke dalam "template" string menggunakan kurung kurawal {}
#format_map() memasukkan nilai ke dalam "template" string menggunakan kurung kurawal {}
#index() mencari posisi (indeks) pertama sebuah nilai. Jika tidak ada, program akan error
#isalnum() apakah isinya hanya huruf dan angka? (tidak boleh ada spasi/simbol), output nilai boolean
#isalpha() apakah isinya hanya huruf?, output nilai boolean
#isascii() apakah semua karakter dalam sebuah string termasuk dalam tabel ASCII, output nilai boolean
#isdecimal() apakah isinya angka?, output nilai boolean
#isdigit() apakah isinya angka?, output nilai boolean
#isidentifier() apakah sebuah string bisa digunakan sebagai nama variabel, nama fungsi, atau nama kelas yang valid, output nilai boolean
#islower() mengecek apakah semua huruf kecil, output nilai boolean
#isnumeric() apakah isinya angka?, output nilai boolean
#isprintable() apakah sebuah string aman untuk ditampilkan ke layar, output nilai boolean
#isspace() apakah isinya hanya spasi/whitespace, output nilai boolean
#istitle() apakah formatnya sudah seperti judul, output nilai boolean
#isupper() mengecek apakah semua huruf besar, output nilai boolean
#join() kebalikan split(), menggabungkan anggota list menjadi satu string
#ljust() meratakan teks ke kiri
#lower() mengubah seluruh string menjadi huruf kecil
#lstrip() menghapus spasi hanya di kiri
#maketrans() digunakan untuk pemetaan karakter secara massal
#partition() membagi string menjadi 3 bagian: sebelum pemisah, pemisah itu sendiri, dan setelah pemisah
#replace() mengganti kata lama dengan kata baru
#rfind() sama seperti find() tetapi pencarian dimulai dari paling kanan (belakang)
#rindex() sama seperti index() tetapi pencarian dimulai dari paling kanan (belakang)
#rjust() meratakan teks ke kanan
#rpartition() membagi string menjadi 3 bagian: sebelum pemisah, pemisah itu sendiri, dan setelah pemisah, tetapi dimulai dari kanan (belakang)
#rsplit() memecah string menjadi list berdasarkan pemisah (default-nya spasi), tetapi dimulai dari kanan (belakang)
#rstrip() menghapus spasi hanya di kanan
#split() memecah string menjadi list berdasarkan pemisah (default-nya spasi)
#splitlines() memecah string berdasarkan baris baru (\n)
#startswith() mengecek apakah string diawali kata tertentu, hasilnya True atau False
#strip() menghapus spasi di awal dan akhir string
#swapcase() mengubah seluruh huruf kecil menjadi besar dan sebaliknya
#title() mengubah setiap awal kata menjadi huruf besar
#translate() digunakan untuk pemetaan karakter secara massal
#upper() mengubah seluruh string menjadi huruf besar
#zfill() menambah angka 0 di depan string sampai panjangnya terpenuhi