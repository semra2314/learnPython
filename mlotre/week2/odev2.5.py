# tc kimlik doğrulama uygulaması : tc kimlik numarasını doğrulamak için 1,3,5,7 ve 9. hanelerdeki
# rakamların toplamının 7 ile çarpımından çıkan snucu 2,4,6 ve 8. hanedeki rakamların toplamından
# çıkartıldığında geriye kalanın 10'a böldüğümüzde kalanı 10uncu haneyi verir.
# birinci haneden onuncu haneye kadar olan tüm rakamların toplamını 10'a böldüğümüzde kalan sayı
# 11. rakamı verir bunu kontrol eden bir program yazınız

def isTcLegit(tcno):

    if len(tcno) != 11 or not tcno.isdigit():
        return False

    digits = [int(digit) for digit in tcno]

    sum1 = sum(digits[i] for i in range(0,9,2))     # 1. 3. 5. 7. 9.
    sum2 = sum(digits[i] for i in range(1,8,2))     # 2. 4. 6. 8.

    if (sum1 * 7 - sum2) % 10 != digits[9]:         # 10. hane için kontrol
        return False

    if(sum(digits[:10]) % 10) != digits[10]:        # 11. hane için kontrol
        return False

    return True                                     # Tüm koşullar tuttu, geçerli.


tcno = input("TC kimlik no giriniz: ")

if isTcLegit(tcno):
    print("Geçerli bir TC kimlik numarası.")
else:
    print("Geçersiz TC kimlik numarası.")