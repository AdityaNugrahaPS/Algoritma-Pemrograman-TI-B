# Print bisa menggunakan Double Quotes maupun Single Quotes
print("Nama Saya Faiz!")
print('Hai Semuanya!')

# Print akan mengalami Error apabila tidak ada Quotesnya
print(Universitas Riau)

# Apabila ingin mengprint angka tidak butuh Quotes
print(3)
print(358)
print(50000)

# Bisa Menggabungkan Print Number dan text dengan memisahkannya dengan koma
print("I am", 35, "years old.")

# Menggunakan sebuah variabel untuk memudahkan dalam print apabila saat codingannya sudah banyak
nama = 'adit'
print(f'halo nama saya {nama}')

# Untuk menghitung menggunakan enumerate
Orang = ['adit','sopo','jarwo']
for i, name in enumerate (Orang):
    print(f'Halo Peserta {i}, {name}')