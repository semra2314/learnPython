# 1 - kullanıcıdan iki tane sayı alınsın ve bu sayılar eşit değilse eşitlenip öyle ekrana yazdırılsın
sayi1 = int(input("Sayı Giriniz: "))
sayi2 = int(input("2. Sayıyı Giriniz: "))

if sayi1!=sayi2:
    while sayi1>sayi2:
        sayi1 -=1
        print(sayi1)
    while sayi2>sayi1:
        sayi2 -=1
        print(sayi2)
