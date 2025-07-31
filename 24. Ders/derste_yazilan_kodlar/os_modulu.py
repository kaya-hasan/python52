# os modülü
import os
# os modülü, işletim sistemi ile etkileşim kurmamızı sağlar.
# Dosya ve dizin işlemleri, çevresel değişkenler, süreç yönetimi gibi birçok işlevi vardır.

# print(dir(os))

# getcwd() ile geçerli çalışma dizinini alabiliriz.
# print(os.getcwd())

# chdir() ile çalışma dizinini değiştirebiliriz.
# print(os.chdir("/Users/hasankaya/Desktop/2025 Güncel/pythonNova/python52"))
# print(os.getcwd())

# listdir() ile belirtilen dizindeki dosya ve dizinleri listeleyebiliriz.
# os.chdir("/Users/hasankaya/Desktop")
# print("bulunduğumuz adres: ", os.getcwd())
# print(os.listdir())

# mkdir() ile yeni bir dizin oluşturabiliriz.
# os.mkdir("yeni_dizin")

# makedirs() ile çok katmanlı dizinler oluşturabiliriz.
# os.makedirs("birinci/ikinci/ucuncu")

# rmdir() ile boş bir dizini silebiliriz.
# os.rmdir("deneme")

# removedirs() ile çok katmanlı boş dizinleri silebiliriz.
# os.makedirs("birinci/ikinci/ucuncu")
# os.removedirs("birinci/ikinci/ucuncu")

# rename() ile dosya veya dizin adını değiştirebiliriz.
# os.rename("OOO", "SSS")
# os.rename("deneme.py", "test.py")

# stat() ile dosya veya dizin hakkında bilgi alabiliriz.
# print(os.stat("test.py"))

# walk() ile dizindeki tüm dosya ve dizinleri dolaşabiliriz.
for klasor_yolu, klasor_isimleri, dosya_isimler in os.walk("/Users/hasankaya/Desktop/2025 Güncel/pythonNova/python52"):
    print("Şu anki dizin: ", klasor_yolu)
    print("Klasörler: ", klasor_isimleri)
    print("Dosyalar: ", dosya_isimler)
    print("*" * 40)
