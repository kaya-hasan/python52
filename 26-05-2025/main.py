print("Problem 1")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

liste = [i*i if i % 2 == 0 else i for i in numbers]
print(liste)
print("-------------------------------------")

print("Problem 2")
nested = [[1, 2], [3, 4], [5]]
carpim = 1
for i in nested:
    for x in i:
        print("x: ", x)
        carpim *= x
print(carpim)

print("-------------------------------------")


print("Problem 3")
toplam_degiskeni = 0
while True:
    girdi = input("Sayıyı giriniz:")
    if int(girdi) < 0:
        print("Toplam Değişkeni: ", toplam_degiskeni)
        break
    else:
        sayi = int(girdi)
        toplam_degiskeni += sayi


print("-------------------------------------")

print("Problem 4")
matrix = [[1, 2, 3], [4, 5], [6]]
yeni_liste = [x for i in matrix for x in i]
print(yeni_liste)

print("-------------------------------------")
print("Problem 5")
text = "banana"
sozluk = {}
for i in text:
    if i in sozluk:
        sozluk[i] += 1
    else:
        sozluk[i] = 1

print(sozluk)
