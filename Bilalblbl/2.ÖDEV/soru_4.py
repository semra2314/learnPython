

kimlik = str(input("TC Kimlik Numaranızı Giriniz: "))

if len(kimlik) != 11 or not kimlik.isdigit():  
    print("TC Kimlik Numarası Geçersiz")
else:
    print("1., 3., 5., 7. ve 9. rakamlar:", kimlik[1],kimlik[3], kimlik[5], kimlik[7], kimlik[9]) 
    print("2., 4., 6. ve 8. rakamlar:", kimlik[2],kimlik[4], kimlik[6], kimlik[8]) 

tektoplam = int(kimlik[1]) + int(kimlik[3]) + int(kimlik[5]) + int(kimlik[7]) + int(kimlik[9])
teksonuc = tektoplam * 7

tektoplam = int(kimlik[2]) + int(kimlik[4]) + int(kimlik[6]) + int(kimlik[8])
sonuc = teksonuc - tektoplam

onbir = 0
for i in range (10):
    onbir = onbir + int(kimlik[i]) 

print(f"10. Hanedeki Rakam {sonuc % 10}")  
print(f"11. Hanedeki Rakam {onbir % 10}")  