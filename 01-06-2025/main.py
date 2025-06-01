# Problem 1

def mukemmel_sayi(sayi):
    toplam = 0
    for i in range(1, sayi):
        if sayi % i == 0:
            toplam += i
    return toplam == sayi


for i in range(1, 1001):
    if mukemmel_sayi(i):
        print(i, "Mükemmel sayıdır")

# Problem 2


def ebob_bulma(sayi1, sayi2):
    i = 1
    ebob_sayisi = 1
    while (i <= sayi1 and i <= sayi2):
        if sayi1 % i == 0 and sayi2 % i == 0:
            ebob_sayisi = i
        i += 1
    return ebob_sayisi


sayi1 = int(input("Sayı1'i giriniz: "))
sayi2 = int(input("Sayi2'yi giriniz: "))
print("Girilen iki sayının ebobu: ", ebob_bulma(sayi1, sayi2))

# Problem 3


def ekok_bulma(sayi1, sayi2):
    maksimum_sayi = sayi1 * sayi2
    for i in range(1, maksimum_sayi, + 1):
        if i % sayi1 == 0 and i % sayi2 == 0:
            return i


sayi1 = int(input("Sayi1 'i giriniz: "))
sayi2 = int(input("Sayi2'yi giriniz: "))
print("Girilen Sayilarin Ekoku: ", ekok_bulma(sayi1, sayi2))


# Problem 4
onlar_dict = {
    1: "On", 2: "Yirmi", 3: "Otuz", 4: "Kırk", 5: "Elli", 6: "Altmış",
    7: "Yetmiş", 8: "Seksen", 9: "Doksan"
}

birler_dict = {
    1: "Bir", 2: "İki", 3: "Üç", 4: "Dört", 5: "Beş", 6: "Altı",
    7: "Yedi", 8: "Sekiz", 9: "Dokuz",
}


def sayi_okunusu(sayi):
    if sayi < 10 or sayi > 99:
        return "Lütfen 10–99 arası bir sayı giriniz."
    birinci_sayi = sayi % 10
    ikinci_sayi = sayi // 10

    if birinci_sayi == 0:
        return onlar_dict[ikinci_sayi]

    return onlar_dict[ikinci_sayi] + " " + birler_dict[birinci_sayi]


sayi = int(input("Sayıyı giriniz: "))
print(sayi_okunusu(sayi))


# Problem 5
def pisagor_bulma():
    pisagor_listesi = list()
    for i in range(1, 101):
        for j in range(1, 101):
            c = (i ** 2 + j ** 2) ** 0.5
            if (c == int(c)):
                pisagor_listesi.append((i, j, int(c)))

    return pisagor_listesi


for i in pisagor_bulma():
    print(i)
