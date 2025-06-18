from Hayvan import Hayvan


class Kopek(Hayvan):
    def __init__(self, isim, yas, tur, agirlik, renk, boyut, havlama_tipi, cins):
        super().__init__(isim, yas, tur, agirlik, renk)
        print("Köpek sınıfının init fonksiyonu çalıştı")
        self.boyut = boyut
        self.havlama_tipi = havlama_tipi
        self.cins = cins

    def __str__(self):
        return super().__str__() + f"\n Boyut: {self.boyut} \n Havlama Tipi: {self.havlama_tipi} \n Cins: {self.cins}"

    def havla(self):
        return f"{self.isim} şöyle havlar {self.havlama_tipi}"
