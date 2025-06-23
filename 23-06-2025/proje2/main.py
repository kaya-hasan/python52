liste = range(1, 20)


def sayi_kontrol(sayi):
    if sayi % 2 == 0:
        return f"{sayi} çift sayıdır"
    else:
        raise ValueError(f"{sayi} tek sayıdır.")


for i in liste:
    try:
        sonuc = sayi_kontrol(i)
        print(sonuc)
    except ValueError:
        pass
