# Problem 1

sayi = int(input("Bir sayı girin: "))
toplam = 0

for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i

if toplam == sayi:
    print(sayi, "Sayısı mükemmel sayıdır. Tebrikler!")
else:
    print(sayi, "Sayısı mükemmel sayı değildir. Üzgünüm!")


# Problem 2
sayi = int(input("Bir sayı girin: "))
basamak_sayisi = len(str(sayi))
toplam = 0

for rakam in str(sayi):
    toplam += int(rakam) ** basamak_sayisi

if toplam == sayi:
    print(sayi, "bir Armstrong sayısıdır.")
else:
    print(sayi, "Armstrong sayısı değildir.")


# Problem 3
for i in range(1, 10):
    for j in range(1, 10):
        print(i, "X", j, "=", i * j)


# Problem 4
toplam_degiskeni = 0
while True:
    girdi = input("Sayıyı giriniz: (çıkmak için q tuşuna basın: )")
    if girdi == "q":
        print("Toplam Değişkeni: ", toplam_degiskeni)
        break
    else:
        sayi = int(girdi)
        toplam_degiskeni += sayi

# Problem 5
for i in range(1, 100):
    if i % 3 != 0:
        continue
    print("3'e bölünen sayılar: ", i)

# Problem 6
sayilar = [i for i in range(0, 100, 2)]
print(sayilar)
