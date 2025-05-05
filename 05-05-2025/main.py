print("Bir sayının tek mi çift mi olduğunu nasıl kontrol edersin?")
number = int(input("Lütfen bir sayı giriniz: "))
if number % 2 == 0:
    print("Bu sayı çifttir")
elif number % 2 == 1:
    print("Bu sayı tektir")

print("----------------------------------------------------")

print("Kullanıcıdan alınan iki sayının toplamını ekrana yazdıran bir Python programı yaz.")
sayi1 = int(input("Lütfen ilk sayiyi giriniz: "))
sayi2 = int(input("Lütfen ikinci sayiyi giriniz: "))
toplam = sayi1 + sayi2
print(sayi1, sayi2, "toplami: ", toplam)

print("----------------------------------------------------")

print("Bir string'in kaç karakterden oluştuğunu bulan kodu yaz.")
karakter = str(input("Lütfen kelime giriniz: "))
print(karakter, "kelimesinin uzunluğu: ", len(karakter))

print("----------------------------------------------------")

print("Bir string'i tersten yazdıran bir Python programı yaz.")
kelime = str(input("Lütfen tersten yazdırılacak kelimeyi giriniz: "))
print(kelime, "kelimesinin tersten yazdırılmış hâli: ", kelime[::-1])


print("----------------------------------------------------")

print("Bir cümlede kaç tane kelime olduğunu bulan kodu yaz.")
cumle = str(input("Lütfen cümleyi giriniz: "))
print(cumle, "cümlesinde", len(cumle.split()), "kelime vardir")
