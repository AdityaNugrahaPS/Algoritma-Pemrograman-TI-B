tipe1 = '1'
tipe2 = 1
tipe3 = 1.5
tipe4 = True
tipe5 = [1,2,3,4]
tipe6 = ['nauu',2,3]
tipe7 = (1,2,3)
tipe8 = {
    'nama': 'nauu',
    'kelas' : 'TI B',
    'nim' : '25071906359',
    'Mahasiswa aktif' : True
}

print(type(tipe1)) #untuk memeriksa tipe data pada tipe1
print(type(tipe2)) #untuk memeriksa tipe data pada tipe2
print(type(tipe3)) #untuk memeriksa tipe data pada tipe3
print(type(tipe4)) #untuk memeriksa tipe data pada tipe4
print(type(tipe5)) #untuk memeriksa tipe data pada tipe5
print(type(tipe6)) #untuk memeriksa tipe data pada tipe6
print(type(tipe7)) #untuk memeriksa tipe data pada tipe7
print(tipe8['kelas']) #untuk memeriksa tipe data pada tipe8 untuk mengambil data 'kelas'

data = "See you at the next pale dawn, partner." #ini merupakan tipe data str (string)
data = 300 #ini merupakan tipe data int (integer)
data = 33.550 #ini merupakan tipe data  float	
data = 1j #ini merupakan tipe data  complex	
data = ["Cassie", "Agy", "Cinny"] #ini merupakan tipe data list atau array	
data = ("Dannie", "Snowy", "Dhei") #ini merupakan tipe data tuple	
data = range(7)	#ini merupakan tipe data range
data = {"name" : "Phainon", "age" : 36}	#ini merupakan tipe data dict	
data = {"Naxi", "Dhei", "Snowy"} #ini merupakan tipe data set
data = frozenset({"Cyrene", "Cassie", "Evey"}) #ini merupakan tipe data  frozenset
data = True	#ini merupakan tipe data bool (boolean)
data = b"Evernight"	#ini merupakan tipe data bytes
data = bytearray(3) #ini merupakan tipe data bytearray
data = memoryview(bytes(360)) #ini merupakan tipe data memoryview
data = None #tidak ada tipe data

#contoh
z = str("See you at the next pale dawn, partner.")		
z = int(300)	
z = float(33.550)	
z = complex(1j)
z = list(("Cassie", "Agy", "Cinny"))		
z = tuple(("Dannie", "Snowy", "Dhei"))		
z = range(7)	
z = dict(name="Phainon", age=36)	
z = set(("Naxi", "Dhei", "Snowy"))		
z = frozenset(("Cyrene", "Cassie", "Evey"))	
z = bool(5)		
z = bytes(7)		
z = bytearray(3)
z = memoryview(bytes(360))	


