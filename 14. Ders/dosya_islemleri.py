# "r" kipi / mode - read
# try:
#     file = open("bilgiler.txt", "r", encoding="utf-8")
#     for satir in file:
#         print(satir, end="")
#     file.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı.")


# try:
#     file = open("bilgiler.txt", "r", encoding="utf-8")
#     # read() fonksiyonu
#     icerik = file.read()
#     print("Dosyanın içeriği (1. dosya okuması): ")
#     print(icerik)
#     icerik2 = file.read()
#     print("Dosyanın içeriği (2. dosya okuması): ")
#     print(icerik2)
#     file.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı.")

# readline() fonksiyonu
# try:
#     file = open("bilgiler.txt", "r", encoding="utf-8")
#     # read() fonksiyonu
#     icerik = file.readline()
#     print("Dosyanın içeriği (1. dosya okuması): ")
#     print(icerik)
#     icerik2 = file.readline()
#     print("ikinci satır verisi")
#     print(icerik2)
#     icerik3 = file.readline()
#     print("üçüncü satır verisi")
#     print(icerik3)
#     file.close()
# except FileNotFoundError:
#     print("Dosya bulunamadı.")


# readlines() fonksiyonu
file = open("bilgiler.txt", "r", encoding="utf-8")
icerik = file.readlines()
print("readline fonksiyonu ile ekrana basıldı")
print(icerik)
