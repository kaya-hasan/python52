# 1. Soru
# sayi = int(input("Lütfen bir sayı giriniz: "))
# i = 1
# toplam = 0
# while i < sayi:
#     if sayi % i == 0:
#         # pozitif tam bölenleri
#         toplam += i
#     i += 1

# if toplam == sayi:
#     print(f"{sayi} bir mükemmel sayıdır.")
# else:
#     print(f"{sayi} bir mükemmel sayı değildir.")

# 2. Soru
# sayi = input("Bir sayı giriniz: ")
# basamak_sayisi = len(sayi)
# sayi = int(sayi)
# toplam = 0
# basamak = 0
# gecici_sayi = sayi

# while gecici_sayi > 0:
#     # 12 % 10 = 2
#     basamak = gecici_sayi % 10
#     toplam += basamak ** basamak_sayisi
#     # gecici_sayi = 354 // 10 = 35 (birler basamağındaki sayı atılır)
#     gecici_sayi //= 10

# if toplam == sayi:
#     print(f"{sayi} bir Armstrong sayısıdır.")
# else:
#     print(f"{sayi} bir Armstrong sayısı değildir.")

# 3. Soru
# for i in range(1, 11):
#     print("*****************")
#     for j in range(1, 11):
#         print(f"{i} x {j} = {i * j}")

# 4. Soru
# toplam = 0
# while True:
#     sayi = input("Lütfen bir sayı giriniz (çıkmak için q'ya basınız): ")
#     if sayi == 'q':
#         print(f"Girdiğiniz sayıların toplamı: {toplam}")
#         break
#     toplam += int(sayi)

# # 5. Soru
# for i in range(1, 101):
#     if i % 3 != 0:
#         continue
#     print(i)

# 6. Soru
liste = [i for i in range(1, 101) if i % 2 == 0]
print(liste)
