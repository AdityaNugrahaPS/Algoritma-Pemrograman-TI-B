#1. Setting The Data Type
tipe1 = "Hello"
tipe2 = 1
tipe3 = 1.5
tipe4 = True
tipe5 = 1j
tipe6 = [1,3,4,5]
tipe7 = (1,2,3)
tipe8 = range(7)
tipe9 = {
    'nama' : 'aini',
    'hobi' : 'baca webtoon',
    'status' :  'rahasia'
}
tipe10 = {"teknik", "fmipa", "faperta"}
tipe11 = frozenset({"teknik", "fmipa", "faperta"})
tipe12 = b"Hello"
tipe13 = bytearray(7)
tipe14 = memoryview(bytearray(7))
tipe15 = None

#2. Getting The Data Type
'''
Untuk menampilkan tipe data dari suatu variabel, bisa dengan menggunakan type().
'''

print("--Getting The Data Type--")
print(type(tipe1))
print(type(tipe2))
print(type(tipe3))
print(type(tipe4))
print(type(tipe5))
print(type(tipe6))
print(type(tipe7))
print(type(tipe8))
print(type(tipe9))
print(type(tipe10))
print(type(tipe11))
print(type(tipe12))
print(type(tipe13))
print(type(tipe14))
print(type(tipe15))

#3. Setting the Specific Data Type
'''
Jika ingin menentukan tipe data spesifik, bisa menggunakan Fungsi berikut ini.
'''

tipe1 = str("Hello")                                # String
tipe2 = int(1)                                      # Integer
tipe3 = float(1.5)                                  # Float
tipe4 = bool(True)                                  # Boolean
tipe5 = complex(1j)                                 # Complex
tipe6 = list([1, 3, 4, 5])                          # List
tipe7 = tuple((1, 2, 3))                            # Tuple
tipe8 = range(7)                                    # Range
tipe9 = dict({
    "nama": "aini",
    "hobi": "baca webtoon",
    "status": "rahasia"
})                                                  # Dictionary
tipe10 = set({"teknik", "fmipa", "faperta"})        # Set
tipe11 = frozenset({"teknik", "fmipa", "faperta"})  # Frozenset
tipe12 = bytes("Hello", "utf-8")                    # Bytes
tipe13 = bytearray(7)                               # Bytearray
tipe14 = memoryview(bytearray(7))                   # Memoryview
tipe15 = None                                       # NoneType