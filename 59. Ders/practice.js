// Toplama işlemi yapan bir fonksiyon
// const topla = (a, b) => a + b;

// ecma
// let ve const kullanılır genelde
// var kullanımı eskidi

/*
console.log(" VAR BLOCK SCOPE PROBLEM ");

function varP() {
  console.log("Func. start");
  if (true) {
    var mesaj = "Merhaba";
    console.log("Blok içerisinde: ", mesaj);
  }
  console.log("Blok dışında: ", mesaj);
}

varP();
*/

/*
console.log(" HOSTING PROBLEM ");
console.log(d1);
var d1 = 42;
console.log(d1);
*/

/* var ile let farkı tek örnekte:
console.log("Let ile çözüm");

function letP() {
  console.log("Func. start");

  if (true) {
    // eğer let ile if bloğunun içerisine bir değişken tanımlarsak başka bir blokta
    // bu if kodunun haricinde bu değişkene erişemeyiz
    // eğer var ile tanımlarsak bu if bloğu dışında fonksiyonun içerisinde kullanabiliriz
    let cikti = "Deneme Yazısı 1";
    console.log("Blok içerisi yine", cikti);
  }
  console.log("Blok dışarısı", cikti); // Hata verir
}

letP();
*/

/*
function (deneme1) {
  if (asdfgfds) {
    let ssd = "denemeasd"
    console.log("yukarıdakiyle ilgili bir şey,", ssd);
  }
  let d2 = deneme2();
  d2 =  deneme(d2,ssd); // en çok karşılaşılan dikkat hatalarından biridir
  // deneme(d2, undefined)
}
*/
/*
function denemeFor() {
  if (document.getElementById("email")) {
    var emailHatasi = "Emailinizi girmeniz gerekmektedir!";
    console.log(emailHatasi);
  }
  if (document.getElementById("sifre")) {
    let sifreHatasi = "Şifrenizi girmeniz gerekmektedir!!";
    console.log(sifreHatasi);
  }
  if (emailHatasi) {
    gosterHata(emailHatasi);
  }
  if (sifreHatasi) {
    gosterHata(sifreHatasi);
  }
  // var ile yaptığımız tanımlamada emailHatasi çalıştırılır çünkü otomatik veri yoksa bile undefine değerini alır.
  // var ile blok dışına undefined verisinin dönmesi sonucu hosting hatası meydana gelir
}
  */

/*
function denemeFor() {
  let emailHatasi = "";
  let sifreHatasi = "";
  if (document.getElementById("email")) {
    emailHatasi = "Emailinizi girmeniz gerekmektedir!";
    console.log(emailHatasi);
  }
  if (document.getElementById("sifre")) {
    sifreHatasi = "Şifrenizi girmeniz gerekmektedir!!";
    console.log(sifreHatasi);
  }
  if (emailHatasi) {
    gosterHata(emailHatasi);
  }
  if (sifreHatasi) {
    gosterHata(sifreHatasi);
  }
}
*/

// for ile karşılaşılan hatalar ve farklar
/*
console.log("Var ile for");

for (var i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log("Sayi: ", i);
  }, 1000);
}
console.log("Döngü dışında yazdırılacak i değeri: ", i); // 3 yazdırır
// i değeri her zaman 3 gözükür çünkü var ile tanımlandığında fonksiyon scope'una girer

// let ile doğru kodun yazdırılması
console.log("let ile for");

for (let i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log("Sayi: ", i);
  }, 1000);
}
// console.log("Döngü dışında yazdırılacak i değeri: ", i); // Hata verir çünkü let ile tanımlandığında blok scope'una girer
*/

// var kullanmamak daha hayırlıdır
// değişecek değerler için let değişmeyenler için const
// NOT: eğer değer blockta kalsın istemiyorsak block dışına let ile tanımlama yaparız
/*
console.log("Const örneği");
const vergi = 0.2;
console.log("Vergi orani: ", vergi);
const kisi = {
  ad: "Emre",
  yas: 26,
};
console.log("Başlangic: ", kisi);

// vergi = 0.3; // Hata verir çünkü const ile tanımlanan değişkenlerin değeri değiştirilemez
// objenin alt özellikleri değiştirilebilir
kisi.yas = 30; // Hata vermez çünkü const ile tanımlanan nesnelerin içindeki özellikler değiştirilebilir
kisi.meslek = "Mühendis";
console.log("Değişiklikler yapıldıktan sonra: ", kisi);
// kisi = { ad: "Ahmet", yas: 40 }; // bu şekilde bir yeni obje ataması yapamayız
*/
/*
const elektronik = ["arduino", "esp32", "stm32"];
elektronik.push("jumper");
console.log(elektronik);
*/
// elektronik = ["yeni", "dizi"]; // Hata verir çünkü const ile tanımlanan dizilerin kendisi değiştirilemez
// string, boolean, number, basit veri yapıları tamamen sabittir
// fakat obje ve diziler gibi yapılar referans olarak sabit içeriği ise değiştirilebilir

/*
console.log("const/let kullanım örneği"); // değiştirilmemesi gerektiği için const ile yazarız
const API_URL = "https://örnekapi.com";
const max_attempt = 5;

let sayac = 0; // saydırılacak ve değeri değişecek bir değişken olduğu için let ile yazarız
let kGiris = "";
function elektronikMarket() {
  const KargoUcret = 120;
  let toplam = 0;
  const urunler = [
    { isim: "stm32", fiyat: 1800 },
    { isim: "MediaC", fiyat: 320 },
  ];
  for (let urun of urunler) {
    toplam += urun.fiyat;
  }
  if (toplam > 1000) {
    toplam += KargoUcret;
  }
  return toplam;
}
console.log("Toplam Ödeme Tutarı: ", elektronikMarket(), "TL");
*/

/*
var PI = 3.14; // PI zaten sabit bir değer olduğu için const ile tanımlanması daha doğru olur
PI = 3.1416;

let maksimum = 100; // hata yokyur
maksimum = 150;

const ogrenci = "Hasan";
ogrenci = "Batuhan"; // hata verir
*/
/*
{
  let x = 10;
}
console.log(x); // var ile yazsak ekranda 10 yazardı ama let ile yazdığımız için hata verir çünkü x değişkeni sadece blok içerisinde geçerlidir
*/
/*
const denemeDizi = [0, 1, 2, 3, 4];
denemeDizi.push(5);
console.log(denemeDizi);
*/

// var ile yazarsak hep maksimum değer yazdırılır
/*
for (let i = 0; i < 3; i++) {
  setTimeout(function () {
    console.log("Sayi: ", i);
  }, 100);
}
// Döngü dışında yazdırılacak i değeri: ", i); // 3 yazdırır
// i değeri her zaman 3 gözükür çünkü var ile tanımlandığında fonksiyon scope'una girer
*/
