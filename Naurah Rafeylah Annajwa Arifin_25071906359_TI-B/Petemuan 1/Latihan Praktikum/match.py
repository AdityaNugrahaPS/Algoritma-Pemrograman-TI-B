bulan = 11
match bulan: #menyatakan bulan ke 11
    case 1:
        print("Januari") #jika bulan ke 1 maka tampilkan januari
    case 2:
        print("Februari") #jika bulan ke 2 maka tampilkan februari
    case 3:
        print("Maret") #jika bulan ke 3 maka tampilkan maret
    case 4:
        print("April") #jika bulan ke 4 maka tampilkan april
    case 5:
        print("Mei") #jika bulan ke 5 maka tampilkan mei
    case 6:
        print("Juni") #jika bulan ke 6 maka tampilkan juni
    case 7:
        print("Juli") #jika bulan ke 7 maka tampilkan juli
    case 8:
        print("Agustus") #jika bulan ke 8 maka tampilkan agustus
    case 9:
        print("September") #jika bulan ke 9 maka tampilkan september
    case 10:
        print("Oktober") #jika bulan ke 10 maka tampilkan oktober
    case 11:
        print("November") #jika bulan ke 11 maka tampilkan november
    case 12:
        print("Desember") #jika bulan ke 12 maka tampilkan desember

#default values & combine values
nilai = "A"
match nilai:
    case "A" | "B": #karakter pipe (|) untuk lebih dari satu nilai dalam satu kasus
        print("lulus")
    case "C":
        print("remedial")
    case _: #garis bawah (_) jika ingin mengakhiri kode dan tidak ada pilihan lain
        print("tidak lulus")

