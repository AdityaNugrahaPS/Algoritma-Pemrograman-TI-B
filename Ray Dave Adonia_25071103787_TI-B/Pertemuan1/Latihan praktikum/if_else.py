# If
print("-If-")

print("Boolean:")
punya_KTP = True
if punya_KTP:
  print("Anda dapat menggunakan fitur voice chat.")

# Elif
print("-Elif-")
a = 21
b = 36
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("b sama dengan a")
elif a < b:
  print("b lebih kecil dari a")
else:
  print("Error")
print(" ")

# If_else
print("-If-")
level = 7
if level < 4:
  print("Anda diperbolehkan masuk sebagai pemula.")
else:
  print("Anda dilarang masuk karena bukan lagi pemula.")
  print("Silahkan pergi.")
print(" ")

# If, elif, else
print("-If, elif, else-")
umur = 21
if umur > 104:
  print("Lansia")
elif umur > 14:
  print("Dewasa.") 
elif umur > 0:
  print("Anak-anak")
else:
  print("Tidak valid.")
print(" ")

# If singkat
print("-If singkat-")
a = 2
b = 3
if a > b: print("a lebih besar dari b")
else: print("a tidak lebih besar dari b")
print("b lebih besar dari a") if b > a else print("b tidak lebih besar dari a")

# Assign
print("-Assign-")
a = 3
b = 7
lebih = a if a > b else b
kurang = a if a < b else b
print(f"{lebih} lebih besar dari {kurang}.")

# Assign dalam satu baris
print("-Assign dalam satu baris-")
a = 4
b = 5
print("a lebih besar dari b") if a > b else print("b lebih besar dari a") if b > a else print("a = b") # Lebih singkat

print(" ")

# Logical operators
print("-Operasi logika-")
a = 5
b = 3
c = 4
print(" ")
## AND 
print("-And-")
if a > b and b > c: # Memeriksa jika kedua kondisi benar
  print("Semua kondisi benar dan urutan abc dari yang terbesar.")
else:
  print("Tidak ada kondisi yang benar, nilai abc tidak berurutan.")
print(" ")

## OR
print("-Or-")
if a > b or b > c: # Hanya memeriksa kebenaran satu kondisi
  print("Ada kondisi yang benar.")
print(" ")

## NOT
print("-Not-")
if not a > b: # Memeriksa jika kondisi tidak benar / salah
  print("a tidak lebih besar dari b")
else:
  print("a mungkin lebih besar dari b")
print(" ")

# Multiple operators
print("-Multiple operators-")
tinggi_badan = 169
ada_pengawas = False
bisa_berenang = False

if(tinggi_badan > 149):
  print("Silahkan menggunakan wahana.")
elif(tinggi_badan < 120) and not ada_pengawas:
  print("Dilarang menggunakan wahana.")
elif(tinggi_badan < 120) and not ada_pengawas or bisa_berenang:
  print("Silahkan menggunakan wahana, hati-hati.")
else:
  print("Silahkan menggunakan wahana.")
print(" ")

# Nested IF
print("-Nested if-")
harta = 9200
if a > 25:
  print("Diatas 25.")
else:
  print("Dibawah 25.")
  if a > 15:
    print("Diatas 15")
  else:
    print("Dibawah 15")
    if a > 5:
      print("Diatas 5")
    else:
      print("Dibawah 5")
print(" ")

# Pass
print("-Pass statement-")
nilai = 75
if nilai < 70:
  print("Remedial.")
else:
  pass
print("Lulus.")
print(' ')

