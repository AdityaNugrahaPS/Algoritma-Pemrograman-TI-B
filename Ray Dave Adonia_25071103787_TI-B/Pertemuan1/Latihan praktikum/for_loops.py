# List
print("-For loop list-")
peserta = ["Leri", "Edo", "Ipin"]
for pemain in peserta:
    print(pemain) 
print()

# String
for x in "Κωνσταντινούπολις":
    print(x)
print()

# Break
peserta = ["Leri", "Nadin", "Tahu", "Edo", "Ipin", "Santi", "Ridho", "Sari"]
for pemain in peserta:
    print(pemain)
    if pemain  == "Ipin": # Loop berhenti setelah Ipin
        break
print()

for pemain in peserta:
    if  pemain == "Ipin": # Loop berhenti sebelum Ipin
        break
    print(pemain)
print()

# Continue
print("-Continue-")
for pemain in peserta:
    if pemain == "Ipin":
        continue 
    print(pemain)

# Range
print("-Range-")
for x in range(0, 20):
    print(x, "tahun = masih dibawah umur.")
print()

# Else
print("-Else-")
for x in range(0, 100):
    print(f"Memuat... {x}%")
else:
    print("Selesai!")
print()

# Nested loop
a = [2, 5, 7]
b = [2, 5, 7]
c = [2, 5, 7]
for x in a:
    for y in b:
        for z in c:
            print(x, y, z)