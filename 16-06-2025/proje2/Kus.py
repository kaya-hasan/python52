from Hayvan import Hayvan


class Kus(Hayvan):
    def __init__(self, isim, yas, tur, agirlik, renk, kanat_uzunlugu, ucabilir_mi, konusabilir_mi):
        super().__init__(isim, yas, tur, agirlik, renk)
        print("Kuş sınıfının init fonksiyonu çalıştı")
        self.kanat_uzunlugu = kanat_uzunlugu
        self.ucabilir_mi = ucabilir_mi
        self.konusabilir_mi = konusabilir_mi

    def __str__(self):
        return super().__str__() + f"\n Kanat Uzunluğu: {self.kanat_uzunlugu} \n Uçabilir Mi: {self.ucabilir_mi} \n Konuşabilir Mi: {self.konusabilir_mi}"
