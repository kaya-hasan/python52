# if else
# a = 15
# b = 20
# c = 30
# print(a + b + c)

# girintiler - indentation
sayi = 20  # blok 1 - scope 1
# if sayi == 20:
#     print(sayi)  # blok 2 - scope 2

# print("Merhaba")  # blok 1 - scope 1
# if sayi == 30:
#     print("blok 3")
# print("Merhaba")  # blok 1 - scope 1

# yas = int(input("Yaşınızı giriniz: "))
# if yas < 18:
#     print("Mekâna giremezsiniz ")


# sayi = int(input("Bir sayı giriniz: "))
# if sayi < 0:
#     print("Negatif sayi")

# yas = int(input("Yaşınızı giriniz: "))
# if yas < 18:
#     print("Mekâna giremezsiniz ")
# else:
#     print("Mekâna hoşgeldiniz")

# if "Selcuk" != "Kemal":

#     print("eşit değil")
# if - elif - else kalıb
# islem = int(input("Bir işlem seciniz: "))

# if islem == 1:
#     print("Birinci işlem seçildi")
# elif islem == 2:
#     print("İkinci işlem seçildi")
# elif islem == 3:
#     print("Üçüncü işlem seçildi")
# else:
#     print("Geçersiz işlem...")

# yas = int(input("Yaşınızı giriniz: "))
# if yas > 7 and yas < 12:
#     print("ilkokuldasınız")
# elif yas > 11 and yas < 16:
#     print("ortaokuldasınız")
# elif yas > 15 and yas < 20:
#     print("liselisin")
# else:
#     print("Üniversitedesin...")

# if - if - if
note = float(input("Notunuzu giriniz: "))
if note >= 90:
    print("AA")
if note >= 75:
    print("BA")
if note >= 50:
    print("BB")
else:
    print("Sınıfta kaldınız.. FF")
