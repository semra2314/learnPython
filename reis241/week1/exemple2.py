import random

dictionary = "abcdefghıijklmnoprs"

password = ""
for i in range(0 , 10):
    index = random.randint(0 , len(dictionary)-1)
    password += dictionary[index]

with open("deneme.txt" , "r+" , encoding="utf-8") as file:
    a = file.read()
    if a == "":
        file.write(password)
    else:
        print(a)