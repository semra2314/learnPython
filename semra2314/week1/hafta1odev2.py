# 2 - 1den yüze kadar sayı yazılsın ekrana ama 10un katı olanları yazdırmasın
"""
for a in range(1,101):
    if a %10!=0:
        print(a)
"""
for a in range(1,101):
    if a %10 == 0:
        continue
    print(a)
