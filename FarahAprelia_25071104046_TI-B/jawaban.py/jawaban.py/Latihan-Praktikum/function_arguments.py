#FUNCTION ARGUMENTS (Argumen ditentukan setelah nama fungsi, di dalam tanda kurung. )

def func(fname): #Definisi fungsi bernama func dengan satu parameter, yaitu fname
  print(fname + " Refsnes") #Mencetak nilai fname yang kemudian digabungkan dengan string Refsnes

func("Emil") #Pemanggilan fungsi serta argumen yang terdapat di dalamnya
func("Tobias") #Pemanggilan fungsi serta argumen yang terdapat di dalamnya
func("Linus") #Pemanggilan fungsi serta argumen yang terdapat di dalamnya

def func(fname, lname): #Definisi fungsi dengan dua parameter, yaitu fname dan lname
  print(fname + " " + lname) #Mencetak fname, 'spasi' dan lname

func("Emil", "Refsnes") #Pemanggilan fungsi dan kedua argumen, yaitu Emil dan Refsnes

def func(x, y): #Definisi fungsi dengan dua parameter, yaitu x dan y
  return x + y #Mengembalikan hasil penjumlahan x + y

result = func(5, 3) #Pemanggilan fungsi serta memasukkan value ke dalam variabel result
print(result) #Mencetak result