function selamla(isim) {
  return isim + "as";
}

const selam = (isim) => {
  return isim + "as";
};

// const selamla = (isim) => "As" + isim;

// arrow func. kısaltma olarak hızlı yazım için kullanılan bir yöntemdir
const carpma = (sayi1, sayi2) => sayi1 * sayi2;
console.log(carpma(5, 10));

const topla = (s1, s2) => s1 + s2;
console.log(topla(5, 10));

const rastG = () => Math.random();

const yasG = (yas) => {
  if (yas < 20) {
    return "Çocuk";
  } else if (yas < 65) {
    return "Genç";
  } else if (yas > 65) {
    return "Yaşlı";
  }
};

console.log(yasG(15));

// arrow function lar genellikle diziler ve metodlar kısmında çok kullanılır
const sayilar = [1, 5, 9, 11, 15];
const kare = sayilar.map((sayi) => sayi * sayi);
console.log(kare);

const ciftS = sayilar.filter((sayi) => sayi % 2 === 0);
const tekS = sayilar.filter((sayi) => sayi % 2 === 1);

console.log(ciftS);
console.log(tekS);

const meyveler = ["muz", "elma", "çilek", "karpuz"];
meyveler.forEach((meyve) => {
  console.log("secilen meyve " + meyve);
});

// Arrow functionlar bir fonksiyonun tek bir satırda yazılabilmesi için kullanılır. Eğer fonksiyon tek bir ifade içeriyorsa, süslü parantezler ve return ifadesi kullanılmaz. Ancak, birden fazla ifade içeriyorsa, süslü parantezler ve return ifadesi gereklidir. Arrow functionlar ayrıca, this bağlamını korur, bu da özellikle nesne yöntemlerinde faydalıdır.

// arrow functionlar uzun kodların yazılmasında süreleri kısaltma konusunda etki gösterir
// kısa kodlarda pek etkileri yoktur

const kisi = {
  isim: "Batuhan",
  yas: 27,
  tanit: function () {
    console.log("İsmim " + this.isim);
  },
};

kisi.tanit();
// çıktıda ismim batuhan

// arrow func. olası hata durumu
const kisi1 = {
  isim: "Batuhan",
  yas: 27,
  tanit: () => {
    console.log("İsmim " + kisi.isim);
  },
};

kisi1.tanit();

console.log(`${kisi.isim} ${kisi.yas}`);
// class
class ydil {
  // constructor: class yapısında bir nesne oluşturulurken çalıştırılan özel bir metottur. Nesne oluşturulurken, constructor metodu otomatik olarak çağrılır ve nesnenin başlangıç durumunu belirlemek için kullanılır. Constructor, genellikle nesnenin özelliklerini başlatmak veya gerekli işlemleri yapmak için kullanılır.
  // constructor , her zaman nesne oluşturulurken ilk çalışan fonksiyondur
  // nesne tanımlanması için kullanılır
  constructor(os, surum) {
    this.os = os;
    this.surum = surum;
  }
  bilgiVer() {
    console.log(
      `Uyumlu olduğu işletim sistemi: ${this.os} şu anki güncel sürüm: ${this.surum}`
    );
  }
}
const js = new ydil("Windows", "ES7");
const py = new ydil("Linux", "Python 3.14");
js.bilgiVer();
py.bilgiVer();

class Araba {
  constructor(ad, fiyat) {
    this._ad = ad;
    this._fiyat = fiyat;
  }
  get fiyat() {
    return this._fiyat + " TL";
  }
  set fiyat(yeniFiyat) {
    if (yeniFiyat < 0) {
      console.log("Fiyat negatif olamaz");
    }
  }
  get ad() {
    return this._ad.toUpperCase();
  }
}
const u1 = new Araba("Honda Civic", 700000);
console.log(u1);
