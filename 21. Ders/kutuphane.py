import sqlite3
import time


class Kitap:
    def __init__(self, isim, yazar, yayinevi, tur, baski):
        # constructor
        # attributes
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tur = tur
        self.baski = baski

    def __str__(self):
        return f"Kitap ismi: {self.isim}\nYazar: {self.yazar}\nYayınevi: {self.yayinevi}\nTür: {self.tur}\nBaskı: {self.baski}"


class Kutuphane:
    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("nova_kutuphane.db")
        self.cursor = self.baglanti.cursor()
        sorgu = "CREATE TABLE IF NOT EXISTS kitaplar (isim TEXT, yazar TEXT, yayinevi TEXT, tur TEXT, baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        sorgu = "SELECT * FROM kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Kütüphanede hiçbir kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0], i[1], i[2], i[3], i[4])
                print(kitap)

    def kitaplari_sorgula(self, isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Aradığınız kitap bulunamadı...")
        else:
            kitap = Kitap(kitaplar[0][0], kitaplar[0][1],
                          kitaplar[0][2], kitaplar[0][3], kitaplar[0][4])
            print(kitap)

    def kitap_ekle(self, kitap):
        sorgu = "INSERT INTO kitaplar VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sorgu, (kitap.isim, kitap.yazar,
                                    kitap.yayinevi, kitap.tur, kitap.baski))
        self.baglanti.commit()

    def kitap_sil(self, isim):
        sorgu = "DELETE FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        self.baglanti.commit()

    def baski_yukselt(self, isim):
        sorgu = "SELECT * FROM kitaplar WHERE isim = ?"
        self.cursor.execute(sorgu, (isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar) == 0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4] + 1
            baski += 1
            sorgu2 = "UPDATE kitaplar SET baski = ? WHERE isim = ?"
            self.cursor.execute(sorgu2, (baski, isim))
            self.baglanti.commit()
