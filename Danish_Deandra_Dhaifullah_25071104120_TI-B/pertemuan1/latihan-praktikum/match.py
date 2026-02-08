#MATCH

#match sama seperti switch case dalam c programming

loading = 0
match loading: # digunakan jika tidak mau menggunakan banyak if statements
    case 10:
        print("10%")
    case 20:
        print("20%")
    case 30:
        print("30%")
    case 40:
        print("40%")
    case 50:
        print("50%")
    case 60:
        print("60%")
    case 70:
        print("70%")
    case 80:
        print("80%")
    case 90:
        print("90%")
    case 100:
        print("100%")
    case _: # gunakan garis bawah seperti else, jika tidak ada persamaan dengan case lain
        print("Has not started loading")
    
month = 7
match month:
    case 1 | 2 | 3 | 4 | 5 | 6 : # bisa menggunakan garis lurus jika mau digabung 
        print('The first half of the year')
    case _:
        print("The second half of the year")

crit_chance = 60
hit = 4
match hit:
    case 1 | 2 | 3 if crit_chance >= 50: # bisa menggunakan if statement dalam match untuk menambah kondisi
        print("Likely chance of a crit")
    case 4 if crit_chance >= 60:
        print("Guaranteed chance of crit")

Month = 12
Day = 25
match Month:
    case 1|2|3|4|5|6|7|8|9|10|11 :
        print("It's not December")
    case 12 if Day == 25:
        print("It's Christmas")
    case _:
        print("Its december but not christmas")
