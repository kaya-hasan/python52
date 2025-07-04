from functools import reduce
print("********** Proje 1 **********")

liste = [(3, 4), (10, 3), (5, 6), (1, 9)]


def alan_hesapla(sayi):
    kisa_kenar, uzun_kenar = sayi
    alan = kisa_kenar * uzun_kenar
    return alan


print(list(map(alan_hesapla, liste)))

print("********** Proje 2 **********")
liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7)]


def ucgen_hesapla(kenarlar):
    a, b, c = kenarlar
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False


ucgen_kenarlari = filter(ucgen_hesapla, liste)
print(list(ucgen_kenarlari))

ucgen_kenarlari2 = filter(
    lambda x: x[0] + x[1] > x[2] and x[0] + x[2] > x[1] and x[1] + x[2] > x[0], liste)
print(list(ucgen_kenarlari2))


print("********** Proje 3 **********")

liste = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

cift_sayi = list(filter(lambda x: x % 2 == 0, liste))

print(list(cift_sayi))
toplam = reduce(lambda x, y: x+y, cift_sayi)
print(toplam)

print("********** Proje 4 **********")

isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren",
              "Atatürk", "Dikmen", "Kaya", "Polat"]

print(list(zip(isimler, soyisimler)))
for i, j in zip(isimler, soyisimler):
    print(i, j)
