# lambda fonksiyonlar

# liste1 = [1, 2, 3, 4, 5]
# liste2 = list()

# for i in liste1:
#     liste2.append(i)

# print(liste2)

# liste3 = [1, 2, 3, 4, 5]
# liste4 = [i for i in liste3]
# print(liste4)

# def ikiyle_carp(sayi):
#     return sayi * 2


# print(ikiyle_carp(14))

# ikiyle_carp = lambda sayi: sayi * 2

# print(ikiyle_carp(105))

# def toplama(a,b,c):
#   return a + b + c
# print(toplama(1,2,3))

# topla = lambda a,b,c: a + b + c
# print(topla(5,10,15))

# def ters_cevir(yazi):
#   return yazi[::-1]
# print(ters_cevir("Python Programlama Dili"))

# ters_cevir = lambda yazi: yazi[::-1]
# print(ters_cevir("Python Programlama Dili"))

# def cift_mi(sayi):
#   return sayi % 2 == 0

# print(cift_mi(1112))

cift_mi = lambda sayi: sayi % 2 == 0

print(cift_mi(881))