#if else

#python if: digunakan untuk menjalankan kode jika kondisi bernilai True

energi = 20

if energi < 50:
    print("Kamu butuh istirahat.")

#python elif: digunakan untuk kondisi tambahan jika if tidak terpenuhi

waktu_tidur = 5

if waktu_tidur > 7:
    print("tidur cukup")
elif waktu_tidur > 10:
    print("tidur berlebihan")

#python else: dijalankan jika semua kondisi sebelumnya salah

energi = 20

if energi > 60:
    print("energi tinggi.")
elif energi > 30:
    print("energi cukup.")
else:
    print("energi rendah. istirahat.")

#shorthand if: versi singkat dari if

status = "online"
print("Aktif") if status == "online" else print("Offline")

#logical operators: menggabungkan beberapa kondisi dalam if

jam_tidur = 7
minum_eskopi = True

if jam_tidur >= 6 and minum_eskopi:
    print("Kamu akan segar seharian.")

#nested if: if di dalam if

nilai = 85

if nilai >= 70:
    if nilai >= 90:
        print("nilai sangat baik.")
    else:
        print("nilai cukup.")

#pass statement: digunakan jika if belum diisi

nilai = 60

if nilai > 80:
    pass
else:
    print("nilai cukup rendah.")





