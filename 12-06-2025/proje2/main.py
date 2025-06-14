# Proje 2
import my_math


while True:
    my_math.menu()
    secim = input("Seçiminiz: ")
    if secim == "1":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.karekok_al(sayi)}")
    elif secim == "2":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.kare_al(sayi)}")
    elif secim == "3":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.ust_degere_yuvarla(sayi)}")
    elif secim == "4":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.alt_degere_yuvarla(sayi)}")
    elif secim == "5":
        sayi = int(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.faktoriyel_al(sayi)}")
    elif secim == "6":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.kosinus_al(sayi)}")
    elif secim == "7":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.sinus_al(sayi)}")
    elif secim == "8":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.tanjant_al(sayi)}")
    elif secim == "9":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {my_math.kotanjant_al(sayi)}")
    elif secim == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim yaptınız..")
