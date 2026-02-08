tipe1 = '1' # string
tipe2 = 1 # integer
tipe3 = 1.5 # float
tipe4 = True # boolean
tipe5 = [1,3,4,5] # list
tipe6 = ['ilyas', 2,3] # list
tipe7 = (1,2,3) # tuple
tipe8 = {
    'nama' : 'ilyas',
    'kelas': 'TI-B',
    'NIM': 25071101121,
    'Mahasiswa Aktif' : True,
} # dict

print(type(tipe1)) 
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))

print(tipe7[2]) # mengakses elemen ke-2 dari tuple

print(tipe8['kelas']) # mengakses nilai dari dict dengan key 'kelas'

tipe5.append(6) # menambahkan elemen ke ujung list
print(tipe5) # hasilnya [1, 3, 4, 5, 6]
