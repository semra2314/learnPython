def censor(sentence):
    badwords = ("sik", "amk", "aq", "göt")  # consider making this an argument too
    sentence = sentence.split()

    for index, word in enumerate(sentence):
        if any(badword in word for badword in badwords):
            sentence[index] = "".join(['*' if c.isalpha() else c for c in word])

    return " ".join(sentence)  # return rather than print

censoredWord = input("Lütfen bir cümle giriniz: ")
censoredWord = censor(censoredWord)  # Sansürlenmiş cümleyi geri döndür ve değişkene ata
print(censoredWord)  # Sansürlenmiş cümleyi yazdır
#4. sorunun cevabı