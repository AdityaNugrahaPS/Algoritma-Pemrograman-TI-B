print("Menghitung angka:")
angka = 1
while angka <= 5:
    print(f"Angka ke-{angka}")
    angka = angka + 1 # Menambah 1 setiap kali jalan agar tidak macet

# Berhenti Paksa (Break)
print("Berhenti di angka 3:")
x = 1
while x <= 10:
    print(x)
    if x == 3:
        break # Berhenti total saat x bernilai 3
    x += 1

# Melewati Angka
print("Melewati angka 2:")
y = 0
while y < 5:
    y += 1
    if y == 2:
        continue # Lewati angka 2 dan langsung lanjut ke angka 3
    print(y)