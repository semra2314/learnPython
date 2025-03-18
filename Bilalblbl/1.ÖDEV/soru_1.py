sayi1 = int(input("1.sayıyı giriniz :"))
sayi2 = int(input("2.sayıyı giriniz :"))

if sayi1 != sayi2:
    sayi2 = sayi1
    print(f"İki sayı birbirine eşit olmadığından {sayi1} ve {sayi2} olmak üzere eşitlenmişlerdir.")   
    
elif sayi2 == sayi1:
    print("İki sayı birbirine eşittir")