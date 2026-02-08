# Function 
print("-Function")
def abbk():
    print("Halo!") # Tereksekusi bila dipanggil

abbk()

# Return
def wqwq():
    return "Selamat pagi!"

pesan = wqwq()
print(pesan)

## Return langsung
print(wqwq())
print()

# Arguments
print("-Argumen-")
## ! argument
def namo(nama):
    print(nama, "disini.")

namo("Ian") 
print()

# Keyword arguments
print("-Keyword arguments:")
def nam(nama, negara):
    print(f"Saya {nama} dan saya tinggal di {negara}.")

nam(nama = "Oliwia", negara = "Polandia")

## Posisional
nam("Akosi", "Nigeria")

# Tipe data yang berbeda
nama_orang = " "
nim = " "
def biodata(orang):
    print("Nama: ", orang["nama"])
    print("NIM: ", orang["nim"])

orang_1 = {"nama": "Ray", "nim": 250710000}
biodata(orang_1)
print()

# Return
## Return nilai
def func(a, b):
    return a + b

hasil = func(2, 1)
print(hasil)

## Return tipe data yang berbeda
def func():
    return ["Jakarta", "Palembang", "Surbaya"]

kota = func()
print(kota[0])
print(kota[1])
print(kota[2])

## Return tuple
def func():
    return(3, 7)

x, y = func()
print("Angka pertama: ", x)
print("Angka kedua: ", y)

# Positional-only arguments
def func(n):
    print("Saya berada di", n)

func(n  = "Jawa")

# Keyword-only arguments
def func(*, nama):
    print("Halo,", nama)

func(nama = "Arif")

# Combining positional-only and keyword-only
def fun(a, b, /, *, c, d):
    return a + b + c + d

result = fun(2, 4, c = 6, d = 8)
print(result)
