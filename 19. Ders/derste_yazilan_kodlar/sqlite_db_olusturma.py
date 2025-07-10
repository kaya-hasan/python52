import sqlite3

connection = sqlite3.connect("kutuphane.db")
cursor = connection.cursor()


def tablo_olustur():
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS kitaplik(isim text, yazar text, yayin_evi text, sayfa_sayisi int)")
    connection.commit()


tablo_olustur()


def kayit_ekle(isim, yazar, yayinevi, sayfa_sayisi):
    cursor.execute(
        "INSERT INTO kitaplik VALUES(?, ?, ?, ?)", (isim, yazar, yayinevi, sayfa_sayisi))
    connection.commit()


kayit_ekle("Sefiller", "Victor Hugo", "YK Yayınları", 250)


connection.close()
# Bu kod, "kutuphane.db" adında bir SQLite veritabanı dosyası oluşturur.
