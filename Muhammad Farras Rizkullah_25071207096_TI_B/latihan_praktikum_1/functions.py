# Fungsi sederhana
def tambah(x, y):
    return x + y

print(tambah(2, 3))  # Output: 5

# Default parameter
def sapa(nama="Andi"):
    print("Halo", nama)

sapa("Budi")  # Output: Halo Budi
sapa()        # Output: Halo Andi

# Positional argumen
def info(kota, provinsi):
    print(f"{kota}, {provinsi}")

info("Jakarta", "DKI")  # Output: Jakarta, DKI

# Keyword argumen
info(provinsi="Jabar", kota="Bandung")  # Output: Bandung, Jabar

# *args
def daftar(*nama):
    for n in nama:
        print(n)

daftar("Ali", "Budi", "Citra")
# Output:
# Ali
# Budi
# Citra