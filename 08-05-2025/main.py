print("------------------------")
sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
sayi3 = int(input("Üçüncü sayıyı girin: "))
print("{} * {} * {} = {}".format(sayi1, sayi2, sayi3, sayi1 * sayi2 * sayi3))

print("------------------------")

kilo = float(input("Lütfen kilonuzu giriniz: (örnek: 1.75)"))
boy = int(input("Lütfen boyunuzu giriniz: "))
print(kilo / (boy * boy))

print("------------------------")

kilometre = int(input("Lütfen kaç km yol yaptığınızı giriniz: "))
yakit = float(input("Kilometrede ne kadar yakıt harcıyorsunuz? (1.5): "))
print("Toplam tutar: {} tl dir.".format(kilometre * yakit))

print("------------------------")

ad = str(input("Lütfen adinizi giriniz: "))
soyad = str(input("Lütfen soyadinizi giriniz: "))
numara = str(input("Lütfen numaranizi giriniz: "))
print("Adınız ve Soyadınız: ", ad, soyad, numara, sep="\n")

print("------------------------")

deger1 = int(input("Lütfen ilk sayınızı giriniz: "))
deger2 = int(input("Lütfen ikinci sayınızı giriniz: "))
deger1, deger2 = deger2, deger1
print("Degerlerin birbiriyle degisimi: ", deger1, deger2)

print("------------------------")

# hipotenüs

kisakenar = float(input("Kisa kenar uzunlugunu giriniz: "))
uzunkenar = float(input("Uzun kenar uzunluğunu giriniz: "))
hipotenus = (kisakenar ** 2) + (uzunkenar ** 2) * 0.5
print("Hipotenus: ", hipotenus)
