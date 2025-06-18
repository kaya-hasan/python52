class Hayvan:
    def __init__(self, isim, yas, tur, agirlik, renk):
        print("Hayvan sınıfının init fonksiyonu çalıştı")
        self.isim = isim
        self.yas = yas
        self.tur = tur
        self.agirlik = agirlik
        self.renk = renk

    def __str__(self):
        return f"Isim: {self.isim}\n Yaş: {self.yas} \n Tür: {self.tur} \n Ağırlık: {self.agirlik} \n Renk: {self.renk}"

    def ses_cikar(self, ses):
        return f"{self.isim} şöyle ses çıkarır: {ses}"

    def hareket_et(self, hareket):
        return f"{self.isim} şöyle hareket eder {hareket}"
