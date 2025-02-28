import random as rand
try:
    file = open("password.txt","r")
    print(file.read())
    file.close()

except:
    password = rand.randint(100000,999999)
    file = open("password.txt","w")
    file.write(str(password))
    print(password)
    file.close()