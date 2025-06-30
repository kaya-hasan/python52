with open("futbolcular.txt", "r", encoding="utf-8") as file:
    gs = list()
    bjk = list()
    fb = list()

    for satir in file:
        satir = satir[:-1]  # Satır sonu karakterini kaldır
        satir_elemanlari = satir.split(",")
        print(satir_elemanlari[1])
        if satir_elemanlari[1] == "Fenerbahçe":
            fb.append(satir + "\n")
        elif satir_elemanlari[1] == "Beşiktaş":
            bjk.append(satir + "\n")
        else:
            gs.append(satir + "\n")

    with open("bjk.txt", "w", encoding="utf-8") as file2:
        file2.writelines(bjk)
    with open("gs.txt", "w", encoding="utf-8") as file3:
        file3.writelines(gs)
    with open("fb.txt", "w", encoding="utf-8") as file4:
        file4.writelines(fb)
