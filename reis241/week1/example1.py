import random

password = random.randint(1,1001)

with open("deneme.txt" , "r+" , encoding="utf-8") as file:
    a = file.read()
    if a == "":
        file.write(str(password))
    else:
        print(a)