def ebob_bul(a, b):
    kucuk = min(a, b)
    for i in range(kucuk, 0, -1): 
        if a % i == 0 and b % i == 0:
            return i  

sayi1 = int(input("Birinci sayıyı giriniz: "))
sayi2 = int(input("İkinci sayıyı giriniz: "))

ebob = ebob_bul(sayi1, sayi2)  
ekok = (sayi1 * sayi2) // ebob  

print(f"{sayi1} ve {sayi2} sayılarının EBOB'u: {ebob}")
print(f"{sayi1} ve {sayi2} sayılarının EKOK'u: {ekok}")