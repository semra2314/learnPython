isimler = ["Ali", "Ayşe", "Mehmet", "Zeynep"]

while True:
    print("\nMevcut isimler:", isimler)
    islem = input("Ekleme yapmak için 'E', silme yapmak için 'S', çıkmak için 'Ç' girin: ")

    if islem == "E":  
        yeni_isim = input("Eklemek istediğiniz ismi girin: ")
        if yeni_isim:
            isimler.append(yeni_isim)
            print(f"{yeni_isim} listeye eklendi.")
        else:
            print("Geçerli bir isim girin!")

    elif islem == "S": 
        silinecek_isim = input("Silmek istediğiniz ismi girin: ")
        if silinecek_isim in isimler:
            isimler.remove(silinecek_isim)
            print(f"{silinecek_isim} listeden silindi.")
        else:
            print("Bu isim listede bulunamadı!")

    elif islem == "Ç":  
        print("Programdan çıkılıyor...")
        break

    else:
        print("Geçersiz giriş! Lütfen 'E', 'S' veya 'Ç' girin.")
