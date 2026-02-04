#fungsi yang memanggil dirinya sendiri

def countdown(n):
  if n <= 0:
    print("Done!")
  else:
    print(n)
    countdown(n - 1) #yang ini gapakai return karen ga mengembalikan nilai dan ga punya tipe data

countdown(5)

#contoh penggunaan pada faktorial
def factorial(n):
  # Base case
  if n == 0 or n == 1:
    return 1 #ini pakai return karena dia mengembalikan nilai dan mempunyai tipe data
  # Recursive case
  else:
    return n * factorial(n - 1)

print(factorial(5))