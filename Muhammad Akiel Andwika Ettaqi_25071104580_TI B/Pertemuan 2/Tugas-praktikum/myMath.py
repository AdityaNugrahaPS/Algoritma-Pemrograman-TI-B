def penambahan(a,b):
    return a + b 
def pengurangan(a,b):
    return a - b
def perkalian(a,b):
    return a * b
def pembagian(a,b):
    if b == 0:
        print("Pembagian tidak dapat dilakukan karena pembagi bernilai 0")
        return 0
    else:
        return a / b
def modulus(a,b):
    return a % b

def fibonacci(n):
  if n <= 1:
    return n
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)

