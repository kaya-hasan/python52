
# def kareleri_al():
#     sonuc = []
#     for i in range(1, 6):
#         sonuc.append(i ** 2)
#     return sonuc


# print(kareleri_al())

# def kareleri_al():
#     # generator fonksiyonu
#     for i in range(1, 6):
#         yield i ** 2  # yield anahtar kelimesi ile değer döndürür, fonksiyonun çalışması durmaz ve bir sonraki çağrıda kaldığı yerden devam eder


# generator = kareleri_al()
# # print(kareleri_al())
# iterator = iter(generator)
# print(next(iterator))  # 1
# print(next(iterator))  # 4
# print(next(iterator))  # 9
# print(next(iterator))  # 16
# print(next(iterator))  # 25
# print(next(iterator))  # StopIteration hatası (iteratör bittiğinde hata verir)


# list comprehension ile generator oluşturma
# liste = [i * 3 for i in range(5)]
# print(liste)

# generator_liste = (i * 3 for i in range(5))
# # print(liste)

# iterator = iter(generator_liste)
# print(next(iterator))  # 0
# print(next(iterator))  # 3
# print(next(iterator))  # 6
# print(next(iterator))  # 9
# print(next(iterator))  # 12
# print(next(iterator))  # StopIteration hatası (iteratör bittiğinde hata verir)


# def carpim_tablosu():
#     # generator fonksiyonu
#     for i in range(1, 11):
#         for j in range(1, 11):
#             yield f"{i} x {j} = {i * j}"


# # for i in carpim_tablosu():
# #     print(i)

# generator = carpim_tablosu()
# iterator = iter(generator)
# print(next(iterator))  # 1 x 1 = 1
# print(next(iterator))  # 1 x 2 = 2
# print(next(iterator))  # 1 x 3 = 3


# for i in range(1, 101):
#     print(i)

generator = range(1, 101)  # range fonksiyonu bir generator döndürürür
iterator = iter(generator)
print(next(iterator))  # 1
print(next(iterator))  # 2
print(next(iterator))  # 3
print(next(iterator))  # 4
