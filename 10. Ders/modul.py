# her python dosyası bir modüldür.
from math import *
import math

# print(dir(math))

# print(help(math))

# print(help(math.factorial))

# print(math.factorial(3))

# print(math.floor(5.9))

# print(math.ceil(5.3))

# alias
# import math as mt

# print(mt.factorial(5))

# from math import factorial, floor

# # print(factorial(9))

# print(floor(15.5))


def factorial(sayi):
    print("kendi factorial fonksiyonum...")
    faktoriyel = 1
    if sayi == 0 or sayi == 1:
        return 1
    while sayi >= 1:
        faktoriyel *= sayi
        sayi -= 1
    return faktoriyel


print(factorial(5))
