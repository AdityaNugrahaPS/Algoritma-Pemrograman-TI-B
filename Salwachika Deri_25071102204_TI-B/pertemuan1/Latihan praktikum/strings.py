'''
String adalah tipe data untuk menyimpan teks di Python.
'''

#menggunakan petik satu ataupun petik dua
print("bracelets")
print('bracelets')
#bisa memakai petik didalam petik asal berbeda dengan petik lainnya
print('nama panggilanku "salwa"')

#slicing
#cara mengambil sebagian karakter dari string berdasarkan posisi (index).
s = 'love you!'
print(s[:3])    #mengambil indeks awal sampai 3
print(s[2:5])   #mengambil indeks 2 sampai 5    
print(s[5:])    #mengambil indek 5 sampai indeks terakhir

#modify string
    #upper case
a = "Hello, World!" #mengubah semua huruf menjadi kapital
print(a.upper())    
    #lower case
a = "Hello, World!"
print(a.lower())    #mengubah semua huruf menjadi huruf kecil
    #remove whitespace
a = " Hello, World! "
print(a.strip())    #menghapus spasi diawal dan di akhir string
    #replace string
a = "Hello, World!"
print(a.replace("H", "J"))  #mengganti bagian string dengan string lain (h diganti j)

#string concatenation/combine
#menggunakan operator +
a = "Hello"
b = "salwa"
c = a + b
print(c)

#format string
nama = 'salwachika'          
print("hello nama saya " + nama)        #2 : menggabungkan teks menggunakan tanda (+) 
print(f'hello nama saya {nama}')        #3 : f-string 
print("hello nama saya", nama)          #4 : menggunakan koma yang akan memberi spasi

#escape character
#Escape character adalah karakter khusus yang digunakan untuk memasukkan karakter yang tidak bisa ditulis langsung ke dalam string.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)      #Gunakan \\" untuk memasukkan tanda kutip di dalam string.
'''
Code	Result	
\'	    Single Quote	
\\	    Backslash	
\n	    New Line	
\r	    Carriage Return	
\t	    Tab	
\b	    Backspace	
\f	    Form Feed	
\ooo	Octal value	
\xhh	Hex value	
'''

