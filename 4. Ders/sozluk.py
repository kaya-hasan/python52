# dictionary - sözlükler
# key - value
# anahtar-deger
# free(key)-özgürlük(value)

# sozluk1 = {"freedom": "özgürlük", "horse": "at", "house": "ev"}
# print(sozluk1)

# sozluk1 = {}
# print(sozluk1)

# sozluk1 = dict()
# print(sozluk1)

# sozluk1 = {"freedom": "özgürlük", "horse": "at", "house": "ev"}
# # sozluk degerlerine ulasmak
# print(sozluk1["man"])

# farkli veri tipleri tutulabilir
# sozluk1 = {"bir": [1, 2, 3, 4], "iki": [[1, 2], [3, 4], [5, 6]], "üç": 15}
# sozluk1["iki"][2][1] += 10
# print(sozluk1["iki"][2][1])

# sozluk1 = {"freedom": "özgürlük", "horse": "at", "house": "ev"}
# sozluk1["man"] = "adam"
# print(sozluk1)

# iç içe sözlük
# sozluk = {"sayilar": {"bir": 1, "iki": 2, "üç": 3}, "meyveler": {
#     "kiraz": "yaz", "portakal": "kış", "erik": "yaz"}}
# # print(sozluk["sayilar"]["üç"])
# print(sozluk["meyveler"]["portakal"])

# sozluk1 = {"freedom": "özgürlük", "horse": "at", "house": "ev"}
# print(sozluk1.values())  # value tarafındaki degerler yazdirilir
# value tarafındaki degerler listeye dönüştürülür
# print(list(sozluk1.values()))

sozluk1 = {"freedom1": "özgürlük", "horse": "at", "house": "ev",
           "freedom2": "özgürlük", "horse": "at", "house": "ev",
           "freedom3": "özgürlük", "horse": "at", "house": "ev",
           "freedom4": "özgürlük", "horse": "at", "house": "ev",
           "freedom5": "özgürlük", "horse": "at", "house": "ev",
           "freedom6": "özgürlük", "horse": "at", "house": "ev",
           "freedom7": "özgürlük", "horse": "at", "house": "ev",
           "freedom8": "özgürlük", "horse": "at", "house": "ev"}
# print(sozluk1)
# print(list(sozluk1.values()))
# print(sozluk1.keys())  # key tarafındaki degerler yazdirilir
print(sozluk1.items())
