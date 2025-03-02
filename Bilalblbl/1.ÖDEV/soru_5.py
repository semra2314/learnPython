list = [1,2,3,3,4,5,6,6,7,7,7,8,9]

sonislem = 0

for x in set(list):
    tekrar = list.count(x)
   
    if tekrar != 1 :
        sonuc = tekrar * x
        sonislem += sonuc
        print(f"{x} sayısı {tekrar} kadar tekrar ediyor")
    
        print(f"{x} sayısının {tekrar} sayısı ile çarpımı : {sonuc}")
    
        
print(f"Tüm tekrar eden sayıların çarpımlarının toplamı: {sonislem}")
    
    