#fungsi
def sapa_mahasiswa(nama):
    # Kode di bawah ini akan menggunakan data dari argumen 'nama'
    print(f"Halo {nama}, selamat mengerjakan tugas praktikum!")

# Cara memanggil fungsi dengan mengisi argumen string
sapa_mahasiswa("farel") 
sapa_mahasiswa("ilyas")

#2. Fungsi dengan Nilai 
# Jika saat dipanggil kita tidak mengisi argumen, maka otomatis menggunakan "Python"
def belajar_apa(bahasa = "Python"):
    print(f"Saya sedang belajar bahasa pemrograman {bahasa}")

# Memanggil dengan argumen baru
belajar_apa("C") 

# Memanggil tanpa argumen (maka akan muncul "Python")
belajar_apa()