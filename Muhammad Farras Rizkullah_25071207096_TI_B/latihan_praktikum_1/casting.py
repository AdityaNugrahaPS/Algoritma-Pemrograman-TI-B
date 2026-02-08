#typecasting adalah proses mengubah tipe data dari satu tipe ke tipe data lainnya   
# Type casting adalah mengubah tipe data dari sebuah variabel
umur = 22.5  # float umur
print(umur)
print(type(umur))  # untuk mengetahui tipe data dari variabel
umur = int(umur)  # mengubah float umur menjadi int umur
print(umur)
print(type(umur))  # mengetahui tipe data yang telah diubah sebelumnya

nama = "farras"  # string
print(type(nama))
nama = bool(nama)  # string nama diubah ke bool nama
print(type(nama))
print(nama)  # menghasilkan nilai True karena string nama memiliki panjang lebih atau sama dengan 1

# Jika string farras memiliki panjang 0 maka bool farras menghasilkan False
farras = ""  # string kosong
farras = bool(farras)  # string farras diubah ke bool farras
print(farras)  # menghasilkan False karena string farras memiliki panjang 0