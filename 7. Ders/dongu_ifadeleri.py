# while
# i = 0
# while i < 20:
#     print(i)
#     if i == 10:
#         break
#     i += 1

# print("Program bitiyor")

# demet = (1, 2, 3, 4, 5, 6, 7)
# for i in demet:
#     if i == 5:
#         break
#     print(i)

# while True:
#     isim = input("İsminizi giriniz: (çıkmak için q tuşuna basınız) ")
#     if isim == "q":
#         print("Programdan çıkılıyor...")
#         break
#     print("Merhaba ", isim)

# continue
# liste = [1, 2, 3, 4, 5, 6, 7, 8]
# for i in liste:
#     if i == 3 or i == 5:
#         continue
#     print("i: ", i)

i = 0
while i < 10:
    if i == 2:
        continue
    print("i: ", i)
i += 1
