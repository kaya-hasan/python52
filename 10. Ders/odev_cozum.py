# 1. Soru çözümü
# def mukemmel(sayi):
#     toplam = 0
#     for i in range(1, sayi):
#         if sayi % i == 0:
#             toplam += i
#     return toplam == sayi


# for i in range(1, 1001):
#     if mukemmel(i):
#         print("Mükemmel sayı: ", i)

# # 2. Soru Çözümü


# def ebob_bulma(sayi1, sayi2):
#     i = 1
#     ebob = 1
#     while i <= sayi1 and i <= sayi2:
#         if not (sayi1 % i) and not (sayi2 % i):
#             ebob = i
#         i += 1
#     return ebob


# sayi1 = int(input("Sayı-1: "))
# sayi2 = int(input("Sayı-2: "))
# print("Ebob: ", ebob_bulma(sayi1, sayi2))

# 3. Soru Çözümü
# def ekok_bulma(sayi1, sayi2):
#     i = 2
#     ekok = 1
#     while True:
#         if sayi1 % i == 0 and sayi2 % i == 0:
#             ekok *= i
#             sayi1 //= i
#             sayi2 //= i
#         elif sayi1 % i == 0 and sayi2 % i != 0:
#             ekok *= i
#             sayi1 //= i
#         elif sayi1 % i != 0 and sayi2 % i == 0:
#             ekok *= i
#             sayi2 //= i
#         else:
#             i += 1
#         if sayi1 == 1 and sayi2 == 1:
#             break
#     return ekok


# sayi1 = int(input("Sayı-1: "))
# sayi2 = int(input("Sayı-2: "))
# print("Ekok: ", ekok_bulma(sayi1, sayi2))

# 4. Soru Çözümü
# birler = ["", "Bir", "İki", "Üç", "Dört",
#           "Beş", "Altı", "Yedi", "Sekiz", "Dokuz"]

# onlar = ["", "On", "Yirmi", "Otuz", "Kırk", "Elli",
#          "Altmış", "Yetmiş", "Seksen", "Doksan"]


# def okunus(sayi):
#     birinci = sayi % 10
#     ikinci = sayi // 10
#     return onlar[ikinci] + " " + birler[birinci]


# sayi = int(input("Sayı: "))
# print(okunus(sayi))

# 5. Soru Çözümü
def pisagor_bul():
    pisagor_listesi = list()
    for a in range(1, 101):
        for b in range(1, 101):
            c = (a ** 2 + b ** 2) ** 0.5
            if c == int(c):
                pisagor_listesi.append([a, b, int(c)])
    return pisagor_listesi


for i in pisagor_bul():
    print(i)
