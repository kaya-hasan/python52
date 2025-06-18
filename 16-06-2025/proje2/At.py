from Hayvan import Hayvan


class At(Hayvan):
    def __init__(self, isim, yas, tur, agirlik, renk, ozellik, cins, hiz):
        super().__init__(isim, yas, tur, agirlik, renk)
        print("At sınıfının init fonksiyonu çalıştı")
        self.ozellik = ozellik
        self.cins = cins
        self.hiz = hiz

    def __str__(self):
        return super().__str__() + f"\n Özellik: {self.ozellik} \n Cins {self.cins} \n Hız: {self.hiz}"

    def kos(self):
        return f"{self.isim} saatte {self.hiz} km hızla koşar"
