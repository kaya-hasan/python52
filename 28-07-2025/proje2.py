def asal_mi(sayi):
    if (sayi == 1 or sayi == 0):
        return False
    for i in range(2, sayi):
        if (sayi % i == 0):
            return False
    return True


def asal_generator():
    for i in range(2, 1001):
        if asal_mi(i):
            yield i


for asal_sayi in asal_generator():
    print(asal_sayi)
