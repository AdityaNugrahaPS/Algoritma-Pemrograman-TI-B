#Bagian ini akan membahas cara membuat dan memanggil fungsi (seperti fungsi di c)

def contoh(): #Untuk membuat fungsi, harus menggunakan def 
    print("ini contoh fungsi")

contoh() #Kita memanggil fungsi disini

#Kita juga bisa membuat fungsi dengan argumen
def sapaNama(nama2):
    print("haiii" + " " + nama2)

sapaNama('Akiel')
sapaNama('Ilyas')
sapaNama('Dihar')

#Kita juga bisa membuat fungsi dengan return value

def kaliLima(x):
    return 5 * x

print (kaliLima(5))
