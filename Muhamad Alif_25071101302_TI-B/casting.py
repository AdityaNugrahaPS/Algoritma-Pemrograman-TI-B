#merubah tipe data ketipe yang lain
#integer
print("======int=====")
data_int = 9
print("data :", data_int, "bertipe :",type(data_int))

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) #akan false jika nilai int = 0
data_compleks = complex(data_int)
print("data :", data_float, "bertipe :",type(data_float))
print("data :", data_str, "bertipe :",type(data_str))
print("data :", data_bool, "bertipe :",type(data_bool))
print("data :", data_compleks, "bertipe :",type(data_compleks))

#float
print("======float=====")
data_float = 9.5
print("data :", data_float, "bertipe :",type(data_float))

data_int = int(data_float) #akan dibulat kan kebawah
data_str = str(data_float)
data_bool = bool(data_float)
data_compleks = complex(data_float)
print("data :", data_int, "bertipe :",type(data_int))
print("data :", data_str, "bertipe :",type(data_str))
print("data :", data_bool, "bertipe :",type(data_bool))
print("data :", data_compleks, "bertipe :",type(data_compleks))

#boolean
print("======boolean=====")
data_bool = False
print("data :", data_bool, "bertipe :",type(data_bool))

data_int = int(data_bool)
data_str = str(data_bool)
data_float = float(data_bool)
data_compleks = complex(data_bool)
print("data :", data_int, "bertipe :",type(data_int))
print("data :", data_str, "bertipe :",type(data_str))
print("data :", data_float, "bertipe :",type(data_float))
print("data :", data_compleks, "bertipe :",type(data_compleks))

#string
print("======string=====")
data_str = "11";
print("data :", data_str, "bertipe :",type(data_str))

data_int = int(data_str) #string harus angka
data_bool = bool(data_str)
data_float = float(data_str) #false jika string kosong
data_compleks = complex(data_str)
print("data :", data_int, "bertipe :",type(data_int))
print("data :", data_bool, "bertipe :",type(data_bool))
print("data :", data_float, "bertipe :",type(data_float))
print("data :", data_compleks, "bertipe :",type(data_compleks))
