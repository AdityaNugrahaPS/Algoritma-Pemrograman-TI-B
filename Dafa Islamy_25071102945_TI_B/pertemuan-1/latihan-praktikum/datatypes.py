'''
text type : str
numeric types : int, float, complex
sequence types : list, tuple, range
mapping type : dict
set types : set, frozenset
boolean type : bool
binary types : bytes, bytearray, memoryview
none type : NoneType
'''

tipe1 = '1' #str
tipe2 = 1 #int
tipe3 = 1.5 #float
tipe4 = True #bool
tipe5 = ['Dafa', 18, 'TI-B'] #list
tipe6 = range(6)
tipe7 = (1,2,3) #tuple
tipe8 = {
    'Nama': 'Dafa',
    'Kelas': 'TI-B',
    'NIM': 25071102945,
    'Mahasiswa aktif': True
} #dict
tipe9 = 6j #complex
tipe10 = {1,2,3,4,5,6} #set
tipe11 = frozenset({1,2,3,4,5,6}) #frozenset
tipe12 = b"Dafa" #bytes
tipe13 = bytearray(6) #bytearray
tipe14 = memoryview(bytes(6)) #memoryview
tipe15 = None #NoneType


#mengetahui tipe data variabel
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

print(tipe7[2]) #mengetahui isi tuple pada index ke-n

print(tipe8['Kelas']) #mengetahui value key pada dict