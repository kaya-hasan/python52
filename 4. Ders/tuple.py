# tuple
# demet = (1, 2, 3, 4, 5, 6, 7, 8, 9)

# print(demet)
# print(type(demet))

# tek elemanlı olması için sonuna , eklenir
# demet = ("Hasan",)
# print(type(demet))

# tuple lara indexin ile ulasilabilir
# demet = (1, 2, 3, 4, 5, 6)
# # 2. indexten basla ve sona kadar yazdır
# print(demet[2:])
# # 2. indexten 4. indexe kadar yazdır
# print([demet[2:4]])

# farklı veri tipleri içerebilir
# demet = (1, 2, 3, "Nova", "Academy", "Nova", 1.45)
# print(demet.index("Nova"))  # Nova'nın indexini bul
# print(demet.index("Academy"))  # Academy'nin indexini bul
# print(demet.index(1.45))  # 1.45'in indexini bul

# demet = (1, 2, 3, "Nova", "Academy", "Nova", "Nova", "Nova", 1.45)
# print(demet.count("Nova"))  # Nova'nın kaç kez tekrar ettiğini bul

# listelerden farki -> degistirilemez - immutable
demet = ("Elma", "Armut", "Kivi")
print(demet[0])
# demet[0] = "Çilek"  # hata verir
demet.remove("Elma")  # hata verir
