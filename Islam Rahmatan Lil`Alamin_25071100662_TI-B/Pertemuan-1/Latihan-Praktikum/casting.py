# singkatnya, casting merupakan proses merubah tipe data dari satu jenis ke jenis lainnya

pi = 3.1415926535

#jika langsung di assigment kan, maka variabel pi memiliki tipe data float
print(pi) #output: 3.1415926535
print(type(pi)) #output: float

#contoh casting dari float ke int
pi_int = int(pi)
print(pi_int) #output: 3
print(type(pi_int)) #output: int

#contoh casting dari float ke string
pi_str = str(pi)
print(pi_str) #output: '3.1415926535'
print(type(pi_str)) #output: str

#contoh casting dari float ke boolean
pi_bool = bool(pi)
print(pi_bool) #output: True   karena ada nilai floatnya
print(type(pi_bool)) #output: bool

#contoh casting dari float ke complex
pi_complex = complex(pi)
print(pi_complex) #output: (3.1415926535+0j)
print(type(pi_complex)) #output: complex

#contoh casting dari float ke list
pi_list = list((pi,))
print(pi_list) #output: [3.1415926535]
print(type(pi_list)) #output: list

#contoh casting dari float ke tuple
pi_tuple = tuple((pi,))
print(pi_tuple) #output: (3.1415926535,)
print(type(pi_tuple)) #output: tuple

#contoh casting dari float ke set
pi_set = set((pi,))
print(pi_set) #output: {3.1415926535}
print(type(pi_set)) #output: set

#contoh casting dari float ke dict
#catatan: casting ke dict hanya bisa dilakukan jika kita memiliki pasangan key dan value
pi_dict = dict([('value', pi)])
print(pi_dict) #output: {'value': 3.1415926535}
print(type(pi_dict)) #output: dict

#begitupun sebaliknya, kita bisa melakukan casting dari tipe data lain ke float
#contoh casting dari int ke float
num = 10
num_float = float(num)
print(num_float) #output: 10.0
print(type(num_float)) #output: float

#contoh casting dari string ke float
num_str = "20.5"
num_str_float = float(num_str)
print(num_str_float) #output: 20.5
print(type(num_str_float)) #output: float