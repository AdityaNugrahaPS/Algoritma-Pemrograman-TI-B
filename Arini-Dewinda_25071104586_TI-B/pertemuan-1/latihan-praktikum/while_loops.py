#while loops

"""
digunakan untuk mengulang selama
kondisi bernilai True
"""

energi = 60
musuh = 1

while energi > 0:
    print("luffy melawan musuh ke-", musuh)

    energi -= 20
    print("energi tersisa:", energi)

    musuh += 1

    if energi <= 0:
        print("energi habis. luffy perlu makan daging untuk mengisi ulang energi.")