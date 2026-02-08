#for loops : digunakan untuk mengulang data secara berurutan

#contoh
risol_mayo = ["mentah", "matang", "gosong", "matang", "mentah"]

for i in range(len(risol_mayo)):
    kondisi = risol_mayo[i]

    if kondisi == "matang":
        print("Risol ke-", i + 1, ": siap dimakan")
    elif kondisi == "mentah":
        print("Risol ke-", i + 1, ": perlu digoreng ulang")
    else:
        print("Risol ke-", i + 1, ": gagal, kebanyakan mikir")
