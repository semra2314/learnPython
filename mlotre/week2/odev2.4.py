# bir string ifadenin polindrom olup olmadığını kontrol etme: polindrom terstende düz halide aynı olmasıdır
# "nalan nazan efe radar" gibi kontrol eden bir program yazınız

word = input("Bir kelime giriniz: ")

word = word.lower()

if word == word[::-1]:                          # bu ifade bir dizinin tersini alır
    print(f"'{word}' bir palindromdur.")
else:
    print(f"'{word}' bir palindrom değildir.")