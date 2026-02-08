"""
Python output
ref: https://www.w3schools.com/python/python_output.asp
"""

print("satu dua") # menghasilkan output ke layar

"""
akan error jika petiknya kurang, biasanya akan throw SyntaxError
"""

"""
perlu diperhatikan bahwa print menerima parameter dengan asterisk '*' yaitu print(*obj)
artinya, menerima argumen yang fleksibel. Pemisah args pada print hanyalah
kwargs (keyword arguments)
"""
print("halo", end=" ") # halo 
# catatan: end adalah kwargs

print(123) # 123
print("123") # 123
print("123", 123, 123) # 123 123 123