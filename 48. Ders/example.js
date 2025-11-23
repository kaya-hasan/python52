// sayi = 5;
// sayi++;

// console.log("Hello, World!", sayi);

// let x = 10;
// let y = 5;
// console.log(x + y);
// console.log(x - y);
// console.log(x * y);
// console.log(x / y);
// console.log(x % y);

// console.log(5 == 6); // false
// console.log(5 != 6); // true
// console.log(10 !== "10"); // true

// console.log(x > y);
// console.log(x >= y);
// console.log(x < y);
// console.log(x <= y);

// let a = 10;
// let b = "10";
// console.log(a == b);
// console.log(a === b);
// console.log(a != b);
// console.log(a !== b);
// console.log(a > 5);

// let x = 10;
// let y = 5;

// console.log(x > y && x >= 10);

// let x = 0;
// let y = 5;

// console.log(x > y || x < 10);

// console.log(!x);

// let a = true;
// let b = false;

// console.log(a && b); // false
// console.log(a || b); // true
// console.log(!a); // false

/* atama operatörleri
a = 5;
a += 3;
console.log(a); // 8
a = a + 3;
console.log(a); // 11 */

/* let num = 10;
num += 5;
console.log(num); // num = num + 5;
num *= 2;
console.log(num); // num = num * 2; */

// koşullar
/* let not = 85; // not değeri 85
if (not >= 90) {
  // not 90 dan büyükse
  console.log("AA");
} else if (not >= 70) {
  // not 70 den büyük ve eşit ise BB
  console.log("BB");
} else {
  console.log("CC"); // hiçbir koşul sağlanmaz ise CC yazdır
} */

// switch - case
/* let gun = 3;
switch (gun) {
  case 1:
    console.log("Pazartesi");

    break;
  case 2:
    console.log("Salı");

    break;
  default:
    console.log("Hafta içi günü");
} */

// üç sayının ortalaması
/* let a = 10;
let b = 20;
let c = 30;
let ortalama = (a + b + c) / 3;
console.log(ortalama); */

/* let note1 = 65;
let note2 = 45;
let note3 = 90;

ortalama = (note1 + note2 + note3) / 3;
console.log("Ortalama: ", ortalama); */

// en büyük sayıyı bulma
/* a = 45;
b = 23;
c = 78;
if (a > b) {
  if (a > c) {
    console.log("En yüksek sayi: " + a);
  } else {
    console.log("En yüksek sayi: " + c);
  }
}

d = 33;
e = 50;
f = 60;
let enBuyuk;
if (d > e && d > f) {
  enBuyuk = d;
} else if (e > d && e > f) {
  enBuyuk = e;
} else {
  enBuyuk = f;
}
console.log("En büyük sayı: " + enBuyuk); */

// bir kişinin yaşını kontrol ederek reşit olup olmadığını belirleme
/* let yas = 23;
if (yas >= 18) {
  console.log("Reşitsiniz.");
} else {
  console.log("Reşit değilsiniz.");
} */

// bir çalışanın maaşına %20 zam yapın ve yeni maaşı hesaplayın
/* let maas = 40000;
let zamOrani = 0.2;
let yeniMaas = maas + maas * zamOrani;
console.log("Yeni maaş: ", yeniMaas); */

// bir öğrencinin aldığını nota göre harf derecesini belirleyin
/* let not = 79;

if (not >= 90) {
  console.log("Harf Notu: AA");
} else if (not >= 80) {
  console.log("Harf Notu: AB");
} else if (not < 80 && not >= 70) {
  console.log("Harf Notu: CB");
} else if (not < 70 && not >= 60) {
  console.log("Harf Notu: CC");
} else {
  console.log("Harf Notu: FF");
} */

// gün numarasına göre gün adını yazdırın
/* let gun = 3;
switch (gun) {
  case 1:
    console.log("Pazartesi");
    break;
  case 2:
    console.log("Salı");
  case 3:
    console.log("Çarşamba");
    break;
  default:
    console.log("Hafta içi günü");
} */

// bir sayının çift mi tek mi olduğunu belirleyin
let sayi = 8;
if (sayi % 2 == 0) {
  console.log(sayi + " çifttir.");
} else {
  console.log(sayi + " tektir.");
}

// bir kişinin kredi alabilmesi için gereken şartları kontrol edin
// yaş 18 veya üzeri
// gelir 5000 veya üzeri
let yas = 25;
let maas = 6000;
if (yas >= 18 && maas >= 5000) {
  console.log("Kredi alabilirsiniz.");
} else {
  console.log("Kredi alamazsınız.");
}
