import sqlite3

connection = sqlite3.connect("kutuphane.db")
cursor = connection.cursor()


# def tablo_olustur():
#     cursor.execute(
#         "CREATE TABLE IF NOT EXISTS kitaplik(isim text, yazar text, yayin_evi text, sayfa_sayisi int)")
#     connection.commit()


# tablo_olustur()


# def kayit_ekle(isim, yazar, yayinevi, sayfa_sayisi):
#     cursor.execute(
#         "INSERT INTO kitaplik VALUES(?, ?, ?, ?)", (isim, yazar, yayinevi, sayfa_sayisi))
#     connection.commit()


# kayit_ekle("Küçük Prens", "Charles Dickens", "Everest", 160)


# select()
# def verileri_al():
#     cursor.execute("SELECT * FROM kitaplik")
#     data = cursor.fetchall()
#     print("Kitaplık tablosunun bilgileri...")
#     for i in data:
#         print(i)


# verileri_al()


# def verileri_al_2():
#     cursor.execute(
#         "SELECT isim, yazar FROM kitaplik where yayin_evi = 'YK Yayınları'")
#     data = cursor.fetchall()
#     print("Kitaplık tablosunun bilgileri...")
#     for i in data:
#         print(i)


# verileri_al_2()


# def verileri_al_3(yayin_evi, sayfa_sayisi):

#     cursor.execute(
#         "SELECT * FROM kitaplik where yayin_evi = ? AND sayfa_sayisi >= ?", (yayin_evi, sayfa_sayisi))
#     data = cursor.fetchall()
#     print("Kitaplık tablosunun bilgileri...")
#     for i in data:
#         print(i)


# yayin_evi = input("Aratmak istediğiniz yayın evini giriniz: ")
# sayfa_sayisi = input("Aratmak istediğiniz sayfa sayısını giriniz: ")
# verileri_al_3(yayin_evi, sayfa_sayisi)


# update()
# def veri_guncelle(old_yayinevi, new_yayinevi):
#     cursor.execute(
#         "UPDATE kitaplik SET yayin_evi = ?, isim = 'editlendi' WHERE yayin_evi = ?", (new_yayinevi, old_yayinevi))
#     connection.commit()


# old_yayinevi = input(
#     " Lütfen ismini değiştirmek istediğiniz yayın evini giriniz: ")
# new_yayinevi = input("Yeni yayın evini giriniz: ")
# veri_guncelle(old_yayinevi, new_yayinevi)

def veri_sil(kitap_ismi, sayfa_sayisi):
    cursor.execute(
        "DELETE FROM kitaplik WHERE isim = ? and sayfa_sayisi = ?", (kitap_ismi, sayfa_sayisi))
    connection.commit()
    print("İlgili kitap kütühaneden silindi.")


kitap_ismi = input("Lütfen silmek istediğiniz kitap ismini giriniz: ")
sayfa_sayisi = input(
    "Lütfen silmek istediğiniz kitabın sayfa sayısını giriniz: ")
veri_sil(kitap_ismi, sayfa_sayisi)
connection.close()
# Bu kod, "kutuphane.db" adında bir SQLite veritabanı dosyası oluşturur.
