# ==============================
# datatypes.py
# Belajar tipe data di Python
# ==============================

# 1. String
teks = "Hello Python"
print(type(teks))  # <class 'str'>

# 2. Integer
angka = 100
print(type(angka))  # <class 'int'>

# 3. Float
desimal = 3.14
print(type(desimal))  # <class 'float'>

# 4. Complex
kompleks = 3 + 5j
print(type(kompleks))  # <class 'complex'>

# 5. Boolean
benar = True
salah = False
print(type(benar))  # <class 'bool'>

# 6. List
list_contoh = ["apel", "pisang", "jeruk"]
print(type(list_contoh))  # <class 'list'>

# 7. Tuple
tuple_contoh = ("apel", "pisang", "jeruk")
print(type(tuple_contoh))  # <class 'tuple'>

# 8. Set
set_contoh = {"apel", "pisang", "jeruk"}
print(type(set_contoh))  # <class 'set'>

# 9. Dictionary
dict_contoh = {"nama": "Fasbir", "umur": 20}
print(type(dict_contoh))  # <class 'dict'>

# 10. Checking data type
x = 5
print(isinstance(x, int))  # True
print(isinstance(x, str))  # False