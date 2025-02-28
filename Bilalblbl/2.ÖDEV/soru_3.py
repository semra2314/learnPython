
kelime =input("Kelime Giriniz :")
kkelime = "".join(reversed(kelime))

if kkelime == kelime:
    print(f"{kelime} polindrom bir kelimedir.")
else:
    print(f"{kelime} polindrom bir kelime değildir.")
