# list comprehension
# liste = [1, 2, 3, 4]
# liste.append(5)
# print(liste)

# liste1 = [1, 2, 3, 4, 5]
# liste2 = []
# for i in liste1:
#     liste2.append(i)
# print(liste2)

# liste1 = [1, 2, 3, 4, 5]
# liste2 = [i*3 for i in liste1]  # list comprehension
# print("liste2: ", liste2)

# liste1 = [(1, 2), (3, 4), (5, 6)]
# for i, j in liste1:
#     print("i: ", i, " j: ", j, "bu değerlerin çarpımı: ", i * j)

# liste2 = [i * j for i, j in liste1]
# print(liste2)

# liste1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# liste2 = [i for i in liste1 if not ((i == 4 or i == 9))]
# print(liste2)

# yazi = "Python"

# liste = [i * 3 for i in yazi]
# print(liste)

liste = [[1, 2, 3,], [4, 5, 6, 7, 8], [9, 10, 11, 12, 13, 14, 15]]
# yeni_liste = [1, 2, 3, 4, 5, 6, 7, 8, ......., 15]

yeni_liste = list()
for i in liste:
    for x in i:
        print("x: ", x)
        yeni_liste.append(x)
print(yeni_liste)

yeni_liste_lc = [x for i in liste for x in i]
print("yeni_liste_lc: ", yeni_liste_lc)
