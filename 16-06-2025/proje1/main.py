class Bilgisayar:
    def __init__(self, marka, model, ram, disk, isletim_sistemi):
        print("Bilgisayar sınıfının init fonksiyonu çalıştı")
        self.marka = marka
        self.model = model
        self.ram = ram
        self.disk = disk
        self.isletim_sistemi = isletim_sistemi

    def __str__(self):
        return f"Marka: {self.marka}\n Model: {self.model}\n Ram: {self.ram} \n Disk: {self.disk} \n Isletim Sistemi: {self.isletim_sistemi}"

    def __len__(self):
        return self.ram


class OzellikGuncelle(Bilgisayar):
    def __init__(self, marka, model, ram, disk, isletim_sistemi, ekran_boyut):
        super().__init__(marka, model, ram, disk, isletim_sistemi)
        print("Ozellik güncelleme sınıfının init fonksiyonu çalıştı")
        self.ekran_boyut = ekran_boyut

    def __str__(self):
        return super().__str__() + f"\nEkran Boyut: {self.ekran_boyut}"

    def ram_guncelle(self, ram_guncelleme):
        print("Ram güncelleniyor")
        self.ram += ram_guncelleme


bilgisayar = Bilgisayar("Apple", "Macbook M2 Air", 8, 128, "Macintosh")
print(bilgisayar)

print("---------------------------------------")

ozellik_guncelle = OzellikGuncelle(
    "Apple", "Macbook M3", 12, 256, "Macintosh Pro", "15 inch")

print(ozellik_guncelle)

print("---------------------------------------")

rami_yukselt = OzellikGuncelle(
    "Lenovo", "All In One Pc", 16, 256, "Windows", "20 inch")

print(rami_yukselt)

print("---------------------------------------")

rami_yukselt.ram_guncelle(16)
print(rami_yukselt)
