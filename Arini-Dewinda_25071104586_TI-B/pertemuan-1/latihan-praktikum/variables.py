#bab variabel

"""
variabel dalam bahasa pemrograman digunakan untuk
menyimpan nilai ke dalam memori komputer.
"""

#nama variabel : harus jelas, gapakai spasi dan ga diawali angka

nama = "arin" #ini benar/legal
nama belakang = "dewinda" #ini salah/illegal karena ada spasinya

#Assign multiple values
penyanyi, judul, genre = "mcr", "helena", "rock alternatif"
print(penyanyi)
print(judul)
print(genre)

#output variabel

"""
pada python kan kita bisa nampilin output variabel pakai 'print()'
nah, kalau mau print banyak sekaligus bisa dipisah pakai koma saja.
"""

kata1 = "robloks"
kata2 = "gem"
kata3 = "terbaik"

print(kata1, kata2, kata3)

#global variabel

"""
global variabel itu dibuat diluar fungsi, nah tapi
bisa dipakai di dalam ataupu luar fungsi karena dia
"""

kondisi = "galau"  # variabel global

def cek_kondisi():
    # Mengakses variabel global
    print("Status sekarang:", kondisi)

cek_kondisi()

#