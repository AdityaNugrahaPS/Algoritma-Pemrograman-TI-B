#STRINGS

string1 = "Loser" # bisa assign string kedalam variabel
percyJacksonParagraph = """Look, I didn't want to be a half-blood.
If you're reading this because you think you might be one, my advice is: close this book right now. 
Believe whatever lie your mom or dad told you about your birth, and try to lead a normal life. Being a 
half-blood is dangerous. It's scary. Most of the time, it gets you killed in painful, nasty ways. If you're a 
normal kid, reading this because you think it's fiction, great.
""" # bisa assign string multi line dalam variabel menggunakan 3 ketip satu atau 3 ketip dua

print("Congratulations") # bisa pakai ketip dua
print('You are the worse') # atau ketip satu
print("He said he was going to a 'party' ") # bisa pakai ketip dalam string ketip hanya ketika ketipnya berbeda
print(string1)
print(percyJacksonParagraph)

#string merupakan sebuah array
string2 = "Someday"
print(string2[2]) # gunakan nomor indeks untuk memilih sebuah karakter untuk di print, dalam contoh ini nomor indeks 2 merupakan 'm'

#looping
string3 = "Gubernatorial"
for x in string3:
 print(x) # gunakan for loop untuk print character satu per satu

#length
string4 = "Break through the middle"
print(len(string4)) # gunakan leng untuk mengetahui panjang sebuah kata/kalimat

#checking
string5 = "I will carry us through the night, through every barrier"
if "night" in string5: # check kalau ada sebuah kata dalam text 
 print("The text contains the word 'night'") 
if "whisper" not in string5: # check kalau tidak ada sebuah kata dalam text
 print("The text doesnt contain the word 'whisper'")

#SLICING
string6 = "For that i'll say i was wrong"
print(string6[5:15]) # you can slice a string by doing this (the second number is not counted)

string7 = "Welcome to space"
print(string7[:12]) # slices from the start to twelve(not included)

string8 = "Perhaps you have simply"
print(string8[9:]) # slices from the number to the end

#MODIFYING
string9 = " We're as happy as can be "
print(string9.upper()) #use upper to turn a string to all upper case
print(string9.lower()) #use to turn all to lower case
print(string9.strip()) # removes whitespaces
print(string9.replace('e', 'i')) # replaces the first letter with the second letter in the string
print(string9.split(' ')) # sepertates all the seperate strings to their own

#CONCATENATE
string10 = "Forgotten"
string11 = "World"
string12 = string10 + string11
print(string12) # use plus to combine two strings
string13 = string10 + ' ' + string11
print(string13) # use quotation marks to add a space