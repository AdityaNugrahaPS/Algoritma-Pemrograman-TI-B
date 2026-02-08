#functions

#python functions - digunakan untuk mengelompokkan kode agar bisa dipakai ulang
def sapa():
    print("nihao")

#python arguments - nilai yang dikirim ke fungsi
def sapa(nama):
    print("Halo", nama)

sapa("Arin")

#python args dan kwargs - digunakan untuk jumlah argumen yang tidak pasti
def jumlah(*angka):
    print(sum(angka))

jumlah(1, 2, 3)

#python scope - menentukan di mana variabel bisa diakses
x = 10

def tampil():
    print(x)

tampil()

#python decorators - fungsi yang memodifikasi fungsi lain
def dekorator(func):
    def pembungkus():
        print("Mulai")
        func()
    return pembungkus

@dekorator
def halo():
    print("Halo")

halo()

#python lambda - fungsi kecil stu baris
kali = lambda a, b: a * b
print(kali(2, 3))

#python recursion - fungsi yang memnaggil dirina sendiri
def hitung(n):
    if n == 0:
        return 0
    return n + hitung(n - 1)

print(hitung(3))

#python generators - fungsi yang menghasilkan nilai satu oersatu
def hitung(n):
    if n == 0:
        return 0
    return n + hitung(n - 1)

print(hitung(3))


