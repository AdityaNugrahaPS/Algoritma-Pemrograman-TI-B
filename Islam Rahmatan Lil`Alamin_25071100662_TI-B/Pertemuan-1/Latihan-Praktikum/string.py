# String nerupakan tipe data yang digunakan untuk menyimpan kumpulan karakter
# String bisa dibuat dengan menggunakan tanda petik satu atau petik dua
nama1 = 'Alam'
nama2 = "Ganteng"
print(type(nama1))  #output: str
print(type(nama2))  #output: str

## Ada beberapa cara dalam menggunakan string dalam program python
# 1. kita bisa menggabungkan string dengan operator +
nama_lengkap = nama1 + ' ' + nama2 # (' ' digunakan untuk biar ada spasi diantara nama1 dan nama2)
print(nama_lengkap)  #output: Alam Ganteng

# 2. kita juga bisa menggabungkan string dengan operator (,)
print(nama1, nama2) #output: Alam Ganteng  langsung ada spasinya 

# kita juga bisa mengulang string dengan operator *
slogan = 'oke gas'
print((slogan + " ") * 3) #output: oke gas oke gas oke gas


## Ada bberapa cara dalam melakukan formatting string di python
# 1. f-string (formatted string)
umur = 18
dataDiri = f'Nama saya {nama_lengkap}, umur saya {umur} tahun.'
print(dataDiri)  #output: Nama saya Alam Ganteng, umur saya 18 tahun.

# 2. %-formatting
dataDiri2 = 'Nama saya %s, umur saya %d tahun.' % (nama_lengkap, umur)
print(dataDiri2)  #output: Nama saya Alam Ganteng, umur saya 18 tahun. 

# 3. str.format() method
dataDiri3 = 'Nama saya {}, umur saya {} tahun.'.format(nama_lengkap, umur)
print(dataDiri3)  #output: Nama saya Alam Ganteng, umur saya 18 tahun.



# kita bisa mengakses karakter pada string dengan indeksing dan slicing
# 1. Indeksing
kata = 'mempertanggungjawabkannya'
print(kata[0])    #output: m (mengakses karakter pertama)
print(kata[5])    #output: r (mengakses karakter ke 6)
print(kata[-1])   #output: a (mengakses karakter terakhir)
print(kata[-4])   #output: n (mengakses karakter ke 4 dari belakang)

# 2. Slicing
print(kata[0:7])    #output: mempert                (menampilkan karakter dari indeks 0 sampai 6)
print(kata[7:])     #output: anggungjawabkannya     (menampilkan karakter dari indeks 7 sampai akhir)
print(kata[:10])    #output: mempertang             (menampilkan karakter dari awal sampai indeks 9)
print(kata[3:15])   #output: pertanggungj           (menampilkan karakter dari indeks 3 sampai 14)
print(kata[::2])    #output: mmetngnjwbana          (menampilkan karakter dari awal sampai akhir dengan langkah 2)
print(kata[::-1])   #output: aynaknabuajgnutrepmem  (menampilkan karakter dari akhir sampai awal dengan langkah -1, jadi membalik string)


## berikut adalah beberapa method bawaan string yang sering digunakan
teks = "Aku adalah mahasiswa paling pintar dan ganteng se angkatan"
# merubah ukuran huruf
print(teks.lower())        #output: aku adalah mahasiswa paling tampan dan ganteng se angkatan   (mengubah semua karakter menjadi huruf kecil)
print(teks.upper())        #output: AKU ADALAH MAHASISWA PALING TAMPAN DAN GANTENG SE ANGKATAN   (mengubah semua karakter menjadi huruf besar)

# menghapus karakter tertentu
teks = "     Aku adalah mahasiswa paling pintar dan ganteng se angkatan    "
print(teks.lstrip())      #output: (Aku adalah mahasiswa paling tampan dan ganteng se angkatan    )    (menghilangkan spasi di awal string)
print(teks.rstrip())      #output: (     Aku adalah mahasiswa paling tampan dan ganteng se angkatan)   (kebalikannya, menghilangkan spasi di akhir string)
print(teks.strip())       #output: (Aku adalah mahasiswa paling tampan dan ganteng se angkatan)        (menghilangkan spasi di awal dan akhir string)

# beberapa method string lainnya
teks = "Aku adalah mahasiswa paling pintar dan ganteng se angkatan"
print(teks.replace("mahasiswa", "manusia"))  #output: aku adalah manusia paling tampan dan ganteng se angkatan (mengganti kata "mahasiswa" dengan "manusia")  
print(teks.split())       #output: ['Aku', 'adalah', 'mahasiswa', 'paling', 'pintar', 'dan', 'ganteng', 'se', 'angkatan']  (memecah string menjadi list berdasarkan spasi)
print(teks.find("ganteng"))  #output: 39 (mencari indeks pertama dari kata "ganteng")
print(teks.count("o"))    #output: 0 (menghitung jumlah kemunculan karakter 'o' dalam string)
print(len(teks))          #output: 58 (menghitung panjang string termasuk spasi)

