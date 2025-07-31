
# class Kareler:
#     def __init__(self, maksimum):
#         self.sayi = 0
#         self.maksimum = maksimum

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.sayi < self.maksimum:
#             self.sayi += 1
#             return self.sayi ** 2
#         else:
#             self.sayi = 0
#             raise StopIteration


# kareler = Kareler(5)
# iterator = iter(kareler)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))  # StopIteration hatası alır


def asal_mi(sayi):
    i = 2
    while i < sayi:
        if sayi % i == 0:
            return False
        i += 1
    return True


def asal_generator():
    i = 2
    while True:
        if asal_mi(i):
            yield i
        i += 1


for asal in asal_generator():
    if asal > 1000:
        break
    print(asal)
