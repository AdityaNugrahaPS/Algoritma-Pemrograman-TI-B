'''
di python for loop digunakan untuk mengiterasi item dari sebuah koleksi (seperti list, tuple, string, dll)
 bukan untuk menghitung i dari 1 sampai n
'''
buah = ['apel', 'jeruk', 'mangga'] # list buah-buahan   
for b in buah: # untuk setiap elemen b dalam list buah
    print("Saya suka buah", b) # tampilkan elemen b

for x in 'halo': # untuk setiap karakter x dalam string 'halo'
    print(x) # tampilkan karakter x

for x in 'halo':
    print(x)
    if x == 'a': # jika karakter x adalah 'a'
        break # hentikan perulangan

for x in 'halo':
    if x == 'a': # jika karakter x adalah 'a'
        continue # lewati iterasi ini
    print(x) # tampilkan karakter x

for i in range(1, 6): # range(1,6) menghasilkan angka dari 1 sampai 5
    print("Perulangan ke-", i) # tampilkan nilai i

for i in range(1, 100, 10): # angka ketiga adalah step/nilai penambahannya
    print("Nilai i adalah", i) # tampilkan nilai i

for i in range(1, 6):
    print("Perulangan ke-", i)
else:
    print("Perulangan selesai") # blok else setelah for selesai

katasifat = ['enak', 'sangat enak', 'selalu enak']
makanan = ['nasi goreng', 'sate', 'bakso']

for sifat in katasifat:
    for makan in makanan: # kalau nama iterator sama nanti rusak, jadi ga bisa 'for makanan in makanan'
        print(f'{makan} itu {sifat}') # for loop dua tingkat/lapis

for x in [0, 1, 2]:
    pass # pass artinya tidak melakukan apa-apa, hanya sebagai placeholder