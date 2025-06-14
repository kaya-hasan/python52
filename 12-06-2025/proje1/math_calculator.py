# Proje 1
# Math modülü ile hesap makinesi

import math


def karekok_al(x):
    return math.sqrt(x)


def kare_al(x):
    return math.pow(x, 2)


def sayi_ust_degere_yuvarla(x):
    return math.ceil(x)


def sayi_alt_degere_yuvarla(x):
    return math.floor(x)


def faktoriyel_al(x):
    return math.factorial(x)


def kosinus_al(x):
    return math.cos(x)


def sinus_al(x):
    return math.sin(x)


def tanjant_al(x):
    return sinus_al(x) / kosinus_al(x)


def kotanjant_al(x):
    return kosinus_al(x) / sinus_al(x)


def menu():
    print("\n--- Hesap Makinesi ---")
    print("1. Karekok Alma")
    print("2. Kare Alma")
    print("3. Üst değere Yuvarlama")
    print("4. Alt değere Yuvarlama")
    print("5. Faktöriyel Alma")
    print("6. Kosinüs Alma")
    print("7. Sinüs Alma")
    print("8. Tanjant Alma")
    print("9. Kotanjant Alma")
    print("q Çıkış")


while True:
    menu()
    secim = input("Seçiminiz: ")
    if secim == "1":
        sayi = float(input("Sayiyi giriniz: "))
        print(f"Sonuç: {karekok_al(sayi)}")
    elif secim == "2":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {kare_al(sayi)}")
    elif secim == "3":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {sayi_ust_degere_yuvarla(sayi)}")
    elif secim == "4":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {sayi_alt_degere_yuvarla(sayi)}")
    elif secim == "5":
        sayi = int(input("Sayıyı giriniz: "))
        print(f"Sonuç: {faktoriyel_al(sayi)}")
    elif secim == "6":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {kosinus_al(sayi)}")
    elif secim == "7":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {sinus_al(sayi)}")
    elif secim == "8":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {tanjant_al(sayi)}")
    elif secim == "9":
        sayi = float(input("Sayıyı giriniz: "))
        print(f"Sonuç: {kotanjant_al(sayi)}")
    elif secim == "q":
        print("Çıkış yapılıyor...")
        break
    else:
        print("Geçersiz seçim yaptınız..")
