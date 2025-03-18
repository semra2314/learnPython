# girilen 2 sayının ebob ve ekoklarını çıktı veren kod
#12 ve 3   5 
print("1. sayıyı giriniz\n")
sayi1 = int(input())
print("2. sayıyı giriniz\n")
sayi2 = int(input())
ebob=1

if (sayi2>sayi1):
    temp = sayi1
    sayi1 = sayi2
    sayi2 = temp

if (sayi1>sayi2):
    if (sayi1%sayi2==0):
        print("ebob: ",sayi2)
        print("ekok: ",sayi1)
    for i in range(1,sayi2+1):
        if(sayi1%i==0 and sayi2%i==0):
            ebob=i
    print("ebob: ",ebob)
    #print("ekok: ",(int(sayi1)*int(sayi2))/ebob)
    if (sayi1%sayi2==0 and sayi1!=sayi2):
        print("ekok: ",sayi1)
    else :
        print("ekok: ",sayi1*sayi2)

if (sayi1==sayi2):
    print("ebob: ",sayi1)
    print("ekok: ",sayi1)


"""
ekok = (sayi1 * sayi2) // ebob
print("ekok:", ekok)
"""
"""

# Kullanıcıdan iki sayı al
print("1. sayıyı giriniz:")
sayi1 = int(input())
print("2. sayıyı giriniz:")
sayi2 = int(input())

# EBOB hesaplama fonksiyonu (Öklid Algoritması kullanarak)
def ebob_hesapla(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# EKOK hesaplama fonksiyonu
def ekok_hesapla(a, b):
    return (a * b) // ebob_hesapla(a, b)

# EBOB ve EKOK değerlerini hesapla
ebob = ebob_hesapla(sayi1, sayi2)
ekok = ekok_hesapla(sayi1, sayi2)

# Sonuçları yazdır
print("EBOB:", ebob)
print("EKOK:", ekok)

"""