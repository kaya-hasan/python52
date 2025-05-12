# beden kitle endeksi
boy = float(input("Boyunuzu giriniz (Örn: 1.75): "))
kilo = int(input("Kilonuzu giriniz (Örn: 70): "))
bki = kilo / (boy * boy)
print("Beden kitle endeksi", bki)
if bki < 18.5:
    print("Zayıf")
elif bki >= 18.5 and bki < 25:
    print("Normal")
elif bki >= 25 and bki < 30:
    print("Fazla kilolu")
elif bki > 30:
    print("Obez")


# en büyük sayıyı bulma
ilk_sayi = int(input("İlk sayınızı giriniz: "))
ikinci_sayi = int(input("İkinci sayınızı giriniz: "))
ucuncu_sayi = int(input("Üçüncü sayınızı giriniz: "))
en_buyuk_sayi = max(ilk_sayi, ikinci_sayi, ucuncu_sayi)
print(f"En büyük sayi: {en_buyuk_sayi}")

# vize1, vize2, final notlarına göre harf notu hesaplama
vize1 = int(input("Birinci vize notunuzu giriniz: "))
vize2 = int(input("İkinci vize notunuzu giriniz: "))
final = int(input("Final notunuzu giriniz: "))
sonuc = (vize1 * 0.30) + (vize2 * 0.30) + (final * 0.40)
print(sonuc, sep="\n")
if sonuc >= 90:
    print("Harf notu AA")
elif sonuc >= 85:
    print("Harf notu BA")
elif sonuc >= 80:
    print("Harf notu BB")
elif sonuc >= 75:
    print("Harf notu CB")
elif sonuc >= 70:
    print("Harf notu CC")
elif sonuc >= 65:
    print("Harf notu DC")
elif sonuc >= 60:
    print("Harf notu DD")
elif sonuc >= 55:
    print("Harf notu FD")
else:
    print("Harf notu FF")

# geometrik hesaplama
giris = int(input(
    "Üçgenin mi dörtgenin mi tipini bulmak istiyorsunuz? \n 1: Üçgen \n 2: Dörtgen \n"))
if giris == 1:
    ucgen_kenar1 = int(input("Üçgenin 1. kenar uzunluğunu giriniz: "))
    ucgen_kenar2 = int(input("Üçgenin 2. kenar uzunluğunu giriniz: "))
    ucgen_kenar3 = int(input("Üçgenin 3. kenar uzunluğunu giriniz: "))
    if ucgen_kenar1 <= 0 or ucgen_kenar2 <= 0 or ucgen_kenar3 <= 0:
        print("Geçersiz giriş! Kenarlar 0'dan büyük olmalıdır! ")
    elif not (ucgen_kenar1 + ucgen_kenar2 > ucgen_kenar3) or not (ucgen_kenar1 + ucgen_kenar3 > ucgen_kenar2) or not (ucgen_kenar2 + ucgen_kenar3 > ucgen_kenar1):
        print("Üçgen belirtmiyor!")
    elif ucgen_kenar1 == ucgen_kenar2 == ucgen_kenar3:
        print("Girdiğiniz değerler eşkenar üçgendir!")
    elif (ucgen_kenar1 == ucgen_kenar2) or (ucgen_kenar1 == ucgen_kenar3) or (ucgen_kenar2 == ucgen_kenar3):
        print("Girdiğiniz değerler ikizkenar üçgendir!")

    else:
        print("Girdiğiniz değerler çeşitkenar üçgendir!")
elif giris == 2:
    dortgen_kenar1 = int(
        input("Dörtgenin 1. kenar uzunluğunu giriniz: "))
    dortgen_kenar2 = int(
        input("Dörtgenin 2. kenar uzunluğunu giriniz: "))
    dortgen_kenar3 = int(
        input("Dörtgenin 3. kenar uzunluğunu giriniz: "))
    dortgen_kenar4 = int(
        input("Dörtgenin 4. kenar uzunluğunu giriniz: "))
    if dortgen_kenar1 <= 0 or dortgen_kenar2 <= 0 or dortgen_kenar3 <= 0 or dortgen_kenar4 <= 0:
        print("Geçersiz giriş! Kenarlar 0'dan büyük olmalıdır!")
    elif dortgen_kenar1 == dortgen_kenar3 and dortgen_kenar2 == dortgen_kenar4:
        print("Bu bir kare!")
    elif dortgen_kenar1 == dortgen_kenar2 == dortgen_kenar3 == dortgen_kenar4:
        print("Bu bir eşkenar dörtgen!")
    else:
        print("Çeşitkenar dörtgen!")
