#Bagian ini berisi logika percabangan if, elif, dan else

a = 67
b = 67

if b > a:
  print("b lebih besar dari a")
elif a == b:
  print("a dan b sama besar")
else:
  print("a lebih besar dari b")

# Short Hand If Else (Dibuat di satu baris yang sama)
print("A") if a > b else print("=") if a == b else print("B")