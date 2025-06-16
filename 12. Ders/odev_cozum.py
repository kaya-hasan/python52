import math
import modul1


def hesap_makinesi():
    print("""
      Gelişmiş Hesap Makinesi - Math Modülü ile
        1. Karekök Alma
        2. Üs Alma
        3. Sinüs Alma
        4. Cosinüs Alma
        5. 10 tabanında Logaritma hesabı
        6. Kendi faktöriyel fonksiyonunu çalıştır
        7. Kendi karekök alma fonksiyonunu çalıştır
        8. Kendi üs alma fonksiyonunu çalıştır
          

""")
    secim = input("Lütfen yapmak istediğiniz işlemi seçiniz (1-5): ")
    if secim == "1":
        sayi = float(input("Karekökünü almak istediğiniz sayi: "))
        print("Bu sayının karekökü: ", math.sqrt(sayi))
    elif secim == "2":
        taban = int(input("Taban: "))
        us = int(input("Üs: "))
        print("Girilen değerler ile yapılan üst hesaplamasının sonucu: ",
              math.pow(taban, us))
    elif secim == "3":
        aci = int(input("Sinüsünü hesaplayacağımız açı değerini gir: "))
        print("Girilen açının sinüs değeri: ", math.sin(aci))
    elif secim == "4":
        aci = int(input("Cosinüsünü hesaplayacağımız açı değerini gir: "))
        print("Girilen açının cosinüs değeri: ", math.cos(aci))
    elif secim == "5":
        sayi = int(input("10 tabanında logaritması alınacak sayıyı giriniz: "))
        print("Log10 değeri: ", math.log10(sayi))
    elif secim == "6":
        sayi = int(input("Faktöriyeli alınacak sayı: "))
        print("Girilen sayının faktöriyeli: ", modul1.factoriyel(sayi))
    elif secim == "7":
        sayi = float(input("Karekökünü almak istediğiniz sayi: "))
        print("Bu sayının karekökü: ", modul1.my_sqrt(sayi))
    elif secim == "8":
        taban = int(input("Taban: "))
        us = int(input("Üs: "))
        print("Girilen değerler ile yapılan üst hesaplamasının sonucu: ",
              modul1.my_pow(taban, us))
    else:
        print("Yanlış seçim yaptınız...")


while True:
    devam_mi = input(
        "Yeni bir hesap makinesi işlemi yapmak ister misiniz? (e/h): ")
    if devam_mi == "e":
        hesap_makinesi()
    else:
        print("Hesap makinesi kapatılıyor...")
        break
