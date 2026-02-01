# **** FORLOOP **** #

# Membuat Forloop
fruits = ["Dragon", "Leopard", "Dough"]
for x in fruits:
  print(x)

# Loop Lewat String
for x in "Dragon":
  print(x)

# Break System
fruits = ["Dragon", "Kitsune", "Venom", "Spirit"]
for x in fruits:
  if x == "Venom":
    break           # Berhenti di Venom
  print(x) # Hasil = Dragon dan Kitsune

# Continue ForLoop
fruits = ["Dragon", "Kitsune", "Venom", "Spirit"]
for x in fruits:
  if x == "Kitsune":
    continue
  print(x) # Kitsune tidak di lewati

# Range Function?
for x in range(6):
  print(x)

# Else in ForLoop
for x in range(3):
  print(x)
else:
  print("Proses selesai!")

# Nester ForLoop
tipe = ["Secret", "Mythical"]
fruits = ["Dragon", "Leopard"]

for x in tipe:
  for y in fruits:
    print(x, y)