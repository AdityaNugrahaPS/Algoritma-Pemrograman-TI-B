string = '1' # string yang berisi angka

string_to_numbers = int(string) # mengubah string ke integer
print(type(string_to_numbers)) # hasilnya int

int_to_string = str(string_to_numbers) # mengubah integer ke string
print(type(int_to_string)) # hasilnya str

float_to_string = float(string_to_numbers) # mengubah integer ke float
print(type(float_to_string)) # hasilnya float

string_to_bool = bool(string) # mengubah string ke boolean
print(type(string_to_bool)) # hasilnya bool

print(type(string)) 
print(type(string_to_numbers))