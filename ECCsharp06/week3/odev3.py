words = ("Car", "Cat", "Mischievous", "Entrepreneur")
meanings = ("araba", "kedi", "yaramaz", "girişimci")
score = 0
print("\n")
print("---------------------")
print("İNGİLİZCE SORU CEVAP")
print("---------------------\n")

for i in range(len(words)):
    tryingChance = 3
    while tryingChance > 0:
        print(words[i])
        wordPrompt = str.lower(input("Yukarıdaki kelimenin anlamı nedir?\n"))
        if wordPrompt == meanings[i]:
            print("\n")
            print("-------------------------")
            print("TEBRİKLER!! DOĞRU CEVAP!")
            print("-------------------------")
            score += 1
            break
        else:
            tryingChance-=1
            print("----------------------------------")
            print(f"Yanlış! Kalan Deneme Hakkınız: {tryingChance}")
            print("----------------------------------")
            if tryingChance == 0:
                print("---------------------------------------")
                print(f"BİLEMEDİNİZ!!! Doğru Cevap: {meanings[i]}")
                print("---------------------------------------")
                break

print("-------------------")
print("OYUN BİTTİ!!!")
print("-------------------\n")
print(f"Toplam Skorunuz: {score}")
#5. sorunun cevabı