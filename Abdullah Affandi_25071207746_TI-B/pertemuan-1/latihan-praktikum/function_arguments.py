"""
Python function arguments
"""

# 1. Fungsi dengan argumen posisional
def sapa(nama):
    """Fungsi dengan satu argumen posisional"""
    return f"Halo, {nama}!"

# 2. Fungsi dengan beberapa argumen posisional
def tambah(a, b):
    """Fungsi dengan dua argumen posisional"""
    return a + b

# 3. Fungsi dengan argumen default
"""
Dianggap default karena nilai pada parameternya telah di-assign
jadi, boleh dokosongin ketika mau manggil fungsi tersebut
"""
def sapa_default(nama="Tamu", pesan="Selamat datang"):
    """Fungsi dengan argumen default"""
    return f"{pesan}, {nama}!"

# 4. Fungsi dengan argumen arbitrer (*args)
"""
Argumen fleksibel
"""
def jumlah_semua(*angka):
    """Fungsi dengan argumen arbitrer (posisional)"""
    total = 0
    for a in angka:
        total += a
    return total

# 5. Fungsi dengan argumen kata kunci arbitrer (**kwargs)
"""
Argumen fleksibel dengan key-value
"""
def cetak_info(**info):
    """Fungsi dengan argumen kata kunci arbitrer"""
    for kunci, nilai in info.items():
        print(f"{kunci}: {nilai}")

# 6. Fungsi dengan kombinasi argumen posisional dan default
"""
sama kayak contoh nomor 3, 4, 5. ini cuma dimodif tipis-tipis
"""
def biodata(nama, usia, kota="Jakarta"):
    """Fungsi dengan argumen posisional dan default"""
    return f"Nama: {nama}, Usia: {usia}, Kota: {kota}"

# 7. Fungsi dengan kombinasi semua jenis argumen
"""
sama kayak contoh nomor 3, 4, 5, 6. ini cuma dimodif tipis-tipis
"""
def fungsi_lengkap(wajib, opsional="nilai_default", *args, **kwargs):
    """Fungsi dengan kombinasi semua jenis argumen"""
    print(f"Argumen wajib: {wajib}")
    print(f"Argumen opsional: {opsional}")
    print(f"Args: {args}")
    print(f"Kwargs: {kwargs}")

# 8. Fungsi dengan argumen kata kunci saja (keyword-only)
"""
keyword only setelah asterisk
"""
def fungsi_keyword_only(*, nama, usia):
    """Fungsi hanya menerima argumen sebagai kata kunci"""
    return f"Nama: {nama}, Usia: {usia}"

# 9. Fungsi dengan argumen posisional
def fungsi_posisional_only(posisi, /, opsional):
    """Fungsi dengan argumen posisional saja di bagian pertama"""
    return f"Posisional: {posisi}, Opsional: {opsional}"

# 10. Fungsi dengan argumen campuran posisional dan kata kunci
def fungsi_campuran(a, b, /, c, d, *, e, f):
    """Fungsi dengan argumen posisional, campuran, dan kata kunci saja"""
    return f"a={a}, b={b}, c={c}, d={d}, e={e}, f={f}"

# 11. Fungsi dengan unpacking argumen
def fungsi_unpack(a, b, c):
    """Fungsi untuk menunjukkan unpacking argumen"""
    return a + b + c

"""
* artinya memisahkan tanpa key
** artinya memisahkan dengan key-value (kv)
"""
list_angka = [1, 2, 3]
print(fungsi_unpack(*list_angka))  # Unpacking list

dict_angka = {'a': 1, 'b': 2, 'c': 3}
print(fungsi_unpack(**dict_angka))  # Unpacking dictionary

# 12. Fungsi rekursif dengan argumen
"""
fungsi ini memanggil diri sendiri
"""
def faktorial(n):
    """Fungsi rekursif untuk menghitung faktorial"""
    if n == 0 or n == 1:
        return 1
    else:
        return n * faktorial(n - 1)

# 13. Fungsi lambda dengan argumen
"""
fungsi anonim
"""
kuadrat = lambda x: x ** 2
penjumlahan = lambda x, y: x + y

# 14. Fungsi dengan tipe data argumen (type hints)
"""
type check, return type str
"""
def fungsi_dengan_tipe(nama: str, usia: int, tinggi: float) -> str:
    """Fungsi dengan type hints"""
    return f"Nama: {nama}, Usia: {usia}, Tinggi: {tinggi}m"