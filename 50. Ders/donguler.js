// for döngüsü

/* for (let i = 0; i < 5; i++) console.log("hello js");

const meyveler = ["Elma", "Armut", "Muz"];
for (let i = 0; i < meyveler.length; i++) {
  console.log(meyveler[i]);
} */

// while döngüsü
/* let i = 1;
while (i <= 5) {
  console.log(i);
  i++;
} */

// do while döngüsü
/* let sayi;
do {
  sayi = parseInt(prompt("Pozitif bir sayı girin: "));
} while (sayi <= 0);
console.log("Teşekkürler! Girdiğiniz pozitif sayı: " + sayi); */

// for...in döngüsü
/* const ogrenci = {
  ad: "Ali",
  yas: 20,
  bolum: "Bilgisayar Mühendisliği",
};

for (let ozellik in ogrenci) {
  console.log(`${ozellik}: ${ogrenci[ozellik]}`);
} */

// döngülerde kullanılan anahtar kelimeler
// break
// continue
/* for (let i = 1; i <= 10; i++) {
  if (i === 5) {
    break; // döngüyü sonlandırır
  }
  console.log(i);
} */
/* for (let i = 1; i <= 10; i++) {
  if (i % 2 === 0) {
    continue; // çift sayıları atlar
  }
  console.log(i); // sadece tek sayıları yazdırır
} */

// iç içe döngüler
/* for (let i = 1; i <= 5; i++) {
  for (let j = 1; j <= 5; j++) {
    console.log(`i: ${i} x j: ${j}`);
  }
} */

// faktöriyel hesaplama
/* let sayi = 5;
let faktoriyel = 1;
for (let i = 1; i <= sayi; i++) {
  faktoriyel *= i;
  console.log(faktoriyel);
} */

// 1'den 10'a kadar sayıları yazdır
/* for (let i = 1; i <= 10; i++) {
  console.log(i);
} */

// bir dizideki elemanları yazdır
/* const meyveler = ["Elma", "Armut", "Muz", "Karpuz"];
for (let i = 0; i < meyveler.length; i++) {
  console.log(meyveler[i]);
} */

// iç içe döngüler çarpım tablosu

/* for (let i = 1; i <= 10; i++) {
  for (let j = 1; j <= 10; j++) {
    console.log(`i: ${i} * j: ${j} = ${i * j}`);
  }
} */

// nesnenin özelliklerini yazdırın
/* const ogrenci = {
  ad: "Ahmet",
  yas: 21,
  bolum: "Bilgisayar Mühendisliği",
};
for (let ozellik in ogrenci) {
  console.log(`${ozellik}: ${ogrenci[ozellik]}`);
} */

// bir dizinin toplamını hesapla
/* const sayilar = [1, 2, 3, 4, 5];
let toplam = 0;
for (let i = 0; i < sayilar.length; i++) {
  toplam += sayilar[i];
}
console.log("Toplam: " + toplam); */

// rastgele sayı üret ve 10'dan küçük olup olmadığını kontrol et
/* rastgele = Math.floor(Math.random() * 20);

if (rastgele < 10) {
  console.log(rastgele + " sayısı 10'dan küçüktür.");
} else {
  console.log(rastgele + " sayısı 10'dan büyük veya eşittir.");
} */

// asal sayıları bulma
/* sayi = 13;
let asal = true;
for (let i = 2; i < sayi; i++) {
  if (sayi % i === 0) {
    asal = false;
    break;
  }
}
console.log(asal ? "Asaldır" : "Asal değildir"); */

// yıldızlarla piramit çizme
/* let satir = 10;
for (let i = 1; i <= satir; i++) {
  let satirYildiz = "";
  for (let j = 1; j <= i; j++) {
    satirYildiz += "*";
  }
  console.log(satirYildiz);
} */

// dizide en büyük sayıyı bulma
/* const sayilar = [15, 42, 7, 98, 34, 12];
let enBuyuk = sayilar[0];
for (let i = 1; i < sayilar.length; i++) {
  if (sayilar[i] > enBuyuk) {
    enBuyuk = sayilar[i];
  }
}
console.log("Dizideki en büyük sayı: " + enBuyuk); */

// bir dizide belirli bir sayıyı arama
const sayilar = [10, 20, 30, 40, 50];
const arananSayi = 70;
let bulunduMu = false;
for (let i = 0; i < sayilar.length; i++) {
  if (sayilar[i] === arananSayi) {
    bulunduMu = true;
    console.log(arananSayi + " sayısı dizide bulundu.");
    break;
  }
}

// bir diziyi tersine çevirme
/* const orijinal = [1, 2, 3, 4, 5];
const ters = orijinal.toReversed();

console.log(orijinal);
console.log(ters);

const orijinal2 = [1, 2, 3, 4, 5];
const ters2 = [];
for (let i = orijinal2.length - 1; i >= 0; i--) {
  ters2.push(orijinal2[i]);
}
console.log("orijinal = ", orijinal);
console.log("ters2 = ", ters2); */

// sayının basamak toplamını bulma
const sayi = 12345;
let toplam = 0;

let yeniSayi = sayi;
while (yeniSayi > 0) {
  toplam += yeniSayi % 10;
  yeniSayi = Math.floor(yeniSayi / 10);
}
console.log("yeni sayi = ", toplam);

// alfabenin harflerini yazdırma
const alfabe = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
for (let i = 0; i < alfabe.length; i++) {
  console.log(alfabe[i]);
}
