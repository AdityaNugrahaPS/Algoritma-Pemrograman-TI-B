cars = ["Ford", "Volvo", "BMW"]

print(cars)

x = len(cars) #Menghitung banyak elemen
print(x)

y = cars[1] #Memanggil elemen indeks ke 1
print(y)

cars.append("Honda") #Menambah elemen di akhir indeks
print(cars)

cars.pop(1) #Menghapus elemen berdasarkan indeks
print(cars)

cars.remove("BMW") #Menghapus elemen berdasarkan nama elemennya
print(cars)