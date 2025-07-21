from kutuphane import *


kutuphane = Kutuphane()
while True:
    print("""
  ******************************************
        
        Kütüphane Programına Hoş Geldiniz.
        İşlemler;
        1. Kitapları Göster
        2. Kitap sorgulama
        3. Kitap Ekle
        4. Kitap Sil
        5. Baskı Yükselt

        Çıkmak için de 'q' ya basabilirsiniz.

  ******************************************
  """
          )
    islem = input("Yapacağınız işlem: ")
    if islem == "q":
        print("Program sonlandırılıyor...")
        break
    elif islem == "1":
        kutuphane.kitaplari_goster()
    elif islem == "2":
        isim = input("Hangi kitabı sorgulamak istiyorsunuz: ")
        print("Sorgulanıyor...")
        time.sleep(2)
        kutuphane.kitaplari_sorgula(isim)
    elif islem == "3":
        isim = input("İsim: ")
        yazar = input("Yazar: ")
        yayinevi = input("Yayınevi: ")
        tur = input("Tür: ")
        baski = int(input("Baskı sayısı: "))
        yeni_kitap = Kitap(isim, yazar, yayinevi, tur, baski)
        print("Kitap ekleniyor...")
        time.sleep(2)
        kutuphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi....")
    elif islem == "4":
        isim = input("Hangi kitabı silmek istiyorsunuz: ")
        cevap = input("Emin misiniz? (e/h): ")
        if cevap == "e":
            print("Kitap siliniyor...")
            time.sleep(2)
            kutuphane.kitap_sil(isim)
            print("Kitap silindi...")
    elif islem == "5":
        isim = input("Hangi kitabın baskı sayısını yükseltmek istiyorsunuz: ")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kutuphane.baski_yukselt(isim)
        print("Baskı yükseltildi...")
    else:
        print("Geçersiz işlem...")
