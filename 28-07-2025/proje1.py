class Kareler:
    def __init__(self, maksimum):
        self.maksimum = maksimum
        self.kare = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.kare <= self.maksimum:
            sonuc = self.kare ** 2
            self.kare += 1
            return sonuc
        else:
            self.kare = 0
            raise StopIteration


kare = Kareler(3)
iterator = iter(kare)
print(next(iterator))  # 0
print(next(iterator))  # 1
print(next(iterator))  # 4
print(next(iterator))  # 9
print(next(iterator))  # StopIteration raised here
