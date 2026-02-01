# Python If Statement
# Python Conditions and If statements
'''
Python mendukung kondisi logika umum dari matematika:

Sama dengan: a == b
Tidak sama dengan: a != b
Kurang dari: a < b
Kurang dari atau sama dengan: a <= b
Lebih besar dari: a > b
Lebih besar dari atau sama dengan: a >= b
Kondisi ini dapat digunakan dalam beberapa cara, yang paling umum dalam "pernyataan if" dan perulangan.

"Pernyataan if" ditulis dengan menggunakan kata kunci if.'''

a = 33
b = 200
if b > a:
  print("B lebih besar dari A")

# How If Statements Work
'''Pernyataan if mengevaluasi suatu kondisi (ekspresi yang menghasilkan True atau False). Jika kondisinya benar, blok kode di dalam pernyataan if akan dieksekusi. Jika kondisinya salah, blok kode akan dilewati.'''

number = 15
if number > 0:
  print("Positif")

# Indentation
# Python mengandalkan indentasi (spasi di awal baris) untuk menentukan cakupan dalam kode. Bahasa pemrograman lain sering menggunakan kurung kurawal untuk tujuan ini.
'''a = 33
b = 200
if b > a:
print("b lebih besar dari a") # you will get an error'''

# Multiple Statements in If Block
# Anda dapat memiliki beberapa pernyataan di dalam blok if. Semua pernyataan harus diberi indentasi pada level yang sama.
age = 20
if age >= 18:
  print("lebih tua")
  print("sebaya")

# Using Variables in Conditions
# Variabel Boolean dapat digunakan langsung dalam pernyataan if tanpa operator perbandingan.
# Using a boolean variable:
is_logged_in = True
if is_logged_in:
  print("selamat datang!")

# The Elif Keyword
'''
Kata kunci `elif` adalah cara Python untuk mengatakan "jika kondisi sebelumnya tidak benar, maka coba kondisi ini".
Kata kunci `elif` memungkinkan Anda untuk memeriksa beberapa ekspresi untuk nilai Benar dan mengeksekusi blok kode segera setelah salah satu kondisi bernilai Benar.'''

a = 33
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a sama dengan b")

# Multiple Elif Statements
'''Anda dapat menggunakan pernyataan elif sebanyak yang Anda butuhkan. Python akan memeriksa setiap kondisi secara berurutan dan mengeksekusi kondisi pertama yang bernilai benar.'''

score = 75

if score >= 90:
  print("nilai: A")
elif score >= 80:
  print("nilai: B")
elif score >= 70:
  print("nilai: C")
elif score >= 60:
  print("nilai: D")

# How Elif Works
'''Saat Anda menggunakan `elif`, Python mengevaluasi kondisi dari atas ke bawah. Begitu menemukan kondisi yang benar, blok tersebut akan dieksekusi dan semua kondisi yang tersisa akan dilewati.'''
age = 18

if age < 13:
  print("kamu adek ku")
elif age < 20:
  print("kamu abangku")
elif age < 65:
  print("kamu bapakku")
elif age >= 65:
  print("kamu kakek ku")

# When to Use Elif
'''Gunakan `elif` ketika Anda memiliki beberapa kondisi yang saling eksklusif untuk diperiksa. Ini lebih efisien daripada menggunakan beberapa pernyataan `if` terpisah karena Python berhenti memeriksa setelah menemukan kondisi yang benar.'''
day = 3

if day == 1:
  print("senin")
elif day == 2:
  print("selasa")
elif day == 3:
  print("rabu")
elif day == 4:
  print("kamis")
elif day == 5:
  print("jumat")
elif day == 6:
  print("sabtu")
elif day == 7:
  print("minggu")

# The Else Keyword
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dn b sama")
else:
  print("terima kasih")

# Else Without Elif
a = 200
b = 33
if b > a:
  print("b lebih besar dari a")
else:
  print("b tidak lebih besar dari a")

# How Else Works
number = 7

if number % 2 == 0:
  print("kelipatan 2")
else:
  print("tidak kelipatan 2")

# Complete If-Elif-Else Chain
temperature = 22

if temperature > 30:
  print("panas!")
elif temperature > 20:
  print("hangat")
elif temperature > 10:
  print("dingin")
else:
  print("beku!")

# Else as Fallback
nama = "Emil"

if len(nama) > 0:
  print(f"selamat datang, {nama}!")
else:
  print("Error: ")

# Short Hand If
a = 5
b = 2
if a > b: print("a lebih besar dari b")

# Short Hand If ... Else
a = 2
b = 330
print("A") if a > b else print("B")

# Assign a Value With If ... Else
a = 10
b = 20
besar = a if a > b else b
print("lebih besar", besar)

# Multiple Conditions on One Line
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")

# Practical Examples
x = 15
y = 20
max_nilai = x if x > y else y
print("Max nilai:", max_nilai)

nama = ""
display_name = nama if nama else "Guest"
print("selamat datang,", display_name)

# Python Logical Operators
'''
Operator logika digunakan untuk menggabungkan pernyataan kondisional. Python memiliki tiga operator logika:

and - Mengembalikan True jika kedua pernyataan benar
or - Mengembalikan True jika salah satu pernyataan benar
not - Membalikkan hasilnya, mengembalikan False jika hasilnya benar'''

# The and Operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("true")

# The or Operator
a = 200
b = 33
c = 500
if a > b or a > c:
  print("true")

# The not Operator
a = 33
b = 200
if not a > b:
  print("true")

# Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

# Using Parentheses for Clarity
temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

print('=======================')
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

print('=======================')
score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

# Nested If Statements
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# How Nested If Works
age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

# Multiple Levels of Nesting
score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

# Nested If vs Logical Operators
temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

print('==================')
temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

print('==================')
username = "Emil"
password = "python123"
is_active = True

if username:
  if password:
    if is_active:
      print("Login successful")
    else:
      print("Account is not active")
  else:
    print("Password required")
else:
  print("Username required")

print('==================')
score = 92
extra_credit = 5

if score >= 90:
  if extra_credit > 0:
    print("A+ grade")
  else:
    print("A grade")
elif score >= 80:
  print("B grade")
else:
  print("C grade or below")

# The pass Statement
a = 33
b = 200

if b > a:
  pass

# why use pass?
'''
Pernyataan `pass` berguna dalam beberapa situasi:

Saat Anda membuat struktur kode tetapi belum mengimplementasikan logikanya
Saat sebuah pernyataan diperlukan secara sintaksis tetapi tidak diperlukan tindakan apa pun
Sebagai tempat penampung untuk kode di masa mendatang selama pengembangan
Dalam fungsi atau kelas kosong yang Anda rencanakan untuk diimplementasikan nanti
'''
# pass in Development
ge = 16

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

# pass vs Comments
'''score = 85

if score > 90:
  # This is excellent
# This will raise an IndentationError
'''

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")

# pass with Multiple Conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")

# pass in Other Contexts
def calculate_discount(price):
  pass # TODO: Implement discount logic

# Function exists but doesn't do anything yet
