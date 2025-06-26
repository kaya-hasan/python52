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

    return isim, harf, harf != "FF"


with open("dosya.txt", "r", encoding="utf-8") as file:
    eklenecekler_listesi = []
    gecenler_listesi = []
    kalanlar_listesi = []
    for satir in file:
        isim, harf, gecti_mi = not_hesapla(satir)
        sonuc = f"{isim} ------> {harf}\n"
        eklenecekler_listesi.append(sonuc)
        if gecti_mi:
            gecenler_listesi.append(sonuc)
        else:
            kalanlar_listesi.append(sonuc)

with open("harf_notu.txt", "w", encoding="utf-8") as file2:
    file2.writelines(eklenecekler_listesi)

with open("gecenler.txt", "w", encoding="utf-8") as file3:
    file3.writelines(gecenler_listesi)

with open("kalanlar.txt", "w", encoding="utf-8") as file4:
    file4.writelines(kalanlar_listesi)
