# kalıtım - inheritance

# class Calisan():
#     def __init__(self, isim, soyisim, maas, departman):
#         print("Çalışan sınıfının init fonksiyonu çalıştı")
#         self.isim = isim
#         self.soyisim = soyisim
#         self.maas = maas
#         self.departman = departman

#     def bilgileri_goster(self):
#         print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı")
#         print(
#             f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nMaaş: {self.maas}\nDepartman: {self.departman}")

#     def departman_degistir(self, yeni_departman):
#         print("Çalışan sınıfının departman değiştir fonksiyonu çalıştı")
#         self.departman = yeni_departman


# class Yonetici(Calisan):
#     def zam_yap(self, zam_miktari):
#         print("Maaşa zam yapılıyor...")
#         self.maas += zam_miktari


#         # object - instance - instantiate etmek - obje - nesne
# yonetici1 = Yonetici("Mehmet", "Demir", 500000, "IK")

# yonetici1.bilgileri_goster()
# yonetici1.zam_yap(88000)
# yonetici1.bilgileri_goster()

# yonetici1.departman_degistir("Yazılım")

# yonetici1.bilgileri_goster()

# print(dir(yonetici1))

# overriding (iptal etme)

class Calisan():
    def __init__(self, isim, soyisim, maas, departman):
        print("Çalışan sınıfının init fonksiyonu çalıştı")
        self.isim = isim
        self.soyisim = soyisim
        self.maas = maas
        self.departman = departman

    def bilgileri_goster(self):
        print("Çalışan sınıfının bilgileri göster fonksiyonu çalıştı")
        print(
            f"İsim: {self.isim}\nSoyisim: {self.soyisim}\nMaaş: {self.maas}\nDepartman: {self.departman}")

    def departman_degistir(self, yeni_departman):
        print("Çalışan sınıfının departman değiştir fonksiyonu çalıştı")
        self.departman = yeni_departman


class Yonetici(Calisan):
    def __init__(self, isim, soyisim, maas, departman, sorumlu_kisi_sayisi):
        # overriding (iptal etme)
        print("Yönetici sınıfının init fonksiyonu çalıştı")
        super().__init__(isim, soyisim, maas, departman)
        self.sorumlu_kisi_sayisi = sorumlu_kisi_sayisi

    def zam_yap(self, zam_miktari):
        print("Maaşa zam yapılıyor...")
        self.maas += zam_miktari

    def bilgileri_goster(self):
        # overriding (iptal etme)
        print("Yönetici Class'ının bilgileri göster fonksiyonu çalışıyor.")
        print(
            f"Yönetici İsim: {self.isim}\nYönetici Soyisim: {self.soyisim}\nYönetici Maaş: {self.maas}\nYönetici Departman: {self.departman}")

        # object - instance - instantiate etmek - obje - nesne
yonetici1 = Yonetici("Mehmet", "Demir", 500000, "IK", 10)

yonetici1.bilgileri_goster()
