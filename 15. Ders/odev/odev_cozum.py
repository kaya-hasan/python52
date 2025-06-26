# 1. ödev

# liste = ["345", "sadas", "324a", "14", "kemal", "11sdfg", "24-.sad", "344f"]

# for eleman in liste:
#     try:
#         eleman = int(eleman)
#         print(eleman)
#     except:
#         pass

# 2. ödev


def cift_mi(sayi):
    if sayi % 2 == 0:
        return sayi
    else:
        raise ValueError("Sayı çift değil")


liste = [111, 452, 66, 71, 55, 52, 12, 8]
for i in liste:
    try:
        print(cift_mi(i))
    except ValueError:
        pass
