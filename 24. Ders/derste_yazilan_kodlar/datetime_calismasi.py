import locale
from datetime import datetime

# print(dir(datetime))

# now() ile geçerli tarih ve saati alabiliriz.
# su_an = datetime.now()
# print("Şu anki tarih ve saat: ", su_an)
# print("Şu anki yıl: ", su_an.year)
# print("Şu anki ay: ", su_an.month)
# print("Şu anki gün: ", su_an.day)
# print("Şu anki saat: ", su_an.hour)
# print("Şu anki dakika: ", su_an.minute)
# print("Şu anki saniye: ", su_an.second)
# print("Şu anki mikrosaniye: ", su_an.microsecond)


# ctime() ile tarih ve saati formatlayabiliriz.
# print("Şu anki zaman: ", su_an)
# print("Şu anki zaman güzelleştirilmiş görünümü: ", su_an.ctime())

# strftime() ile tarih ve saati istediğimiz formatta alabiliriz.
# Yıl bilgisini almak için: %Y
# Ay bilgisini almak için: %B
# Gün bilgisini almak için: %A
# Saat bilgisini almak için: %X


# suan = datetime.now()
# # print(datetime.strftime(suan, "%Y"))
# # print(datetime.strftime(suan, "%B"))
# # print(datetime.strftime(suan, "%A"))
# # print(datetime.strftime(suan, "%X"))
# # print(datetime.strftime(suan, "%D"))
# # print(datetime.strftime(suan, "%Y %B %A"))
# # print(datetime.strftime(suan, "%B %A %Y"))

# print(locale.setlocale(locale.LC_ALL, "tr_TR.UTF-8"))
# print(datetime.strftime(suan, "%Y %B %A"))

# timestamp() ile tarih ve saati Unix zaman damgasına çevirebiliriz.
# fromtimestamp() ile Unix zaman damgasını tarih ve saate çevirebiliriz.

# suan = datetime.now()

# print(datetime.timestamp(suan))

# saniye = datetime.timestamp(suan)
# zaman = datetime.fromtimestamp(saniye)
# print("Şu anki zaman: ", zaman)

tarih = datetime(2023, 12, 21)
suan = datetime.now()
fark = suan - tarih
print("Aradaki tarih farkı: ", fark.days)
