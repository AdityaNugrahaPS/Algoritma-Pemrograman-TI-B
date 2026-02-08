# Penamaan variabel
## Legal
var = "x"
VaR = "x"
_var = "x"
var0 = "x"
VAR = "x"

## Tidak legal
0var = "x"
var i = "x"
var-i = "x"

# membuat variabel
a = 10
b = 'Palembang'
print(a)
print(b)

c = int(5)
d = float(2)  
print(c, d)

# Membuat lebih dari satu variabel / Multiple variables
## Banyak nilai sekaligus
x, y, z = 12, 15, 31
print(x, y, z)

## Satu nilai untuk beberapa variabel
x = y = z = "Apel"
print(x, y, z)


## Output variables
x = "Satu, "
y = "dua, "
z = "tiga."
print(x, y, z) # Mencetak beberapa variabel sekaligus menggunakan koma)
print(x + y + z) # Mencetak beberapa variabel sekaligus juga dapat menggunakan tanda tambah)
x = 4
print(x + y) # Akan tetapi, menggabungkan string dengan nomor akan menghasilkan error.

## Global variables
x = "merah"
def func():
    x = "biru"
    print("Balonku berwarna" + x)
func()
print("Balonku berwarna" + x)