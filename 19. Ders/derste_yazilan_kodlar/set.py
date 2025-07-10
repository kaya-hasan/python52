# set - küme
# x = set()  # boş küme
# print(type(x))

# liste = [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(liste)

# kume = set(liste)  # küme oluşturma
# print("kümemiz: ", kume)  # küme elemanları benzersizdir

# iterable her türlü objeden set oluşturulabilir

# kume = set("Python Programlama Dili")
# print(kume)

# kume = {"Python", "Php", "Python", "Java"}
# print(kume)

# sırasız bir veri tipidir
# kume = {"Python", "Php", "Java", "C#", "C", "javascript"}
# print(kume)

# for i in kume:
#     print(i)

# print(kume[0])

# kume = {"Python", "Php", "Java", "C#", "C", "javascript"}
# liste = list(kume)
# print(liste)
# print(liste[0])
# print(liste[1])

# add() - eleman ekleme
# kume = {1, 2, 3, 4, 5, 6}
# kume.add(77)
# print(kume)

# iki kümenin farkı : difference()
# kume1 = {1, 2, 3, 4, 5, 6}
# kume2 = {4, 5, 6, 7, 8, 9, 10}

# # kume1 - kume2
# print(kume1.difference(kume2))

# difference_update() - iki kümenin farkını güncelleme
# kume1 = {1, 2, 3, 4, 5, 6}
# kume2 = {4, 5, 6, 7, 8, 9, 10}

# kume1.difference_update(kume2)
# print(kume1)

# discard() - eleman çıkarma
# kume1 = {1, 2, 3, 4, 5, 6, 7}
# kume1.discard(3)  # 7 elemanını çıkarır
# kume1.discard(100)
# print(kume1)

# küme kesişimleri - intersection()
# kume1 = {1, 2, 3, 4, 5, 6}
# kume2 = {4, 5, 6, 7, 8, 9, 10}
# kume1.intersection_update(kume2)  # kume1 kümesini kume2 ile kesiştirir
# print(kume1)
# print(kume2)
# print(kume1.intersection(kume2))  # kume1 ve kume2'nin kesişimini döndürür

# intersection_update() - küme kesişimini güncelleme
# kume1 = {1, 2, 3, 4, 5, 6}
# kume2 = {4, 5, 6, 7, 8, 9, 10}
# kume1.intersection_update(kume2)  # kume1 kümesini kume2 ile kesiştirir
# print(kume1)

# ayrık küme mi - isdisjoint()
# kume1 = {1, 2, 3, 4, 5}
# kume2 = {6, 7, 8, 9, 10}
# kume3 = {1, 11, 111, 1111}
# print(kume1.isdisjoint(kume2))  # kume1 ve kume2 ayrık kümeler mi?
# print(kume1.isdisjoint(kume3))  # kume1 ve kume3 ayrık kümeler mi?

# alt küme - issubset()
# kume1 = {1, 2, 3, 4, 5, 8}
# kume2 = {1, 2, 3, 4, 5, 6, 7}
# kume3 = {7, 77, 777}
# print(kume1.issubset(kume2))  # kume1 kume2'nin alt kümesi mi?
# print(kume1.issubset(kume3))  # kume1 kume3'ün alt kümesi mi?

# birleşim kümesi - union()
# kume1 = {1, 2, 3, 4}
# kume2 = {10, 20, 30, 40}
# print(kume1.union(kume2))  # kume1 ve kume2'nin birleşimini döndürür

# update() - birleşim kümesini güncelleme
kume1 = {1, 2, 3, 4}
kume2 = {10, 20, 30, 40}
kume1.update(kume2)  # kume1 kümesini kume2 ile günceller
print(kume1)  # kume1 kümesi artık kume2 ile birleşik
