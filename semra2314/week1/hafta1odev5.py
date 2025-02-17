# 5 - sayılardan oluşan listede birden fazla tekrar eden sayı var ise onların tekrar sayısı ve sayının kendisiyle çarpıp(eğer birden fazla tekrar eden sayı varsa çıkan sonuçları toplayın) ekrana yazdırın
Numbers = [1,2,3,3,4,5,5,5,6]
total = 0
for a in set(Numbers): #burda set fonksiyonu ile tekrarlanmayan sayıları alıyoruz
    if Numbers.count(a)>1: #burda sayının kaç kere tekrar edildiğini kontrol ediyoruz
        num = a * int(Numbers.count(a)) #burda tekrar edilen sayının kaç kere tekrar edildiğini sayının kendisine katarak yeni
        total += num
print(total)