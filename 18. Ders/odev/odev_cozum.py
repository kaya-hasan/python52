# 1. soru çözümü

# def alan_hesapla(demet):
#     return demet[0] * demet[1]


# liste = [(3, 4), (10, 3), (5, 6), (1, 9)]
# print(list(map(alan_hesapla, liste)))

# 2. soru çözümü

# def ucgen_mi(demet):
#     if abs(demet[0] - demet[1]) < demet[2] and demet[0] + demet[1] > demet[2] \
#             and abs(demet[2] - demet[1]) < demet[0] and demet[2] + demet[1] > demet[0] \
#             and abs(demet[0] - demet[2]) < demet[1] and demet[0] + demet[2] > demet[1]:
#         return True
#     else:
#         return False


# liste = [(3, 4, 5), (6, 8, 10), (3, 10, 7), (100, 1, 1), (111, 10, 11)]
# print(list(filter(ucgen_mi, liste)))

# 3. soru çözümü

# from functools import reduce


# def cift_mi(sayi):
#     if sayi % 2 == 0:
#         return True
#     else:
#         return False


# def topla(sayi1, sayi2):
#     return sayi1 + sayi2


# liste = list(range(1, 11))
# filtre = list(filter(lambda x: x % 2 == 0, liste))
# print(reduce(lambda sayi1, sayi2: sayi1 + sayi2, filtre))


# 4. soru çözümü
# isimler = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
# soyisimler = ["Yılmaz", "Öztürk", "Dağdeviren",
#               "Atatürk", "Dikmen", "Kaya", "Polat"]
# for i, j in zip(isimler, soyisimler):
#     print(f"{i} {j}")
