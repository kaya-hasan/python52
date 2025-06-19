import random
import time


class Kumanda:
    def __init__(self, tv_durum="Kapalı", tv_ses=0, kanal_liste=["Trt"], kanal="Trt"):
        self.tv_durum = tv_durum
        self.tv_ses = tv_ses
        self.kanal_liste = kanal_liste
        self.kanal = kanal

    def tv_ac(self):
        if self.tv_durum == "Açık":
            print("Televizyon zaten açık...")
        else:
            print("Televizyon açılıyor...")
            self.tv_durum = "Açık"

    def tv_kapa(self):
        if self.tv_durum == "Kapalı":
            print("Televizyon zaten kapalı...")
        else:
            print("Televizyon kapanıyor...")
            self.tv_durum = "Kapalı"

    def ses_ayarlari(self):
        while True:
            cevap = input("Sesi Azalt: '<'\nSesi arttır: '>'\nÇıkış: çıkış")
            if cevap == "<":
                if self.tv_ses != 0:
                    self.tv_ses -= 1
                    print("Ses: ", self.tv_ses)
                else:
                    print("Ses zaten kapalı. sesi azaltamazsınız!")
            elif cevap == ">":
                if self.tv_ses != 20:
                    self.tv_ses += 1
                    print("Ses: ", self.tv_ses)
                else:
                    print("Sesimiz zaten üst sınırda. Daha fazla arttırılamaz.")
            else:
                print("Ses güncellendi: ", self.tv_ses)
                break

    def kanal_ekle(self, kanal):
        print("Kanal ekleniyor..")
        time.sleep(1)
        self.kanal_liste.append(kanal)
        print("Kanal eklendi")

    def rastgele_kanal(self):
        rastgele = random.randint(0, len(self.kanal_liste) - 1)
        self.kanal = self.kanal_liste[rastgele]
        print("Şu anki kanal", self.kanal)

    def __str__(self):
        return f"Tv Durumu: {self.tv_durum}\n Ses: {self.tv_ses}\n Kanal Listesi: {self.kanal_liste}\n Şu anki Kanal: {self.kanal}"


kumanda = Kumanda()
print("""
    Televizyon Uygulaması:
    1. Televizyonu Aç
    2. Televizyonu Kapat
    3. Ses Ayarları
    4. Kanal Ekle
    5. Rastgele Kanal
    6. Televizyon Bilgileri
      
    Çıkmak için q'ya basın.
      
""")

while True:
    islem = input("Yapmak istediğiniz işlemi seçin: ")
    if islem == "q":
        print("Program sonlandırılıyor")
        break
    elif islem == "1":
        kumanda.tv_ac()
    elif islem == "2":
        kumanda.tv_kapa()
    elif islem == "3":
        kumanda.ses_ayarlari()
    elif islem == "4":
        kanal_isimleri = input("Kanal isimleri: (',' ile ayırarak veriniz)")
        kanal_listesi = kanal_isimleri.split(",")
        for eklenecek_kanal in kanal_listesi:
            kumanda.kanal_ekle(eklenecek_kanal)
    elif islem == "5":
        kumanda.rastgele_kanal()
    elif islem == "6":
        print(kumanda)
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyin.")
