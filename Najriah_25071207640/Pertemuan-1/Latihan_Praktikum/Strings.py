#1. Python Strings
'''
String dalam python dikelilingi oleh tanda kutip tunggal, atau tanda kutip ganda.

"Halo" sama dengan 'Halo'.
'''

print("Halo")
print('Halo')

''' 
Kedua perintah diatas akan menghasilkan keluaran yang sama, yaitu 'Halo'.
'''

'''
Tanda kutip bisa digunakan di dalam String, selama tidak cocok dengan tanda 
kutip yang mengelilingi string.
'''

print("--Quotes Inside Quotes--") #Menampilkan header
print("It's Ok")
print('Her name is "Mei"') 
print("Her name is 'Mei'") #Tanda kutip yang digunakan harus berbeda antara Strings utama dengan kutipan di dalam String

'''
Menetapkan string ke variabel dilakukan dengan nama variabel diikuti dengan tanda sama dengan dan string
'''

a = "Matthias"

print("\n--Assign String to a Variable--") #Menampilkan Header
print(a)

'''
Bisa membuat string dengan beberapa baris dengan menggunakan tiga tanda kutip
'''

b = """Do you think I have forgotten?
Do you think I have forgotten?
Do you think I have forgotten, about You?"""

print("\n--Multiline Strings--") #Menampilkan Header
print(b)

c = '''And there was something about you that now I can't remember
It's the same damn thing that made my heart surrender
And I'll miss you on a train, I'll miss you in the mornin'
I never know what to think about
I think about you
About you
''' #Multiline String menggunakan tanda petik satu (')

print(c)

'''
String dalam Python adalah susunan karakter unicode. Namun, Python tidak memiliki tipe 
data karakter, satu karakter hanyalah string dengan panjang 1. 
Tanda kurung siku dapat digunakan untuk mengakses elemen string.
'''

d = "Hi guys"

print("\n--Strings are Arrays--") #Menampilkan header
print(d[1])

'''
Karena string adalah array, kita dapat mengulang karakter dalam string dengan for loop.
'''

print("\n--Looping Through a String--") #Menampilkan header
for a in "Matthias" : #Ulangi huruf dalam kata "Matthias"
    print(a)

'''
Untuk mengetahui panjang string, gunakan fungsi len()'
'''

a = "Matthias"
print("\n--String Length--")
print(len(a))

'''
Untuk memeriksa apakah frasa atau karakter tertentu ada dalam string, 
kita dapat menggunakan kata kunci in.'''

d = "Hi guys"

print("\n--Check String--") #Menampilkan header
print("Hi" in d) #Menghasilkan nilai True or False

#Penggunaan in di dalam if
d = "Hi guys"
if "Hi" in d :
    print("Bye leadis")

'''
Untuk memeriksa apakah frasa atau karakter tertentu tidak ada dalam string, 
kita dapat menggunakan kata kunci not in.
'''

d = "Hi guys"

print("\n--Check if NOT--") #Menampilkan header
print("leadis" not in d) #Menghasilkan nilai True or False

#Penggunaan not in di dalam if
d = "Hi guys"
if "leadis" not in d :
    print("Hello")

#2. Slicing Strings

#Menampilkan karakter dari posisi 2, dan sampai akhir
a = "Matthias"

print("\n--Slicing Strings--") #Menampilkan header
print(a[2:])

'''
Gunakan indeks negatif untuk memulai dari akhir string
'''
a = "Matthias"
print(a[-1])

#3. Modify Strings
'''
Upper Case
'''

a =  "Matthias"

print("\n--Upper Case--") #Menampilkan header
print(a.upper())

'''
Lower Case
'''

a = "MATTHIAS"

print("\n--Lower Case--") #Menampilkan header
print(a.lower())

'''
Remove Whitespace
'''
d = " Hi guys "

print("\n--Remove Whitespace--") #Menampilkan header
print(d.strip()) #Menghasilkan 'Hi guys'

'''
Replace Strings
'''

d = "Hi guys"

print("\n--Replace Strings--") #Menampilkan header
print(d.replace("H", "B")) #Mengganti hurus H menjadi B

'''
Split Strings
'''

d = "Hi guys"

print("\n--Replace Strings--") #Menampilkan header
print(d.split(","))

#4. String Concatenation
'''
Untuk menggabungkan dua string, bisa menggunakan operator +
'''

a = "Hi"
b = " guys"
c = a + b

print("\n--String Concatenation--")
print(c)

#5. String Format
'''
Pada Python tidak dapat menggabungkan string dan angka.
Tetapi kita dapat menggabungkan string dan angka dengan menggunakan f-string
'''

a = 3000
ab = f"I love You {a}"

print("\n--F-Strings--") #Menampilkan header
print(ab)

'''
Placeholders and Modifiers
'''

price = 300
ab = f"The price is {price} IDR" #Placeholder dapat berisi variabel, operasi, fungsi, dan pengubah untuk memformat nilai

print("\n--Placeholders and Modifiers--") #Menampilkan header
print(ab) 

'''
Placeholder dapat menyertakan pengubah untuk memformat nilai.
'''

price = 300
ab = f"The price is {price:.2f} IDR" #Menampilkan harga dengan dua desimal

print(ab)

'''
Placeholder bisa mengandung operasi Matematika
'''

ab = f"The price is {300 * 30} IDR"
print(ab)

#6. Escape Character
'''
Untuk menyisipkan karakter yang ilegal dalam string, gunakan karakter escape.
Karakter escape adalah garis miring terbalik (\) yang diikuti oleh karakter yang ingin Anda sisipkan.
Contoh karakter ilegal adalah tanda kutip ganda di dalam string yang dikelilingi oleh tanda kutip ganda
'''

txt = "She's so perfect, her name is \"Giselle\", I love her so much"

print("\n--Escape Character--")
print(txt)