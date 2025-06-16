# magical method - dunder method - özel method
# __init__() - constructor - yapıcı metod

# class Kitap():
#     pass


# kitap = Kitap()  # init metodumuz tetikleniyor

# del kitap  # del anahtar kelimesi bir objeyi siler ve __del__() metodu çalışır

# print(kitap)

# print(len(kitap))

# liste = list()

# print(len(liste))

class Kitap:
    def __init__(self, isim, yazar, sayfa_sayisi, tur):
        print("Kitap objesi oluşturuluyor...")
        self.isim = isim
        self.yazar = yazar
        self.sayfa_sayisi = sayfa_sayisi
        self.tur = tur

    def __str__(self):
        return f"Isim: {self.isim}\nYazar: {self.yazar}\nSayfa Sayısı: {self.sayfa_sayisi}\nTür: {self.tur}"

    def __len__(self):
        return self.sayfa_sayisi

    def __del__(self):
        print("Kitap objesi siliniyor...")


kitap1 = Kitap("İstanbul Hatırası", "Ahmet Ümit", 561, "Polisiye")

# print(kitap1)
# print(len(kitap1))

del kitap1
print(kitap1)
