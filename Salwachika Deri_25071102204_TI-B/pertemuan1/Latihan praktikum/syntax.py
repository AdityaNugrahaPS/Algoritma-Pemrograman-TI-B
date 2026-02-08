''''
deskripsi materi : 
phyton syntax merupakan seluruh aturan tata bahasa python. 
hal yang harus diperhatikan didalam syntax antaranya :
-spasi
-titik dua yang dipakai setelah if, for, while,def
-huruf besar dan huruf kecil
-string bisa menggunakan petik dua dan petik satu
sedangkan statements adalah bagian yang terdapat dalam syntax phyton. phyton statements merupakan satu baris perintah yang dijalan python. setiap statements menyuruh program melakukan sesuatu. 
'''

#format penulisan teks pada syntax phyton
print('hello world')                    #1 : string langsung yang bisa menggunakan petik dua(") atau petik satu(')

nama = 'salwachika'
                  
print("hello nama saya " + nama)        #2 : menggabungkan teks menggunakan tanda (+) 
print(f'hello nama saya {nama}')        #3 : f-string 
print("hello nama saya", nama)          #4 : menggunakan koma yang akan memberi spasi
 

#statements
print("selamat pagi semuanya!")                 #many statements 
print("apakabar kalian semua?")
print("saya senang bertemu dengan kalian")

namalengkap = 'salwachika deri'             #{pemberian nilai dengan menyimpan data ke variabel
panggilan = 'salwa'                         #{pemberian nilai dengan menyimpan data ke variabel
tempatlahir = 'taluk kuantan'               #{pemberian nilai dengan menyimpan data ke variabel
tanggallahir = '7 agustus 2006'             #{pemberian nilai dengan menyimpan data ke variabel

print(f'nama saya {namalengkap}')
print(f'saya biasa dipanggil {panggilan}')
print(f'saya lahir di {tempatlahir}')
print(f'pada tanggal {tanggallahir}')