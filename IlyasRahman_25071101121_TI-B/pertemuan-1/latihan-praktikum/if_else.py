# ifelse biasa
a = 33
b = 33
if a > b:
    print("a lebih besar dari b")
elif a == b:
    print("a dan b sama") # hasil a dan b sama

umur = 18
if umur >= 17:
    print("anda sudah dewasa")
else:
    print("anda masih di bawah umur") # hasil anda sudah dewasa

print(" ")
# if bersarang
umur = 20
ada_sim = True
if umur >= 17:
    if ada_sim:
        print("anda boleh mengemudi") # hasil anda boleh mengemudi
    else:
        print("anda belum punya sim")
else:
    print("anda masih di bawah umur")

print(" ")        
# ifelse bersarang
nilai = 75
if nilai >= 85:
    print("nilai: A")
elif nilai >= 70:
    print("nilai: B")
elif nilai >= 60:
    print("nilai: C")
else:
    print("nilai: D") # hasil nilai: B

print(" ")
# ifelse pendek
a = 10
b = 20
print("a") if a > b else print("b") # hasil b

Bigger = a if a > b else b
print(Bigger) # hasil 20

c = 15
d = 25
print('c') if c > d else print('=') if c == d else print('d') # hasil d

