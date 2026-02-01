tipe1 = '24'
tipe2 = 67
tipe3 = 3.14
tipe4 = False
tipe5 = [2,0,1,6]
tipe6 = ['Me',2,1]
tipe7 = (1.3,3,False,7)
tipe8 = {
    'name': 'Shoyo',
    'kelas':'TI-B',
    'NIM': '25071104120',
    'Mahasiswa aktif': True,
}

print(type(tipe1)) #bisa mendapatkan tipe data sebuah variabel menggunanakan "type(namaVariabel)"
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6[0])) # jika variabel sebuah tipe sequence kita harus deklarasikan nomor indeks yang ingin di check
print(type(tipe7[0]))
print(type(tipe8['kelas'])) # jika sebuah dictionary kita harus menulis nama variabel dalam dictionarynya
