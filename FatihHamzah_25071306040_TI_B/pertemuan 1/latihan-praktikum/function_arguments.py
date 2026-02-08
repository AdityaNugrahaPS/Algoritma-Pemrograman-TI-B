def contoh(): #Untuk membuat fungsi, harus menggunakan def 
    print("ini contoh fungsi")

contoh() #Kita memanggil fungsi disini

#Kita juga bisa membuat fungsi dengan argumen
def sapaNama(nama2):
    print("haiii" + " " + nama2)

sapaNama('hamzah')
sapaNama('faris')
sapaNama('hakim')

#Kita juga bisa membuat fungsi dengan return value

def kaliLima(x):
    return 5 * x

print (kaliLima(5))