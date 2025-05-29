# gömülü fonksiyonlar - built-in functions
# user defined - kullanıcı tanımlı fonksiyonlar

# parametresiz - void functions
# def selamla():
#     print("Selamlar arkadaşlar!")
#     print("Nasılsınız?")


# print(type(selamla))
# kullanım kısmı - function calling
# selamla()
# selamla()
# selamla()
# selamla()

# def selamla(isim):
#     print("Selam", isim)
#     print("Nasılsınız?", isim)


# selamla("Ahmet")

# def toplama(a, b, c):
#     print("Sayıların toplamları = ", a + b + c)


# toplama(10, 20, 30)

# faktöriyel hesaplama
# def faktoriyel(sayi):
#     faktoriyel = 1
#     # 6! = 6 * 5 * 4 * 3 * 2 * 1
#     if sayi == 0 or sayi == 1:
#         print("Faktöriyel: ", faktoriyel)
#     else:
#         while sayi > 1:
#             faktoriyel *= sayi
#             sayi -= 1
#         print("Faktöriyel: ", faktoriyel)


# faktoriyel(6)

# def selamla(isim="İsimsiz"):
#     # fonksiyon tanımlama - function definition
#     print("Selam", isim)
#     print("Nasılsınız?")


# selamla()

# def bilgileriGoster(ad="Bilgi Yok", soyad="Bilgi Yok", numara="Bilgi Yok"):
#     print("Ad:", ad, "Soyad:", soyad, "Numara:", numara)


# bilgileriGoster(ad="Selçuk", soyad="Veli", numara=1375)

# print(1, 2, 3, sep=10)

# esnek sayıda değerler - yıldızlı parametreler

# def toplama(*parametreler):
#     print(parametreler)


# toplama(1, 2, 3, 4, 5, 6)

def toplama(*parametreler):
    toplam = 0
    for i in parametreler:
        toplam += i
    print(toplam)


toplama(1, 2, 3, 1, 111, 11, 22)
