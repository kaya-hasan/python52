# Proje 2
# Math Modülü olmadan hesap makinesi

def karekok_al(x):
    return x ** 0.5


def kare_al(x):
    return x ** 2


def ust_degere_yuvarla(x):
    if x == int(x):
        return int(x)
    elif x > 0:
        return int(x) + 1
    else:
        return int(x)


def alt_degere_yuvarla(x):
    return x // 1


def faktoriyel_al(x):
    if x < 2:
        return 1
    else:
        return x * faktoriyel_al(x - 1)


def sinus_al(x):
    toplam = 0
    for n in range(10):
        terim = ((-1) ** n) * (x ** (2*n + 1)) / faktoriyel_al(2*n + 1)
        toplam += terim
    return toplam


def kosinus_al(x):
    toplam = 0
    for n in range(10):
        terim = ((-1) ** n) * (x ** (2 * n)) / faktoriyel_al(2 * n)
        toplam += terim
    return toplam


def tanjant_al(x):
    return sinus_al(x) / kosinus_al(x)


def kotanjant_al(x):
    return kosinus_al(x) / sinus_al(x)


def menu():
    print("\n--- Hesap Makinesi ---")
    print("1. Karekok Alma")
    print("2. Kare Alma")
    print("3. Üst değere Yuvarlama")
    print("4. Alt değere Yuvarlama")
    print("5. Faktöriyel Alma")
    print("6. Kosinüs Alma")
    print("7. Sinüs Alma")
    print("8. Tanjant Alma")
    print("9. Kotanjant Alma")
    print("q Çıkış")
