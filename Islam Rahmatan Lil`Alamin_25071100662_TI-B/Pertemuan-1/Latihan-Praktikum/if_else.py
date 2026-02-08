## Percabangan If-Else

# If statement
nilai = 75
if nilai >= 60:
    print("lulus")  #output: lulus

# If-Else statement
nilai = 50
if nilai >= 60:
    print("lulus")
else:
    print("tidak lulus")  #output: tidak lulus.

# If-Elif-Else statement
nilai = 75
if nilai >= 85: 
    print("A")  
elif nilai >= 70:
    print("B") #output: B
elif nilai >= 60:
    print("C")
else:
    print("D")


# one-liner
# [jika kondisi benar] if [kondisi] else [jika kondisi salah]
Ipk = 3.7
Kelulusan = "lulus" if Ipk >= 2.5 else "tidak lulus"
print(Kelulusan) #output: lulus

# Nested If
umur = 20
if umur >= 17:
    if umur >= 21:
        print("Dewasa")  #output: Dewasa
    else:
        print("Remaja")
else:
    if umur >= 5:
        print("Anak-anak")
    else:
        print("Balita")

# Kombinasi Nested if dengan One-liner
umur = 2
status = 'Dewasa' if umur >= 21 else 'Remaja' if umur >= 17 else 'Anak-anak' if umur >= 5 else 'Balita'
print(status)  #output: Balita

# Kombinasi dengan operator logika
# pengecekan passowrd yang memiliki syarat tertentu
# minimal 8 karakter, ada huruf besar dan kecil, ada angka

def CekPassword(pw): # fungsi untuk mengecek password
    if len(pw) >= 8:
        if (not pw.islower() and not pw.isupper() and not pw.isalpha() and not pw.isdigit()): # ngecek apakah ada huruf besar dan angka dan total digitnya lebih dari 8
            print("Password valid")  #output: Password valid
        else:
            print("Password harus mengandung huruf besar, huruf kecil, dan angka")
    else:
        print("Password tidak valid, minimal 8 karakter")

CekPassword("Admin1234")  #output: Password valid
CekPassword("admin1234")  #output: Password harus mengandung huruf besar, huruf kecil, dan angka
CekPassword("Admin")      #output: Password tidak valid, minimal 8 karakter
CekPassword("1234567890") #output: Password harus mengandung huruf besar, huruf kecil, dan angka

# menjadikan fungsi diatas menjadi one-liner
def CekPasswordOneLiner(pw):
    print("password memenuhi syarat") if (len(pw) >= 8 and not pw.islower() and not pw.isupper() and not pw.isalpha() and not pw.isdigit()) else print("Password tidak memenuhi syarat")

CekPasswordOneLiner('Admin1234')  #output: password memenuhi syarat
CekPasswordOneLiner('admin1234')  #output: password tidak memenuhi syarat
CekPasswordOneLiner('Admin')      #output: password tidak memenuhi syarat
CekPasswordOneLiner('1234567890') #output: password tidak memenuhi syarat