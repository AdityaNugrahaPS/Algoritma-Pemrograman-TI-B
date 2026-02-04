# jika ada banyak pola yang ingin dicocokkan, kita bisa menggunakan match case
# Contoh program simulasi terminal linux sederhana menggunakan match case

from time import sleep # biar bisa pake fungsi sleep
from function_arguments import loadingBar

def mintaPassword():
    pw = input("Masukkan password: ")
    if pw == "Alamganteng":
        return True
    else:
        return False


while True: # Biar ngulang" terus sampe di break
    command = input("alam@archlinux:~$ ").strip().split() # nge split biar bisa misahin tiap kata dan buang spasi di awal/akhir
    if not command: # biarkalau inputan kosong gak error
        continue
    match command:
        case ['help']:
            # Menampilkan daftar perintah yang tersedia seperti help, shutdown, reboot, exit, pacman(install, search, clear chache), rm(-r, -f, -rf), ls, mkdir, cd, dll) 
            print("Perintah yang tersedia:")
            print("help - Menampilkan daftar perintah")
            print("shutdown - Mematikan sistem")
            print("reboot - Merestart sistem")
            print("exit - Keluar dari program")
            print("sudo - menjalankan perintah sebagai administrator")
            print("pacman - Mengelola paket (install(-S), search(-s), clear cache(-Sc))")
            print("rm - Menghapus file atau direktori (-r, -f, -rf)")
            print("ls - Menampilkan isi direktori")
            print("mkdir - Membuat direktori baru")
            print("cd - Berpindah ke direktori lain")
            print("whoami - Menampilkan nama user saat ini")

        case ["shutdown"]: # mematikan sistem
            if input("Apakah Anda yakin ingin mematikan sistem? (y/n): ") == 'y':
                print("Mematikan sistem...")
                break
            else:
                print("Perintah dibatalkan.")

        case ["whoami"]:
            print("alam") # menampilkan nama user saat ini
        
        case ["reboot"]: # merestart sistem
            if input("Apakah Anda yakin ingin merestart sistem? (y/n): ") == 'y':
                print("Merestart sistem...")
                sleep(3) # kasih jeda 3 detik
                print("Sistem telah direstart")
            else:
                print("Perintah dibatalkan.")

        case ["sudo","pacman", "-S", package]: # menginstall paket
            if not mintaPassword(): # minta password dulu trus cek kalau salah gagal, kalau benar lanjut
                print("Password salah! Akses ditolak.")
                continue
            loadingBar(f"installing {package}")


        case ["sudo","pacman", "-s", package]: # mencari paket
            if not mintaPassword():
                print("Password salah! Akses ditolak.")
                continue
            print(f"Sedang mencari paket: {package}")

        case ["sudo","pacman", "-Sc"]: # membersihkan chache
            if not mintaPassword():
                print("Password salah! Akses ditolak.")
                continue
            print("Membersihkan chache")

        case ["pacman" , 'install' | 'search' | 'clear' | 'cache', *sisa]: # tanpa sudo. (*sisa) maksudnya biar gak error kalo ada inputan tambahan
            print("Tidak memiliki akses root. Gunakan 'sudo' untuk menjalankan perintah ini.")

        case ["sudo","rm", "-r", directory]: # menghapus folder beserta isinya
            if not mintaPassword():
                print("Password salah! Akses ditolak.")
                continue
        
            print(f"Menghapus folder beserta isinya: {directory}")

        case ["sudo","rm", "-f", file]: # menghapus file tanpa konfirmasi
            if not mintaPassword():
                print("Password salah! Akses ditolak.")
                continue
            print(f"Memaksa menghapus file: {file}")

        case ["sudo","rm", "-rf", directory]: # hapus paksa semuaa folder beserta anak cucunya
            if not mintaPassword():
                print("Password salah! Akses ditolak.")
                continue
            print(f"Paksa menghapus folder beserta isinya: {directory}")


        case ['rm', '-r' | '-f' | '-rf', *sisa]: # kalau gapake sudo
            print("Tidak memiliki akses root. Gunakan 'sudo' untuk menjalankan perintah ini.")

        case ["ls"]:
            print("Membuat list isi direktori saat ini")

        case ["mkdir", directory]:
            print(f"Membuat direktori baru: {directory}")

        case ["cd", directory]:
            print(f"Pindah ke directory: {directory}")

        case ["exit"]:
            print("Keluar dari program...")
            break

        case ["fastfetch"] | ["neofetch"]: # Izinnn bang pake ai buat ini doang eheheee
            # Definisi Warna (ANSI Escape Codes)
            # Biar kodingan gak kepanjangn, kita singkat aja
            C = "\033[36m" # Cyan (Warna khas Arch)
            B = "\033[1;34m" # Blue Bold
            P = "\033[1;35m" # Purple
            W = "\033[0m"  # Putih/Reset (Wajib ada biar gak warna terus)
            G = "\033[32m" # Green
            Y = "\033[33m" # Yellow
            R = "\033[31m" # Red

            # ASCII ART Arch Linux (Versi Mini biar rapi)
            # Kita print baris per baris digabung sama infonya
            print(f"{C}                  {P}Alam{W}@{P}archlinux{W}")
            print(f"{C}       /\\        {W}-----------------")
            print(f"{C}      /  \\       {B}OS{W}: AlamOS (Arch Rolling Release)")
            print(f"{C}     /    \\      {B}Kernel{W}: 6.9.420-gacor-edition")
            print(f"{C}    /      \\     {B}Uptime{W}: 1 min (Baru nyala bang)")
            print(f"{C}   /   ,,   \\    {B}Packages{W}: 67 (pacman)")
            print(f"{C}  /   |  |   \\   {B}Shell{W}: kitty 0.44.12")
            print(f"{C} /_-''    ''-_\\  {B}Disk(/){W}: 78GB / 8TB ({G}0.95%{W})")
            print(f"{C}                 {B}CPU{W}: Intel i9-99900K (:v)")
            print(f"{C}                 {B}GPU{W}: RTX 5090 Ti (Eaaa)")
            print(f"{C}                 {B}VRam{W}: 64GB GDDR7 (Aduhaii)")
            print(f"{C}                 {B}Memory{W}: 1.9GB / 192GB ({G}1%{W})")
            print("")
            
            # Baris warna-warni di bawah (Color Palette) biar makin mirip asli
            print(f"   {R}███{G}███{Y}███{B}███{P}███{C}███{W}   ")

        case _:
            print("Perintah tidak dikenali. Ketik 'help' untuk melihat daftar perintah yang tersedia.")
        
    #Biar ada spasi tiap inputan
    print()