liste = [2, 3, 2, 5, 3, 3, 7, 5, 5, 5]

sayac = {}

for sayi in liste:
    sayac[sayi] = sayac.get(sayi, 0) + 1

toplam = 0

for sayi in sayac:
    if sayac[sayi] > 1:
        toplam += sayi * sayac[sayi]

print("Sonuç:", toplam)