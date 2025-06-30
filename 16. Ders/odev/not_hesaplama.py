def not_hesapla(satir):
    satir = satir[:-1]
    liste = satir.split(",")
    print(liste)
    isim = liste[0]
    vize1 = liste[1]
    vize2 = liste[2]
    final = liste[3]
    not_ortalama = int(vize1) * 3/10 + int(vize2) * 3/10 + int(final) * 4/10
    if not_ortalama >= 90:
        harf = "AA"
    elif not_ortalama >= 85:
        harf = "BA"
    elif not_ortalama >= 80:
        harf = "BB"
    elif not_ortalama >= 70:
        harf = "CB"
    elif not_ortalama >= 55:
        harf = "CC"
    else:
        harf = "FF"

    return isim + "------>" + harf + "\n"


with open("dosya.txt", "r", encoding="utf-8") as file:
    kalanlar_listesi = []
    gecenler_listesi = []
    for satir in file:
        cikti = not_hesapla(satir)
        harf_notu = cikti[-3:-1]
        if harf_notu == "FF":
            kalanlar_listesi.append(cikti)
        else:
            gecenler_listesi.append(cikti)
    print("geçenler listesi: ")
    print(gecenler_listesi)
    print("kalanlar listesi: ")
    print(kalanlar_listesi)

with open("kalanlar_listesi.txt", "w", encoding="utf-8") as file2:
    file2.writelines(kalanlar_listesi)
with open("gecenler_listesi.txt", "w", encoding="utf-8") as file3:
    file3.writelines(gecenler_listesi)
