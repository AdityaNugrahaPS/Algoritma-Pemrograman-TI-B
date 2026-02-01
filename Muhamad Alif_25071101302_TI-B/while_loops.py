# Python While Loops
'''
Python memiliki dua perintah perulangan dasar:
perulangan while
perulangan for
'''

# The while Loop
i = 1
while i < 6:
  print(i)
  i += 1

# The break Statement
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# The continue Statement
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

# The else Statement
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i lebih kecil dari 6")
