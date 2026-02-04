# ada beberapa cara dalam menggunakan python

# Cara biasa
x = "matematika"
y = 5

print(x)
print(y)


#Karena variabel tipe datanya bersifat dinamis, jadi bisa dirubah saat kode dijalankan
x = 5       
print(type(x)) # output: type = number
x = "Halo"  
print(type(x)) # output: type = string

# Di python, kita bisa memberikan banyak nilai ke beberapa variabel langsung
hewan, buah, sayur = "ayam", 'apel', 'bayam'
print(hewan)  #output: ayam
print(buah)   #output: apel
print(sayur)  #output: bayam

# atau bisa juga satu nilai yang sama diberikan kepada beberapa variabel
aku = kamu = dia = "suka"
print(aku)  #output: suka
print(kamu) #output: suka
print(dia)  #output: suka

# Kita juga bisa menampilkan ke layar beberapa variabel dalam satu output
hewan, buah, sayur = "ayam", 'apel', 'bayam'
print(hewan, buah, sayur)    # output: ayam apel ayam
print(hewan + buah + sayur)  # output: ayamapelbayam
