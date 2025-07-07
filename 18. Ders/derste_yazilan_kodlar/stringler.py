# upper() - lower()
# yazi = "PythoN NoVa AkadEmi"
# print(yazi.upper())  # Tüm harfleri büyük yapar
# print(yazi.lower())  # Tüm harfleri küçük yapar

# replace
# print(yazi.replace("d", "oooooo"))  # Belirli bir kelimeyi değiştirir

# startwith() - endswith()
# print(yazi.startswith("P"))  # Başlangıç harfini kontrol eder
# print(yazi.endswith("i"))  # Bitiş harfini kontrol eder
# print(yazi.endswith("i."))

# split() - kelimeleri ayırır
# print(yazi.split("---"))

# strip() - lstrip() - rstrip()

# yazi = "                  hasan kaya                   "
# print(yazi.strip())  # Başındaki ve sonundaki boşlukları siler

# yazi = "XXXXXXXXhasan kayaXXXXXXXXXXX"
# print(yazi.strip("X"))  # Başındaki ve sonundaki X'leri siler
# print(yazi.lstrip("X"))  # Sadece başındaki X'leri siler
# print(yazi.rstrip("X"))  # Sadece sonundaki X'leri siler


# join() - listeyi birleştirir
# liste = ["21", "02", "2025"]
# tarih = "/".join(liste)
# print(tarih)

# liste = ["T", "B", "M", "M"]
# print(".".join(liste))

# count() - belirli bir kelimenin kaç kez geçtiğini sayar
yazi = "türkiye büyük millet meclisinde türkiye ile ilgili konular türkiye de görev yapan milletvekilleri ile görüşülür"
# print(yazi.count("türkiye"))
# print(yazi.count("türkiye", 8))
# find() - rfind() - belirli bir kelimenin ilk geçtiği yeri bulur
# print(yazi.rfind("millet"))
print(yazi.find("millet", 20))
