# **** MATCH **** #
# Match mirip dengan switch di C

# Membuat Match
toko = "beli"

match toko:
    case "beli":
        print("Membuka menu pembelian...")
    case "jual":
        print("Membuka menu penjualan...")
    case _:
        print("Perintah tidak dikenal.")

# Menggabungkan Case
status = "owner"

match status:
    case "admin" | "owner":
        print("Akses penuh diberikan.")
    case "pembeli":
        print("Akses terbatas.")

# Guard Match
item = "Dragon"
stok = 0

match item:
    case "Dragon" if stok > 0:
        print("Dragon Ready Ngab, Sung aja!")
    case "Dragon" if stok == 0:
        print("Dragon habis, tunggu restock yaa.")