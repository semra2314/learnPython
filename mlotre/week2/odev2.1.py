# ebob ekok

a = int(input("İlk sayıyı girin: "))
b = int(input("İkinci sayıyı girin: "))

# EBOB hesaplama
min_sayi = min(a, b)
ebob = 1
for i in range(1, min_sayi + 1):
    if a % i == 0 and b % i == 0:
        ebob = i

# EKOK hesaplama
ekok = a * b
temp = max(a, b)
while True:
    if temp % a == 0 and temp % b == 0:
        ekok = temp
        break
    temp += 1

# Sonuçları ekrana yazdır
print(f"EBOB: {ebob}")
print(f"EKOK: {ekok}")
