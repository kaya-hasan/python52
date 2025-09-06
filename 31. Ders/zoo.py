"""
Hayvanat Bahçesi Yönetim Sistemi Tasarlama
1) Hayvan Sınıfı (Abstract/soyut sınıf olarak tanımla)
ortak özellikleri (isim, yas, tur)
ortak metodlar (yemekYe(), sesCikar() (soyut olarak tanımlansın))

2) Alt sınıflar:
Aslan, Fil, Kus gibi hayvan sınıfları Hayvandan türeyecek.
Her hayvanın kendine özgü sesi olacak
İstersek farklı hayvan türleri de eklenebilecek

3) Kafes sınıfı
İçinde hayvanlar tutabilmeliyiz
bir kafesin içerisinde yalnızca aynı tür hayvanlar bulunabilir.

4) Hayvanat bahçesi sınıfı
tüm kafesleri tut
yeni hayvan eklenebilmeli
hayvanların listesi ve kafeslerin listesi yazdırılabilmeli.

"""
from abc import ABC, abstractmethod
# -- Soyut Hayvan Sınıfı --


class Hayvan(ABC):
    def __init__(self, isim, yas, tur):
        self.isim = isim
        self.yas = yas
        self.tur = tur

    @abstractmethod
    def yemekYe(self):
        pass

    @abstractmethod
    def sesCikar(self):
        pass


class Aslan(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas, "Aslan")

    def sesCikar(self):
        print(f"{self.isim} kükredi!")

    def yemekYe(self):
        print(f"{self.isim} et yiyo!")


class Fil(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas, "Fil")

    def sesCikar(self):
        print(f"{self.isim} boru sesi çıkarır!")

    def yemekYe(self):
        print(f"{self.isim} ot yiyor!")


class Kafes:
    def __init__(self, tur):
        self.tur = tur
        self.hayvanlar = []

    def hayvan_ekle(self, hayvan: Hayvan):
        if hayvan.tur != self.tur:
            print(f"Bu kafese {hayvan.tur} eklenemez! Kafes türü: {self.tur}")
        else:
            self.hayvanlar.append(hayvan)

    def listele(self):
        isimler = ",".join([Hayvan.isim for Hayvan in self.hayvanlar])
        return f"Kafes ({self.tur}) : {isimler}"


class Kus(Hayvan):
    def __init__(self, isim, yas):
        super().__init__(isim, yas, "Kuş")

    def sesCikar(self):
        print(f"{self.isim} ötüyor: Cik cik!")

    def yemekYe(self):
        print(f"{self.isim} yem yiyor!")


class HayvanatBahcesi:
    def __init__(self):
        self.kafesler = []

    def hayvan_ekle(self, hayvan: Hayvan):
        # aynı tür kafes varsa ekle
        for kafes in self.kafesler:
            if kafes.tur == hayvan.tur:
                kafes.hayvan_ekle(hayvan)
                return
        # yoksa yeni kafes aç
        yeni_kafes = Kafes(hayvan.tur)
        yeni_kafes.hayvan_ekle(hayvan)
        self.kafesler.append(yeni_kafes)

    def listele(self):
        for i, kafes in enumerate(self.kafesler, 1):
            print(f"Kafes {i} -> {kafes.listele()}")


# Test Senaryosu

if __name__ == "__main__":
    aslan1 = Aslan("Max", 2)
    aslan2 = Aslan("Aslan2", 10)
    fil1 = Fil("Fil1", 5)
    kus1 = Kus("Kus1", 12)

    bahce = HayvanatBahcesi()
    bahce.hayvan_ekle(aslan1)
    bahce.hayvan_ekle(aslan2)
    bahce.hayvan_ekle(fil1)
    bahce.hayvan_ekle(kus1)

    bahce.listele()

# kafes 1 -> (ASLAN): Max, Aslan2
# kafes 2 -> Kafes (Fil) : Fil1
# kafes 3 -> Kafes (Kus) : Tweety
