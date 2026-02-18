import random

print(random.randint(5, 10))
print(random.random())

# random.random kullanılarak random.randint fonksiyonu oluşturun


def rint(a, b):
    aralik = (b-a)*random.random()
    sonuc = aralik + a

    return sonuc


print(rint(5, 10))
