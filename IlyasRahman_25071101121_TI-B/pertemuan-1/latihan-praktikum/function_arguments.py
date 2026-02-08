def fungsi_saya():
    print("Ini adalah fungsi saya")

fungsi_saya()  # Memanggil fungsi saya


# aturan penamaan sama dengan variabel



# contoh penggunaan fungsi yang bermanfaat
def inci_ke_cm(a):
    return a * 2.54

hasil = inci_ke_cm(5)
print("Hasil konversi:", hasil)  # Output: Hasil konversi: 12.7

hasil = inci_ke_cm(10)
print("Hasil konversi:", hasil)  # Output: Hasil konversi: 25.4 

hasil = inci_ke_cm(15)
print("Hasil konversi:", hasil)  # Output: Hasil konversi: 38.1



# penggunaan return untuk mengembalikan nilai dari fungsi
def sapa():
    return "Halo, dari fungsi!" # mengembalikan string

pesan = sapa()
print(pesan)  # Output: Halo, dari fungsi!
print(sapa())  # Output: Halo, dari fungsi! # langsung memanggil fungsi dalam print

def tambah(a, b):
    return a + b # mengembalikan hasil penjumlahan

jumlah = tambah(3, 5)
print("Jumlah:", jumlah)  # Output: Jumlah: 8

def forbidden_function():
    return 42  # mengembalikan angka 42
result = forbidden_function()
print("apa rahasia hidup ini?", result)  # Output: apa rahasia hidup ini? 42



# fungsi tanpa isi (kosong)
def FungsiGaGuna():
    pass  # menggunakan 'pass' sama dengan contoh for loop kosong di for_loops.py



# fungsi dengan argumen
def sapa_nama(nama): # nama adalah argumen
    print(f"Halo, {nama}!")

sapa_nama("Ilyas")  # Output: Halo, Ilyas! # 'ilyas' adalah parameter
sapa_nama("Rahman")  # Output: Halo, Rahman!



# fungsi dengan argumen default
def negara(negara = 'indonesia'): # negara adalah argumen dengan default value 'indonesia'
    print(f"Saya dari {negara}")

negara()  # Output: Saya dari indonesia
negara('malaysia')  # Output: Saya dari malaysia
negara('singapura')  # Output: Saya dari singapura
negara('zimbabwe')  # Output: Saya dari zimbabwe



# make key = value
def info(nama, umur):
    print(f"Nama saya {nama} dan umur saya {umur} tahun.")

info(umur=18, nama='ilyas')  # Output: Nama saya ilyas dan umur saya 18 tahun. (keyword arguments)
info( 'nurul' , 20)  # begini bisa juga tapi harus urut sesuai posisi argumen (positional arguments)

info('ahmad', umur=22)  # kombinasi positional dan keyword arguments(positional dulu baru keyword)

# contoh keyword only dan positional only arguments
def contoh1(a, /):
    print(f"a: {a}")
# argumen a hanya bisa diisi secara positional only
contoh1(10)  # Output: a: 10
#contoh1(a=10)  # Error: a is positional only

def contoh2(*, b):
    print(f"b: {b}")
# argumen b hanya bisa diisi secara keyword only
contoh2(b=20)  # Output: b: 20
#contoh2(20)  # Error: b is keyword only

def contoh3(a, *, b, c):
    print(f"a: {a}, b: {b}, c: {c}")
# a positional only, b dan c keyword only
contoh3(1, b=2, c=3)  # Output: a: 1, b: 2, c: 3
#contoh3(a=1, b=2, c=3)  # Error: a is positional only
#contoh3(1, 2, 3)  # Error: b and c are keyword only



# variabel yang dikirim akan bersifat persistent (tidak hilang) di luar fungsi
def PencetakBuah(buah):
    for b in buah:
        print(b)

daftar_buah = ['apel', 'jeruk', 'mangga']
PencetakBuah(daftar_buah)  # Output: apel jeruk mangga (masing-masing di baris baru)

# contoh dengan dict
def cetak_dict(data):
    print("nama:", data['nama'])
    print("umur:", data['umur'])

data_saya = {'nama': 'ilyas', 'umur': 20}
cetak_dict(data_saya)  # Output: nama: ilyas umur: 20


