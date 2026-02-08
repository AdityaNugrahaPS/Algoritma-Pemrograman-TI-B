#sub-bab 'print text'

print("Perkenalkan nama saya Dafa Islamy")

#double quotes
print("Perkenalkan nam saya Dafa Islamy") #menggunakan petik dua
print('Perkenalkan nama saya Dafa Islamy') #menggunakan petik satu


nama1 = "Dafa"
nama2 = 'Islamy'

#version 1
print("halo nama saya " + nama1, "dan teman saya " + nama2)
#version 2
print(f'halo nama saya {nama1} dan teman saya {nama2}')
#version 3
print('halo nama saya', nama1, 'dan teman saya', nama2)

#print without newline
print("Saya suka Pemrograman dan", end= " ")
print("saya suka Matematika")


#sub-bab 'print numbers'
print(6) #print angka tidak perlu menggunakan tanda petik
print(16)
print(600)
print(25 - 9) #juga dapat melakukan operasi aritmetika

#print mix text and numbers
print('Umur saya', 18, 'tahun') #print dapat menggabungkan teks dan angka