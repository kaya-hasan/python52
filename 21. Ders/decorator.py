# decorator
# import time


# def kareleri_hesapla(sayilar):
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 2)
#     print("Kareleri hesapla fonksiyonu bitti")
#     bitis = time.time()
#     print(f"Bu fonksiyon {bitis - baslama} saniye sürdü.")


# def kupleri_hesapla(sayilar):
#     baslama = time.time()
#     sonuc = []
#     for i in sayilar:
#         sonuc.append(i ** 3)
#     print("Küpleri hesapla fonksiyonu bitti")
#     bitis = time.time()
#     print(f"Bu fonksiyon {bitis - baslama} saniye sürdü.")


# kareleri_hesapla(range(1000000))
# kupleri_hesapla(range(1000000))


import time


def zaman_hesapla(fonksiyon):
    def wrapper(sayilar):
        baslama = time.time()
        sonuc = fonksiyon(sayilar)
        bitis = time.time()
        print(fonksiyon.__name__ + " " + str(bitis - baslama) + " saniye sürdü.")
        return sonuc
    return wrapper


@zaman_hesapla
def kareleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 2)
    print("Kareleri hesapla fonksiyonu bitti")


@zaman_hesapla
def kupleri_hesapla(sayilar):
    sonuc = []
    for i in sayilar:
        sonuc.append(i ** 3)
    print("Küpleri hesapla fonksiyonu bitti")


kareleri_hesapla(range(1000000))
kupleri_hesapla(range(1000000))
