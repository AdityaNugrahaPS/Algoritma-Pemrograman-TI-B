#Penjumlahan
def penambahan(a, b):
    return a + b

#Pengurangan
def pengurangan(a, b):
    return a - b

#Perkalian
def perkalian(a, b):
    return a * b

#Pembagian
def pembagian(a, b):
    return a / b

#Modulus
def modulus(a, b):
    return a % b

#Fibonacci
def fibonacci(n):
    if n <= 1:
      return n
    else:
      return fibonacci(n - 1) + fibonacci(n - 2)