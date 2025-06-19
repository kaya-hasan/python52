# class Bilgisayar:
#     def __init__(self, marka, model, ram, depolama):
#         # constructor method
#         # attributes - özellikler
#         self.marka = marka
#         self.model = model
#         self.ram = ram
#         self.depolama = depolama
#         self.acik = False

#     def ac(self):
#         if not self.acik:
#             self.acik = True
#             print(
#                 f"{self.marka} - {self.model} bilgisayarınız açıldı. Kullanıma hazır.")
#         else:
#             print(f"Bilgisayarınız zaten açık.")

#     def kapa(self):
#         if self.acik:
#             self.acik = False
#             print(f"{self.marka} - {self.model} bilgisayarınız kapatıldı.")
#         else:
#             print(f"Bilgisayarınız zaten kapalı.")

#     def bilgileri_goster(self):
#         durum = ""
#         if self.acik:
#             durum = "Açık"
#         else:
#             durum = "Kapalı"
#         print(f"""
#         Marka: {self.marka}
#         Model: {self.model}
#         Ram: {self.ram}
#         Depolama: {self.depolama}
#         Durum: {durum}
#         """
#               )

#     def __str__(self):
#         return f"{self. marka} - {self.model} - ({self.ram}, Depolama: {self.depolama})"

#     def __del__(self):
#         print(f"{self.marka} - {self.model} bilgisayar silindi")

#     def __len__(self):
#         return int(self.ram[:2])


# pc1 = Bilgisayar("Lenovo", "MT-313", "16 GB", "512 GB")
# pc2 = Bilgisayar("Samsung", "Skyline-7", "32 GB", "1 TB")
# pc3 = Bilgisayar("Apple", "MacBook5", "32GB", "512 GB")

# print("PC 1 Bilgileri")
# pc1.bilgileri_goster()

# print("PC 2 Bilgileri")
# pc2.bilgileri_goster()

# pc1.ac()
# pc2.ac()
# print("PC 1 Bilgileri")
# pc1.bilgileri_goster()
# print("PC 2 Bilgileri")
# pc2.bilgileri_goster()

# pc1.kapa()
# print("PC 1 Bilgileri")
# pc1.bilgileri_goster()

# print(pc1)
# print(pc2)
# print(len(pc1))
# print(len(pc2))


# Soru 2 Çözüm
class Hayvan:
    # Super Class - Parent Class
    def __init__(self, isim, yas, ayak_sayisi):
        self.isim = isim
        self.yas = yas
        self.ayak_sayisi = ayak_sayisi

    def ses_cikar(self):
        return "Bilinmeyen ses"

    def yemek_ye(self):
        return f"{self.isim} yemek yiyor."

    def bilgileri_goster(self):
        return f"İsim: {self.isim}, Yaş: {self.yas}, Ayak Sayısı: {self.ayak_sayisi}"


class Kopek(Hayvan):
    def __init__(self, isim, yas, ayak_sayisi, cins):
        super().__init__(isim, yas, ayak_sayisi)
        self.cins = cins

    def ses_cikar(self):
        return "Hav hav"

    def kuyruk_salla(self):
        return f"{self.isim} kuyruğunu sallıyor."

    def bilgileri_goster(self):
        # override
        return super().bilgileri_goster() + " Cins: " + self.cins


class Kus(Hayvan):
    # inheritance
    def __init__(self, isim, yas, ayak_sayisi, kanat_uzunlugu):
        super().__init__(isim, yas, ayak_sayisi)
        self.kanat_uzunlugu = kanat_uzunlugu

    def ses_cikar(self):
        # override
        return "Cik cik"

    def uc(self):
        return f"{self.isim} uçuyor."

    def bilgileri_goster(self):
        # override
        return super().bilgileri_goster() + " Kanat Uzunlugu: " + str(self.kanat_uzunlugu)


class At(Hayvan):
    def __init__(self, isim, yas, ayak_sayisi, hiz):
        super().__init__(isim, yas, ayak_sayisi)
        self.hiz = hiz

    def ses_cikar(self):
        # override
        return "İhihihihihi"

    def kos(self):
        return f"{self.isim} koşuyor."

    def bilgileri_goster(self):
        # override
        return super().bilgileri_goster() + " Hız(km/sa): " + str(self.hiz)


kopek1 = Kopek("Karabaş", 3, 4, "Doberman")
kopek2 = Kopek("Sungur", 2, 4, "Kangal")
kus1 = Kus("Tweety", 2, 2, 10)
kus2 = Kus("Boncuk", 1, 2, 7)
at1 = At("Bold Pilot", 4, 4, 50)
at2 = At("Şampiyon", 5, 4, 30)


print(kopek1.bilgileri_goster())
print(kopek2.bilgileri_goster())
print(kopek1.kuyruk_salla())
print(kopek2.kuyruk_salla())
print(kopek1.ses_cikar())
print(kopek1.ses_cikar())

print(kus1.bilgileri_goster())
print(kus2.bilgileri_goster())
print(kus1.uc())
print(kus2.uc())
print(kus1.ses_cikar())
print(kus2.ses_cikar())

print(at1.bilgileri_goster())
print(at2.bilgileri_goster())
print(at1.ses_cikar())
print(at2.ses_cikar())
print(at1.kos())
print(at2.kos())
