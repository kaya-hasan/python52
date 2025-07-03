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

# liste = ["Elma", "Armut", "Muz", "Kiraz"]
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


# def asal_mi(sayi):
#     i = 2
#     if sayi < 1:
#         return False
#     elif sayi == 1:
#         return False  # asal sayı değil
#     elif sayi == 2:
#         return True  # 2 en küçük asal sayıdır
#     else:
#         while i < sayi:
#             if sayi % i == 0:
#                 return False  # asal sayı değil
#             i += 1
#     return True  # sayı asaldır


# # print(asal_mi(1972))

# asal_sayilar = filter(asal_mi, range(0, 10000))
# print("asal sayılar: ", list(asal_sayilar))

# map fonksiyonu ********

# def double(sayi):
#     return sayi * 2

# map() fonksiyonu, bir iterable'ın (liste, demet, vb.) her elemanına belirli bir fonksiyonu uygular.
# print(tuple(map(double, [1, 2, 3, 4, 5, 6, 7])))

# print(tuple(map(lambda sayi: sayi ** 2, [1, 2, 3, 4, 5, 6, 7])))

# liste1 = [1, 2, 3, 4]
# liste2 = [5, 6, 7, 8, 111, 222, 333]
# liste3 = [9, 10, 11, 12, 13, 14, 15]

# print(list(map(lambda sayi1, sayi2, sayi3: sayi1 *
#       sayi2 * sayi3, liste1, liste2, liste3)))


# from math import factorial

# def okunus(sayi):
#     if sayi == 1:
#         return "Bir"
#     elif sayi == 2:
#         return "İki"
#     elif sayi == 3:
#         return "Üç"


# print(list(map(okunus, (1, 2, 3))))
# print(list(filter(okunus, (1, 2, 3))))


# zip()
# zip() fonksiyonu, birden fazla iterable'ı (liste, demet, vb.) birleştirir ve her bir iterable'ın elemanlarını bir tuple içinde döndürür.
# liste1 = [1, 2, 3, 4, 5]
# liste2 = [6, 7, 8, 9, 10, 11]

# sonuc = [(1,6), (2,7), (3,8), (4,9), (5,10)]
# i = 0
# sonuc = list()
# while i < len(liste1) and i < len(liste2):
#     sonuc.append((liste1[i], liste2[i]))
#     i += 1
# print(sonuc)

# print(list(zip(liste1, liste2)))

# liste1 = [1, 2, 3, 4, 5]
# liste2 = [6, 7, 8, 9, 10, 11]
# liste3 = ["Python", "Java", "C#", "Javascript", "C"]
# # print(list(zip(liste1, liste2, liste3)))

# for i, j, k in zip(liste1, liste2, liste3):
#     print(f"i: {i * 2} - j: {j * 3} - k: {k + " editlendi"}")

# sozluk1 = {"Elma": 1, "Armut": 2, "Kiraz": 3}
# sozluk2 = {"Kalem": 10, "Silgi": 20, "Defter": 30}
# print(list(zip(sozluk1.values(), sozluk2.keys())))

# reduce()
from functools import reduce
# # reduce() fonksiyonu, bir iterable'ın (liste, demet, vb.) elemanlarını tek bir değere indirger.


# def bolme(sayi1, sayi2):
#     return sayi1 / sayi2


# print(reduce(bolme, [10, 1, 2, 40]))

def maksimum(x, y):
    if x > y:
        return x
    else:
        return y


# print(reduce(maksimum, [1, 500, 10, -6, 77, -101, 93, 10, 2]))
print(min([1, 2, 3, 4, 5, 6, 1, 2, 3, 66, 111, 2, 3, 4, 55, -11]))
