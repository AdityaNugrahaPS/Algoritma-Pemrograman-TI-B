"""
Python strings
"""

# 1. Membuat string
print("1. Membuat string:")
string1 = "Ini adalah string dengan tanda kutip ganda"
string2 = 'Ini adalah string dengan tanda kutip tunggal'
string3 = '''Ini adalah string
dengan beberapa baris'''
print(string1)
print(string2)
print(string3)

# 2. Mengakses karakter dalam string
print("\n2. Mengakses karakter dalam string:")
nama = "Python"
print(f"String: {nama}")
print(f"Karakter pertama: {nama[0]}")
print(f"Karakter terakhir: {nama[-1]}")
print(f"Karakter dari indeks 1-3: {nama[1:4]}")

# 3. Panjang string
print("\n3. Panjang string:")
kata = "Program"
print(f"Panjang dari '{kata}': {len(kata)}")

# 4. Penggabungan string
print("\n4. Penggabungan string:")
kata1 = "Halo"
kata2 = "Dunia"
gabungan = kata1 + " " + kata2
print(f"Gabungan: {gabungan}")

# 5. Perulangan dalam string
print("\n5. Perulangan dalam string:")
for huruf in "ABC":
    print(f"Huruf: {huruf}")

# 6. Memeriksa keberadaan substring
print("\n6. Memeriksa keberadaan substring:")
kalimat = "Saya sedang belajar Python"
print(f"'belajar' dalam kalimat: {'belajar' in kalimat}")
print(f"'Java' dalam kalimat: {'Java' in kalimat}")

# 7. Metode string - upper() dan lower()
print("\n7. Metode string - upper() dan lower():")
teks = "Halo Dunia"
print(f"Asli: {teks}")
print(f"Upper: {teks.upper()}")
print(f"Lower: {teks.lower()}")

# 8. Metode string - strip()
print("\n8. Metode string - strip():")
teks_spasi = "  Halo Dunia  "
print(f"Asli: '{teks_spasi}'")
print(f"Setelah strip(): '{teks_spasi.strip()}'")

# 9. Metode string - replace()
print("\n9. Metode string - replace():")
teks_lama = "Saya suka mangga"
teks_baru = teks_lama.replace("mangga", "apel")
print(f"Asli: {teks_lama}")
print(f"Setelah replace: {teks_baru}")

# 10. Metode string - split()
print("\n10. Metode string - split():")
kalimat = "satu-dua-tiga"
bagian = kalimat.split("-")
print(f"Asli: {kalimat}")
print(f"Setelah split: {bagian}")

# 11. Format string
print("\n11. Format string:")
nama = "Abdullah"
umur = 19
pesan = "Nama saya {}, umur saya {}".format(nama, umur)
print(pesan)

# 12. F-string (format string literal)
print("\n12. F-string:")
pesan_f = f"Nama saya {nama}, umur saya {umur} tahun"
print(pesan_f)

# 13. Escape characters
print("\n13. Karakter escape:")
teks_escape = "Dia berkata, \"Python itu menyenangkan!\""
print(teks_escape)

# 14. String raw
print("\n14. String raw:")
path = r"C:\nama\folder\file.txt"
print(path)

# 15. String capitalize, title, swapcase
print("\n15. Metode capitalize, title, swapcase:")
judul = "ini adalah judul artikel"
print(f"Asli: {judul}")
print(f"Capitalize: {judul.capitalize()}")
print(f"Title: {judul.title()}")
print(f"Swapcase: {judul.swapcase()}")

# 16. Pengecekan tipe karakter
print("\n16. Pengecekan tipe karakter:")
angka = "12345"
alfabet = "abcd"
alnum = "abc123"
print(f"'{angka}'.isdigit(): {angka.isdigit()}")
print(f"'{alfabet}'.isalpha(): {alfabet.isalpha()}")
print(f"'{alnum}'.isalnum(): {alnum.isalnum()}")
print(f"'{judul}'.istitle(): {judul.istitle()}")

# 17. Pencarian dalam string
print("\n17. Pencarian dalam string:")
kalimat_panjang = "Python adalah bahasa pemrograman yang populer"
posisi = kalimat_panjang.find("bahasa")
print(f"Posisi 'bahasa' dalam kalimat: {posisi}")
print(f"Apakah dimulai dengan 'Python': {kalimat_panjang.startswith('Python')}")
print(f"Apakah diakhiri dengan 'populer': {kalimat_panjang.endswith('populer')}")

# 18. Mengganti beberapa karakter sekaligus
print("\n18. Mengganti beberapa karakter sekaligus:")
asli = "Halo Dunia!"
baru = asli.replace("Halo", "Hai").replace("!", "?")
print(f"Asli: {asli}")
print(f"Baru: {baru}")