from Hayvan import Hayvan
from Kus import Kus
from Kopek import Kopek
from At import At

hayvan = Hayvan("Karabaş", 10, "Güzel Hayvan", "10 kg", "Kırmızı")

print(hayvan)
print("-------------------------------")
kus = Kus("Limon", 2, "Sultan Papağanı",
          "150 gram", "Sarı", "2 cm", "Yarı uçar", "Birkaç kelime biliyor")

print(kus)
print(kus.ses_cikar("Ciyak ciyak"))
print(kus.hareket_et("Zıplaya zıplaya"))


print("-------------------------------")

at = At("Beyaz Saray", 3, "Genç At", "150 kg",
        "Beyaz", "Yarışır", "Türk Atı", "32 km")

print(at)
print(at.kos())


print("-------------------------------")

kopek = Kopek("Karabaş", 4, "İsveç köpeği", "15 kg",
              "Mavi", "1 metre", "Kalın", "Süs köpeği")
print(kopek)
print(kopek.havla())
