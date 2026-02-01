#FOR LOOPS

movies = ["Dune", "The Godfather", "Nope", "Superman"]
for x in movies: # digunakan untuk iterasi sebuah sequence 
    print(x)

for y in 'Tough Luck':
    print(y) # bisa menggunakan untuk sebuah string juga

colours = ["Blue", "White", "Magenta", 'Red']
for z in colours:
    print(z)
    if z == "Magenta":
        break # break untuk berhenti pada satu value 

anime = ["One Piece", 'Death Note', 'OPM', 'JJK']
for a in anime:
    if a == 'OPM':
        break
    print(a) # kalau print setelah break kondisi diatas tidak dihitung

bodyParts = ["Legs", "Eye", "Head", "Belly"]
for b in bodyParts:
    if b == 'Eye':
        continue # continue untuk melanjutkan iterasi dengan kondisi atas tidak dihitung
    print(b)

for c in range(10):
    print(c) # range mengembalikan suatu sequence dari nomor mulai dari 0

for d in range(2, 15):
    print(d) # bisa ada dua nomor dalam range yang pertama mulainya dan kedua akhirnya tapi ingat tidak dihitung samapai 15 berhenti pada 14

for e in range(3, 30, 5):
    print(e) # nomor ketiga untuk mengetahui apa kenaikan dari rangenya
else:
    print("All numbers counted for") # bisa juga command else dalamnya

for f in range(1, 15, 3):
    if f == 7: break
    print(f)
else:
    print("All numbers counted for") # kalau ada break sebelumnya else tidak diprint

#NESTED LOOPS
verbs = ['Running', "Sleeping", "Reading", "Dying"]
object = ["Man", "Sloth", "Book", "Dodo"]
for v in verbs: # bisa print dua sequence
    for o in object:
        print(v,o) 

for l in ["how", 'do', 'right']:
    pass # kalau for loop nya tidak ada isi maka gunakan pass untuk skip loopnya dan tidak dapat error