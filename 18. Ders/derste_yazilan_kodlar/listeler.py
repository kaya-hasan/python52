# append - listenin sonuna eleman ekler
# liste = [1, 2, 3, 4, 5]
# liste.append(6)
# print(liste)
# liste.append("Python")
# print(liste)

# extend - listenin sonuna başka bir liste ekler
# liste1 = [1, 2, 3, 4]
# liste2 = [5, 6, 7, 8]
# liste1.extend(liste2)
# print(liste1)


# insert() - listenin istediğimiz bir indeksine eleman ekler
# liste = [1, 2, 3, 4, 5, 6, 7]
# liste.insert(2, "Nova")
# print(liste[5])
# liste.insert(5, "Akademi")
# print(liste)

# pop() - listenin sonundaki elemanı siler
# liste = [1, 2, 3, 4, 5, 6, 7]
# liste.pop()
# print(liste)
# liste.pop()
# print(liste)
# liste.pop()
# print(liste)
# liste.pop(2)
# print(liste)

# remove() - listeden istediğimiz elemanı siler
# liste = ["Python", "Php", "Java", "Javascript", "Ruby", "Go", "Rust"]
# liste.remove("C#")
# print(liste)

# index() - listede istediğimiz elemanın indeksini verir
# liste = [1, 2, 3, 4, 5, 6, 7]
# print(liste.index(77))
# liste = ["Python", "Php", "Java", "Javascript",
#          "Python", "Ruby", "Go", "Rust", "Python"]
# print(liste.index("Python"))
# print(liste.index("Python", 2))

# count() - listede istediğimiz elemanın kaç kez geçtiğini verir
# liste = [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 2, 3, 4, 5, 6, 7, 8]
# print(liste.count(88))

# sort() - listeyi sıralar
# liste = [100, 1100, 2, 5, 77, -22, -5, 0, 11, 990, 88]
# liste.sort()
# print(liste)

liste = ["a", "b", "c", "Python", "Php", "Java", "Javascript",
         "Python", "Ruby", "Go", "Rust", "Python", "Z"]
liste.sort()
print(liste)
