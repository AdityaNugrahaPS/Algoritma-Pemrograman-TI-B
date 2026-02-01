"""
Python boolean
"""

# Tipe data boolean dalam Python hanya memiliki dua nilai: True atau False
nilai_boolean_true = True      # Nilai kebenaran: benar
nilai_boolean_false = False    # Nilai kebenaran: salah

# Boolean dari perbandingan
perbandingan_sama = (5 == 5)           # Hasilnya True karena 5 sama dengan 5
perbandingan_tidak_sama = (5 != 3)     # Hasilnya True karena 5 tidak sama dengan 3
perbandingan_lebih_besar = (10 > 5)    # Hasilnya True karena 10 lebih besar dari 5
perbandingan_lebih_kecil = (3 < 7)     # Hasilnya True karena 3 lebih kecil dari 7

# Boolean dari operasi logika
logika_and = True and False            # Hasilnya False karena kedua nilai harus True
logika_or = True or False              # Hasilnya True karena salah satu nilai True
logika_not = not True                  # Hasilnya False karena nilai dibalik

# Boolean dari nilai-nilai tertentu
nilai_string = bool("abc")             # String tidak kosong menghasilkan True
nilai_string_kosong = bool("")         # String kosong menghasilkan False
nilai_angka = bool(5)                  # Angka selain nol menghasilkan True
nilai_nol = bool(0)                    # Angka nol menghasilkan False
nilai_list = bool([1, 2, 3])           # List tidak kosong menghasilkan True
nilai_list_kosong = bool([])           # List kosong menghasilkan False
nilai_dict = bool({"key": "value"})    # Dictionary tidak kosong menghasilkan True
nilai_dict_kosong = bool({})           # Dictionary kosong menghasilkan False
nilai_tuple = bool((1, 2))             # Tuple tidak kosong menghasilkan True
nilai_tuple_kosong = bool(())          # Tuple kosong menghasilkan False
nilai_set = bool({1, 2, 3})            # Set tidak kosong menghasilkan True
nilai_set_kosong = bool(set())         # Set kosong menghasilkan False

# Nilai None sebagai boolean
nilai_none = bool(None)                # None menghasilkan False

# Operator identitas (is) dan keanggotaan (in)
objek_a = [1, 2, 3]
objek_b = [1, 2, 3]
objek_c = objek_a

identitas_sama = objek_a is objek_c    # True karena objek_a dan objek_c adalah objek yang sama
identitas_berbeda = objek_a is objek_b # False karena objek_a dan objek_b adalah objek berbeda
keanggotaan = 2 in objek_a             # True karena 2 adalah anggota dari objek_a
tidak_anggota = 5 in objek_a           # False karena 5 bukan anggota dari objek_a

# Fungsi-fungsi bawaan yang mengembalikan boolean
cek_digit = "123".isdigit()            # True karena semua karakter adalah digit
cek_alpha = "abc".isalpha()            # True karena semua karakter adalah huruf
cek_alphanumeric = "abc123".isalnum()  # True karena semua karakter adalah huruf atau angka
cek_upper = "HELLO".isupper()          # True karena semua huruf kapital
cek_lower = "hello".islower()          # True karena semua huruf kecil
cek_spasi = "   ".isspace()            # True karena semua karakter adalah spasi