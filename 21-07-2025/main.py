def mukemmel_decorator(func):
    def wrapper():
        mukemmel_sayi_yazdir()
        func()
    return wrapper


def asal_mi(sayi):
    if (sayi == 1 or sayi == 0):
        return False
    for i in range(2, sayi):
        if (sayi % i == 0):
            return False
    return True


@mukemmel_decorator
def asal_sayilari_yazdir():
    for i in range(1, 1001):
        if asal_mi(i):
            print(i)


def mukemmel_sayi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi


def mukemmel_sayi_yazdir():
    for i in range(1, 1001):
        if mukemmel_sayi(i):
            print(i, "Mükemmel sayıdır")


asal_sayilari_yazdir()
