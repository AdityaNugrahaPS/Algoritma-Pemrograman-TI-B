# **** WHILE LOOP **** #
# While Loop gunanya untuk mengulang suatu perintah selama kondisinya masih benar

# Membuat While Loop
i = 1
while i < 6:
  print(i)
  i += 1  # Kalo gak ditambah program jalan terusss

# Break System
i = 1
while i < 6:
  print(i)
  if i == 3:
    break # Agar berhenti di 3
  i += 1

# Continue While
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue # Angka 3 di skip lanjut ke angka berikutnya
  print(i)

# Else While
i = 1
while i < 3:
  print(i)
  i += 1
else:
  print("Perulangan selesai!")