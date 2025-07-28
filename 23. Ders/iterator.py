# iterator - iterable obje

# bir obje'nin iterable olabilmesi için __iter__() ve __next__() metodlarını tanımlamamız gerekir.

# liste = [1, 2, 3, 4, 5]

# # print(dir(liste))

# iterator = iter(liste)
# print(next(iterator))  # 1 (ilk eleman)
# print(next(iterator))  # 2 (ikinci eleman)
# print(next(iterator))  # 3 (üçüncü eleman)
# print(next(iterator))  # 4 (dördüncü eleman)
# print(next(iterator))  # 5 (besinci eleman)
# print(next(iterator))  # StopIteration hatası (iteratör bittiğinde hata verir)

# liste = [1, 2, 3, 4, 5]
# for i in liste:
#     print(i)

# liste = [1, 2, 3, 4, 5]
# iterator = iter(liste)
# while True:
#     try:
#         print(next(iterator))
#     except StopIteration:
#         break  # iteratör bittiğinde döngüden çık

# __iter__() ve __next__()

# class Kumanda:
#     def __init__(self, kanal_listesi):
#         # constructor - yapılandırıcı
#         # attribute tanımlamaları
#         self.kanallar = kanal_listesi
#         self.index = -1

#     def __iter__(self):
#         # iterable objenin iterator'ını döndürür
#         return self

#     def __next__(self):
#         # bir sonraki elemanı döndürür
#         self.index += 1
#         if self.index < len(self.kanallar):
#             return self.kanallar[self.index]
#         else:
#             self.index = -1
#             raise StopIteration


# kumanda1 = Kumanda(["trt1", "show", "fox", "star", "ntv"])
# iterator = iter(kumanda1)
# print(next(iterator))  # trt1
# print(next(iterator))  # show
# print(next(iterator))  # fox
# print(next(iterator))  # star
# print(next(iterator))  # ntv

# for i in kumanda1:
#     print(i)
