def futbolcu_ayir(futbolcu):
    futbolcu = futbolcu.strip()
    liste = futbolcu.split(",")
    isim_soyisim = liste[0]
    takim = liste[1]

    if takim == "Galatasaray":
        takim = "GS"
    elif takim == "Fenerbahçe":
        takim = "FB"
    elif takim == "Beşiktaş":
        takim = "BJK"
    else:
        takim = "Diğer"

    return isim_soyisim, takim


with open("futbolcular.txt", "r", encoding="utf-8") as file:
    futbolcu_listesi = []
    for satir in file:
        futbolcu = futbolcu_ayir(satir)
        futbolcu_listesi.append(futbolcu)

with open("gs.txt", "w", encoding="utf-8") as file_gs:
    for futbolcu in futbolcu_listesi:
        if futbolcu[1] == "GS":
            file_gs.write(f"{futbolcu[0]}\n")


with open("fb.txt", "w", encoding="utf-8") as file_fb:
    for futbolcu in futbolcu_listesi:
        if futbolcu[1] == "FB":
            file_fb.write(f"{futbolcu[0]}\n")


with open("bjk.txt", "w", encoding="utf-8") as file_bjk:
    for futbolcu in futbolcu_listesi:
        if futbolcu[1] == "BJK":
            file_bjk.write(f"{futbolcu[0]}\n")


with open("diger.txt", "w", encoding="utf-8") as file_diger:
    for futbolcu in futbolcu_listesi:
        if futbolcu[1] == "Diğer":
            file_diger.write(f"{futbolcu[0]}\n")
