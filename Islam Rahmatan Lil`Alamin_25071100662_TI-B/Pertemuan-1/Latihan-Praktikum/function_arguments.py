# Fungsi di python dengan argumen
# Argumen adalah nilai yang kita berikan ke fungsi saat memanggilnya

# 1. Fungsi dengan argumen posisi
def sapa(nama):
    print(f"Halo, {nama}!")

# 2. Fungsi dengan beberapa argumen posisi
def tambah(a, b):
    return a + b

# 3. Fungsi dengan argumen default
def sapaSopan(nama, greeting="Halo"):
    print(f"{greeting}, {nama}!")

# 4. Fungsi dengan argumen kata kunci
def infoMahasiswa(nama, umur, jurusan):
    print(f"Nama: {nama}, Umur: {umur}, Jurusan: {jurusan}")

# 5. Contoh klo pake operasi matematika
def hitungLuasPersegiPanjang(panjang, lebar):
    return panjang * lebar


## contoh fungsi loading bar yg ada di linux
import time

def loadingBar(namaProses, bnykProses = 20): # bnykProses itu defaultnya 20, tapi bisa diubah pas manggil fungsi
    print(f"Mulai {namaProses}")

    for i in range(bnykProses + 1):
        isi = "█" * i
        kosong = "-" * (bnykProses - i)
        persen = (i/bnykProses) * 100

        print(f"\rProcess: [{isi}{kosong}] {persen:.0f}%", end = "")
        time.sleep(0.1)
    print(" Selesai!")


if __name__ == "__main__": # Biar bisa di import ke file lain tanpa ngejalanin ini
    # 1. Manggil fungsi dengan argumen posisi
    sapa("Alam")  #output: Halo, Alam!
    sapa("Ganteng")  #output: Halo, Ganteng!

    # 2. Manggil fungsi dengan beberapa argumen posisi
    print(tambah(5, 3))  #output: 8
    print(tambah(10, 20))  #output: 30

    # 3. Manggil fungsi dengan argumen default
    sapaSopan("Alam")  #output: Halo, Alam!
    sapaSopan("Islam", "Ohayou")  #output: Ohayou, Islam
    # jadi jika argumennya gak diisi, dia bakal pake nilai defaultnya

    # 4. Manggil fungsi dengan argumen kata kunci
    infoMahasiswa(nama="Alam", umur=18, jurusan="Informatika")  #output: Nama: Alam, Umur: 18, Jurusan: Informatika
    infoMahasiswa(jurusan="TI", nama="Islam", umur=19)  #output: Nama: Islam, Umur: 19, Jurusan: TI
    # jadi kita bisa ngasih argumen sesuai nama parameternya, gak perlu sesuai urutan
    
    # 5. Manggil fungsi yg pake operasi matematika
    print(hitungLuasPersegiPanjang(5, 3))  #output: 15
    print(hitungLuasPersegiPanjang(lebar=4, panjang=6))  #output: 24
    # kita bisa pake argumen posisi atau argumen kata kunci

    # Test Loading Bar
    loadingBar("installing fastfetch")
    loadingBar("installing vscode", 40)




