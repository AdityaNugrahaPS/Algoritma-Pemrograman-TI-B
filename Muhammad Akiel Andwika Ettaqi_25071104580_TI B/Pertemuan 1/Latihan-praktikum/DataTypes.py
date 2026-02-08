#Bagian ini berisi tipe tipe data yang ada di python

tipe1 = '1'                #string
tipe2 = 1                  #integer
tipe3 = 4.2                #float
tipe4 = False              #boolean
tipe5 = [1,3,4,5]          #list
tipe6 = ['Kiel', 1,3,5]    #list juga tapi beda tipe data
tipe7 = (1,2,3)            #tuple (beda list dan tuple adalah list bisa dimodifikasi setelah dibuat, tuple tidak)

tipe8 = {                  #dictionary
    'Nama': 'Kiel',
    'NIM': '25071104580',
    'Kelas': 'ITB',
}

#Untuk mengetahui tipe apa sebuah variabel itu, kita bisa memakai print(type(Variabel))
print (type(tipe1))
print (type(tipe2))
print (type(tipe3))
print (type(tipe4))
print (type(tipe5))
print (type(tipe6))
print (type(tipe7))
print (type(tipe8))

#Contoh output yang dikeluarkan
print (tipe1)
print (tipe2)
print (tipe3)
print (tipe4)
print (tipe5[0])
print (tipe5[1])
print (tipe5[2])
print (tipe5[3])
print (tipe6[0])
print (tipe6[1])
print (tipe6[2])
print (tipe6[3])
print (tipe7)
print (tipe8['Kelas'])
print (tipe8['Nama'])
print (tipe8['NIM'])