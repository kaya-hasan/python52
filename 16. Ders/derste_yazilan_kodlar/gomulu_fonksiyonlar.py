# # all - any

# def hepsi(liste):
#     # bütün değerler True ise True, en az birisi False ise False döndürmek istiyoruz.
#     # liste = [True, True, True, False]
#     # return False
#     for i in liste:
#         if not i:
#             return False
#     return True


# # Boolean - True - False (Sayısal) True = 1, False = 0
# # print(hepsi([True, True, True, True, True, True, True]))
# # Integer degerlerde 0 hariç tüm değerlerin Boolean karşılığı True'dur. Ancak 0'ın karşılığı False'tur.

# # print(hepsi([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))
# def herhangi(liste):
#     # Herhangi bir değer True ise True, Hepsi False ise False değer döndürür.
#     # liste = [False, False, False, False]
#     for i in liste:
#         if i:
#             return True
#     return False


# print(herhangi([False, False, False, False]))

# all()

# liste = [False, False, False, False, 99]

# # print(all(liste))

# print(any(liste))

# ENUMERATE Fonksiyonu

liste = ["Elma", "Armut", "Muz", "Kiraz"]
# sonuc = [(0, "Elma"), (1, "Armut"), (2, "Muz"), (3, "Kiraz")]

# sonuc = list()
# i = 0
# for eleman in liste:
#     sonuc.append((i, eleman))
#     i += 1

# print(sonuc)

# sonuc = list(enumerate(liste))
# print("sonuc: ", sonuc)
# enumerate() fonksiyonu, bir iterable'ın (liste, demet, vb.) her elemanını ve onun indeksi ile birlikte döndürür.
# liste = ["a", "b", "c", "d", "e", "f", "g"]
# for index, eleman in enumerate(liste):
#     if index % 2 == 1:
#         print(f"Index: {index} - Eleman: {eleman}")

# Filter()

# filter() fonksiyonu, bir iterable'ın (liste, demet, vb.) her elemanını belirli bir koşula göre filtreler.
# filter(mantıksal değer dönen bir tane fonksiyon(True-False), liste gibi tuple gibi iterable bir veritipi)

# sonuc = filter(lambda x: x % 2 == 0, range(1, 10000))
# print("sonuc: ", list(sonuc))


def asal_mi(sayi):
    i = 2
    if sayi < 1:
        return False
    elif sayi == 1:
        return False  # asal sayı değil
    elif sayi == 2:
        return True  # 2 en küçük asal sayıdır
    else:
        while i < sayi:
            if sayi % i == 0:
                return False  # asal sayı değil
            i += 1
    return True  # sayı asaldır


# print(asal_mi(1972))

asal_sayilar = filter(asal_mi, range(0, 10000))
print("asal sayılar: ", list(asal_sayilar))
