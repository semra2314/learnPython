sozluk = {
    "araba": "car",
    "uçak": "plane",
    "otobüs": "bus",
    "gemi": "ship",
    "tren": "train"
}

while True: 
    print("\nAraba, Uçak, Otobüs, Gemi, Tren (Çıkış için 'çıkış' yazın)")
    kelime = input("İngilizcesini öğrenmek istediğiniz kelimeyi giriniz: ").lower().strip()

    if kelime == "çıkış":
        print("Programdan çıkılıyor...")
        break  

    if kelime == "":
        print("Lütfen bir kelime giriniz!")
    elif kelime in sozluk:
        print(f"{kelime} kelimesinin İngilizcesi: {sozluk[kelime]}")
    else:
        print("Bu kelime sözlükte bulunmuyor.")
