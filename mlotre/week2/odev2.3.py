# Sözlük olarak 5 kelime girin kullanıcıya İngilizce / Türkçe mi Türkçe / İngilizce mi diye sorulsun
# sonra girilen kelimenin anlamını yazılsın ekrana

it = {
    "apple": "elma",
    "executioner": "cellat",
    "congratulations": "tebrikler",
    "vase": "vazo",
    "earth": "dünya"
}

secim = input("İngilizce/Türkçe için '1', Türkçe/İngilizce için '2' giriniz: ")

if secim == '1':
    kelime = input("Çevirmek istediğiniz İngilizce kelimeyi girin: ")
    print("Türkçesi:", it.get(kelime.lower()))

elif secim == '2':
    ti = {i: t for t, i in it.items()}
    kelime = input("Çevirmek istediğiniz Türkçe kelimeyi girin: ")
    print("İngilizcesi:", ti.get(kelime.lower()))

else:
    print("Geçersiz seçim!")
