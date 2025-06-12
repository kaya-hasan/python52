import random
import time

print("""
Sayı Tahmin Oyunu
      
1 ile 100 arasındaki sayıyı tahmin edin
"""
      )

rastgele_sayi = random.randint(1, 100)
tahmin_hakki = 10

while True:
    tahmin = int(input("Tahmininizi giriniz: "))
    if tahmin < rastgele_sayi:
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Sayı tahmininizden daha büyük")
        tahmin_hakki -= 1
    elif tahmin > rastgele_sayi:
        print("Bilgiler sorgulanıyor....")
        time.sleep(1)
        print("Sayı tahmininizden daha küçük")
        tahmin_hakki -= 1
    else:
        print("Tebrikler, doğru tahmin ettiniz, Sayı = ", rastgele_sayi)
        break
    if tahmin_hakki == 0:
        print("Tahmin hakkınız bitti...")
        print("Doğru sayı: ", rastgele_sayi)
        break
    print("Kalan tahmin hakkınız: ", tahmin_hakki)
