#Bagian ini berisi cara mengubah satu tipe data menjadi tipe data yang lain

string = '1'
string_to_numbers = int(string) #biar kebaca kalau string itu jadi int

print(type(string_to_numbers)) #cek tipenya apa (sudah berubah menjadi int)
print(type(string))            #tipe datanya sebelum diubah masih str

#Contoh lain  

int = 1
int_to_float = float(int)

print(int_to_float)
print(int)
print(type(int_to_float))
print(type(int))
