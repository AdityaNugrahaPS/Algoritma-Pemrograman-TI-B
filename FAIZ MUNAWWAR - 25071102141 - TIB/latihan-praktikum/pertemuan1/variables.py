# Variabel harus di Deklarasi sendiri
x = 5
y = "John"
print(x)
print(y)

# Di Python type dapat berubah tanpa harus di deklarasi kembali
x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

# Bisa Menentukan tipe data sendiri dengan melakukan casting
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

#Legal Variable
hotel_mewah = 1
HotelMewah = 3

#Illegal Variable
# hotel-Mewah = 2
# hotel mewah = 4

# Bisa mendeklarasikan Variable sekaligus dalam satu garis
x, y, z = "Faiz", "Rio", "Ubay"
print(x)
print(y)
print(z)

# Bisa juga mendeklariskan banyak Variable dalam satu nilai
x = y = z = "Manusia"
print(x)
print(y)
print(z)

# Bisa menggunakan List untuk mengumpulkan nilai menjadi satu
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Bisa mengprint sekaligus dalam satu baris dengan menggunakan koma
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Bisa juga dengan + tetapi tidak ada spasi nya, karena + lebih sering di pake untuk number
print(x + y + z)

x = 5 
y = 10     # Contoh Number
print(x + y)

# Text dan number tidak dapet di gabung dengan +, karena akan menyebabkan error
x = 5
y = "John"
# print(x + y)
# Tetapi dapat di gabung dengan menggunakan koma
print(x, y)

# ********* FUNCTION ********* #

x = "Ganteng"
def fungsi():    #Bisa Memanggil sebuah variabel di luar fungsi
  print("Lanang itu " + x)
fungsi()

y = "awesome"
def fungsi():
  y = "fantastic"   #Bisa membuat nama sebuah variabel yang sama di dalam fungsi, dan di luar fungsi
  print("Python is " + y)

fungsi()

print("Python is " + y)



