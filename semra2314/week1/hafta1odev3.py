# 3 - bir isimlerden oluşan liste oluşturun ve kullanıcıdan ekleme 
# mi yoksa silme işlemi mi yapmak istediğini sorup cevaplara uygun
#  işlemler yapın
Names = ["ali","veli","deli"]

while True:
    print(*Names) # liste elemanlarını ekrana bastır ve burda * işareti ile liste elemanlarını tek tek ekrana bastırma işlemini yaptık
    option = int(input("1 eklemek 2 silmek demek,lütfen birini seçin: "))
    if option==1:
        name = str(input("eklenecek kelimeyi girin : ")) 
        print("ekliyoruzz")
        Names.append(name)
        print("bitti.")
    elif option==2:
        while True:
            name1 = str(input("silmek istediğinz ismi girin : ")) 
            if name1 in Names:
                print("siliyorumm")
                Names.remove(name1)
                print("sildimm.")
                break
            else:
                print("girdiğiniz isim bulunamadı")

                
            