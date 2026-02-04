def tambah(a, b) :
    return a + b

def kurang(a, b) :
    return a - b

def kali(a,b) :
    return a*b

def bagi(a,b) :
    if b == 0 :
        print("Pembagian tidak dapat dilakukan kaena pembagi bernilai 0")
    elif b != 0 :
        return a/b
    
def fibonacci(n) :
    return (n-1) + (n-2)