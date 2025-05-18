# 1. Soru
i = 0
while i < 5:
    print("i'nin degeri: ", i)
    i += 1

# 2. Soru
sum = 0
for sayi in range(1, 10 + 1):
    sum += sayi
print("1'den 10'a kadar olan sayıların toplamı: ", sum)

# 3. Soru
j = int(input("Lütfen sayıyı giriniz: "))
while j > 0:
    print("Kullanıcıdan alınan sayı: ", j)
    j -= 1

# 4. soru
liste = list(range(2, 11, 2))
print("Liste olarak yazdırılması: ", liste)

# 5. Soru
while True:
    kelime = input("Lütfen kelimeyi giriniz (çıkmak için (exit)): ")
    if kelime == "exit":
        break
    else:
        print("Devam ediyor...")
