# proje 1 -> String içindeki harflerin frekansını (bir harfin kaç defa geçtiği) bulmaya çalışın.
text = "ProgramlamaÖdeviİleriSeviyeVeriYapılarıveObjeleripynb"
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

print(frequency)


# proje 2 - dosya işlemleri
with open("siir.txt", "r", encoding="utf-8") as file:
    first_letter = []
    for text in file:
        text = text.lstrip()
        if text:
            first_letter.append(text[0])

sonuc = "".join(first_letter)
print(sonuc)


# proje 3 - mail formatı kontrol etme
with open("mailler.txt", "r", encoding="utf-8") as file:
    for text in file:
        text = text.strip()
        if (
            text.count("@") == 1
            and " " not in text
            and text.find("@") > 0
            and "." in text.split("@")[1]
            and "xyz" not in text
            and text.lower() in text
        ):
            print(text)


# proje 4
names = ["Kerim", "Tarık", "Ezgi", "Kemal", "İlkay", "Şükran", "Merve"]
surnames = ["Yılmaz", "Öztürk", "Dağdeviren",
            "Atatürk", "Dikmen", "Kaya", "Polat"]

ordered_list = sorted(zip(names, surnames))

for names, surnames in ordered_list:
    print(f"{names} - {surnames}")
