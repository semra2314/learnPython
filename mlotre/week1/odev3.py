liste = ["Melih", "Semih"]

print("Mevcut liste:", liste)

islem = input("1) Ekleme , 2) Silme ")

if islem == "1":
    a = input("Eklenecek ismi giriniz:")
    liste.append(a)
    print("Mevcut liste:", liste)

elif islem == "2":
    b  = input("Silinecek ismi giriniz:")

    if b in liste:
        liste.remove(b)
    else:
        print("İsim listede yok!")

    print("Mevcut liste:", liste)