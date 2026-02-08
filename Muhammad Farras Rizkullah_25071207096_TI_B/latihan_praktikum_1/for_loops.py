# Contoh 1: Looping dengan range
for i in range(3):  # mencetak halo sebanyak 3 kali
    print("halo")

print()  # baris kosong

# Contoh 2: Looping string dengan end=""
kode = "ABC123"
for huruf in kode:
    print(huruf, end="-")

print("\n")  # baris baru

# Contoh 3: Looping dictionary
negara = {
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur"
}
for n, ibukota in negara.items():
    print(f"{n}: {ibukota}")

print()  # baris kosong

# Contoh 4: Nested for loop sederhana
buah = ["apel", "pisang"]
warna = ["merah", "kuning"]

for b in buah:
    for w in warna:
        print(f"{b} {w}")