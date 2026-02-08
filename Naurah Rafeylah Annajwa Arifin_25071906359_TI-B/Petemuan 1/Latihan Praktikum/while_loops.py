#the while loop
i = 1 #i dimulai dari 1
while i < 7: #i akan terus berulang sampai tidak lebih dari 7
    print(i)
    i += 1 #i selalu bertambah satu

#the break statement
i = 1
while i < 7:
    print(i)
    if i == 3: #jika i mencapai 3, maka pengulangan berhenti
        break #break menyatakan pengulangan berhenti
    i += 1

#the continue statement
i = 1
while i < 7:
    i += 1
    if i == 3: #jika i sama dengan 3, maka angka 3 akan dilewati
     continue #continue adalah perintah untuk melewati
    print(i)

#the else statement
i = 1
while i < 7:
   print(i)
   i += 3 #i selalu ditambah 3
else:
   print("i tidak lebih besar dari 7")

