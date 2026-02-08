# selain while loop, ada juga for loop
# biasanya dipake kalo kita udah tau jumlah iterasi nya
# atau buat ngulang sesuatu berdasarkan isi dari tipe data (list, tuple, string, dll)

# 1. for loop dengan range()
print("Contoh for loop dengan range()")
for i in range(1, 6): # range(start, stop) mulai dari 1 sampai 5 (stop itu eksklusif)
    print(i)  #output: 1 2 3 4 5

# 2. for loop dengan list
print("\nContoh for loop dengan list")
buah = ['apel', 'jeruk', 'mangga', 'pisang']
for item in buah:
    print(item)  #output: apel jeruk mangga pisang

# 3. for loop dengan string
kata = "Alam Ganteng Sekali"
for huruf in kata:
    print(huruf)  #output: A l a m   G a n t e n g   S e k a l i  

# 4. kombinasi for loop dengan operasi matematika
angka = [1, 2, 3, 4, 5]
jumlah = 0
for num in angka:
    jumlah += num  # menambahkan setiap elemen dalam list ke variabel jumlah
print(jumlah)  #output: 15

# atau bisa juga dikombinasi dengan range
angka = list(range(1, int(input("Masukkan angka ke n yg mau dijumlahkan:")) + 1)) # ditambahin 1 biar angka n nya termasuk
jumlah = 0
for num in angka:
    jumlah += num
print(jumlah)  #output: jumlah dari 1 sampai n

# 5. nested for loop
n = int(input("Masukkan tinggi bintang: "))
for i in range(n + 1): # mulai dari 0 sampai n
    for j in range(i + 1): 
        print('*', end='')  # mencetak bintang tanpa pindah baris
    print()  # pindah ke baris berikutnya setelah mencetak satu baris bintang

# 6. contoh kombinasi for loop dengan pernyataan break dan continue
for i in range(1, 10):
    if i == 5:
        continue  # melewati angka 5
    if i == 8:
        break  # keluar dari loop ketika i sama dengan 8
    print(i)  #output: 1 2 3 4 6 7 (skip 5 dan berhenti sebelum 8)