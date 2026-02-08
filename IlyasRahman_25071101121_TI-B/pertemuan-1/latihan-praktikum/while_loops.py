i = 1
while i <= 5:
    print("Perulangan ke-", i)
    i += 1 # while loop biasa

j = 1
while j <= 10:
    print("Nilai j adalah", j)
    if j == 5:
        break # menghentikan perulangan saat j sama dengan 5
    j += 1

k = 1
while k <= 10:
    k += 1
    if k % 2 == 0:
        continue # melewati iterasi saat k adalah bilangan genap
    print("Nilai k adalah", k)

l = 1
while l <= 5:
    print("Perulangan ke-", l)
    l += 1
else:
    print("Perulangan selesai") # blok else setelah while

m = 1
while m <= 5:
    print("Perulangan ke-", m)
    m += 1
    if m == 3:
        break # karena perulangan dihentikan, blok else tidak dijalankan
else:
    print("Perulangan selesai") # blok else setelah while