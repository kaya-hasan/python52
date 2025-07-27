# def fonksiyon(isim, *args):
#     print("isim ", isim)
#     print(args)
#     print("args elemanları")
#     for i in args:
#         print(i)


# fonksiyon("Hasan", 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

# def my_func(**kwargs):  # key-value argümanları
#     print(kwargs)
#     for i, j in kwargs.items():
#         print(f"{i} - {j}")


# my_func(isim="Hasan", sirket="Nova", mevsim="Yaz", yas=30, sehir="Istanbul")

# def yeni_fonksiyon(*args, **kwargs):
#     for i in args:
#         print("Argümanlar: ", i)
#     print("***************************")
#     for key, value in kwargs.items():
#         print(f"Argüman ismi: {key} - Argüman değeri: {value}")


# yeni_fonksiyon(1, 2, 3, 4, "selcuk", "nova", 6, 7, 8, 9,
#                isim="Veli", yas=22, sehir="İzmir", adres="Konak")

# def selamla(isim):
#     print("Selam ", isim)


# # selamla("Mehmet")
# degisken_ismi = selamla
# # print(degisken_ismi)
# degisken_ismi("Tayfun")
# # selamla("Zeynep")
# del selamla
# # selamla("Zeki")
# degisken_ismi("Müjdat")

# scope 1
# def fonksiyon():
#     # scope 2
#     def fonksiyon2():
#         print("Ben küçük bir fonksiyonum.")
#     print("Ben büyük bir fonksiyonum.")
#     fonksiyon2()


# fonksiyon()
# fonksiyon2()

# def fonksiyon(*args):
#     def topla(args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam
#     print(topla(args))


# fonksiyon(1, 2, 3, 4, 5, 6, 7)

# def fonksiyon(islem_adi):
#     def toplama(*args):
#         toplam = 0
#         for i in args:
#             toplam += i
#         return toplam

#     def carpma(*args):
#         carpim = 1
#         for i in args:
#             carpim *= i
#         return carpim

#     if islem_adi == "topla":
#         return toplama
#     else:
#         return carpma


# print(fonksiyon("topla")(1, 2, 3, 4, 5))


def toplama(a, b):
    return a + b


def carpma(a, b):
    return a * b


def cikartma(a, b):
    return a - b


def bolme(a, b):
    return a / b


def anafonksiyon(func1, func2, func3, func4, islem_adi):
    if islem_adi == "toplama":
        print(func1(5, 10))
    elif islem_adi == "carpma":
        print(func2(5, 10))
    elif islem_adi == "cikarma":
        print(func3(5, 10))
    elif islem_adi == "bolme":
        print(func4(5, 10))
    else:
        print("Geçersiz işlem..")


anafonksiyon(toplama, carpma, cikartma, bolme, "toplama")
anafonksiyon(toplama, carpma, cikartma, bolme, "carpma")
anafonksiyon(toplama, carpma, cikartma, bolme, "cikarma")
anafonksiyon(toplama, carpma, cikartma, bolme, "bolme")
