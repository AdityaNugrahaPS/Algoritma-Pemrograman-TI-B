#bab string

#multiline strings

"""
Kita bisa memakai tiga tanda petik ganda jika ingin menampilkan string
lebih dari satu baris.
"""

#contoh :

poem = """Aku ingin mencintaimu dengan sederhana
Dengan kata yang tak sempat diucapkan kayu
kepada api yang menjadikannya abu

Aku ingin mencintaimu dengan sederhana
Dengan isyarat yang tak sempat disampaikan awan
kepada hujan yang menjadikannya tiada"""

answer = input("There's a new message for you, would you like to read it? (yes/no): ")

if answer == "yes":
    print(poem)
else:
    print("Alright! maybe next time.")

#slicing strings

"""
slicing dipakai untuk mengambil sebagian string, dengan format string[start:end].
dengan index pertama dimulai dengan 0 dan index negatif dihitung dari belakang.
"""

teks = "Risol Mayo"

print(teks[0:7]) #Risol M  
print(teks[7:])  #ayo
print(teks[-6:]) #l mayo   

#modify strings

kalimat = "Aku Lucu"

print(kalimat.upper()) #menjadi huruf besar semua
print(kalimat.lower()) #menjadi huruf kecil semua
print(kalimat.replace("lucu", "baik")) #mengganti kata

#concatenate strings

"""
menggabungkan dua atau lebih string menggunakan operator '+'
dan spasi ditulis secara manual.
"""

depan = "Ayam"
belakang = "Geprek"

hasil = depan + " " + belakang
print(hasil)

#format strings

"""
menggabungkan strings dengan numbers tanpa error
"""

#contoh yang error

risol = 9
text = "Risol mayo aku ada " + age
print(text)

#contoh yang benar

risol = 9
text = f"Risol mayo aku ada {risol} "
print(text)

#escape characters

"""
jika ingin menulis karakter yang illegal distrings, kita bisa
memakai escape karakter '/'
"""

text = "Aku baru saja membeli buku berjudul "Fate" di Gramedia." #nah ini bakal error

#yang benar adalah :

text = "Aku baru saja membeli buku berjudul \"Fate\" di Gramedia."

#string methods






