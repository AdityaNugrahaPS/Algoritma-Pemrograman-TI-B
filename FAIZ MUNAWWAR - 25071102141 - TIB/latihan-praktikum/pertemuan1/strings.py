print("Hello") # Yang didalam kurung itulah string
print('Hello')

print("Nama Saya 'Faiz'") # Tetap bisa menggunakan kutip, dengan syarat tidak boleh dengan tanda kutip yang sama
print('Nama Saya "Faiz"')

# Menetapkan String Ke Variabel
a = "Hello"
print(a)

# Dengan tiga tanda kutip dapat menetapkan multibaris
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# Perulangan dengan string
for x in "Manusia":
  print(x)

# Untuk menghitung panjang sebuah string
a = "Hello, World!"
print(len(a))

# Untuk memeriksa apakah ada sebuah teks dengan menggunakan in
text = "Kamu Sangat Keren!!"
print("Keren" in text)

# Untuk memeriksa apakah tidak ada sebuah teks bisa dengan menggunakan not in
text = "The best things in life are free!"
print("expensive" not in text)

b = "Hello, World!" 
print(b[2:5])       #Untuk mengambil karakter dari posisi 2 sampai 5

# **** Modifikasi String ***** #

a = "Hello, World!"
print(a.upper())  # String akan menjadi huruf besar

a = "Hello, World!"
print(a.lower()) # String akan menjadi huruf kecil

a = " Hello, World! "
print(a.strip()) # Menghapus space kosong

a = "Hello, World!"
print(a.replace("H", "T")) # Mengubah dari H menjadi T

a = "Hello, World!"
print(a.split(",")) # Membuat pemisah dengan string yang di tentukan

# **** Menggabungkan String **** #

a = "Hello"
b = "World"
c = a + b
print(c)
c = a + " " + b # Untuk Menambahkan Space
print(c)

age = 36
# txt = "My name is John, I am " + age # Seperti yang kita tau bahwa number dan text tidak dapat di gabung maka.
# print(txt)
txt = f"My name is John, I am {age}" # Untuk mengabungkannya bisa menggunakan f-string, f di depan string dan tambahkan kurung kurawal
print(txt)

price = 59
txt = f"The price is {price} dollars" # Placeholder dapat berisi variabel,numbers,operasi,fungsi dan pengubah nilai
print(txt)

price = 59
txt = f"The price is {price:.2f} dollars" # Dengan bilangan desimal (float)
print(txt)

txt = "We are the so-called "Vikings" from the north." # Seperti yang kita tau tidak bisa di menggunakan double qoutes secara bersamaan maka.
print(txt)

txt = "We are the so-called \"Vikings\" from the north." # Bisa menambahkan garis miring "/"
print(txt)