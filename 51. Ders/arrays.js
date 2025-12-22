// Diziler (Arrays)
/*
Birden fazla veriyi tek bir değişkende saklamak için kullanılan veri yapısıdır.
JavaScript'te diziler, farklı veri türlerini (sayı, string, obje vb.) bir arada tutabilir.
*/

/* let sayilar = [1, 2, 3, 4, 5];
let karisik = ["Merhaba", 25, true]; */

// dizilerde işlemler -> push()
/* sayilar.push(12);
console.log(sayilar); */

// pop -> dizinin son elemanını çıkarır ve döndürür
/* let meyveler = ["Elma", "Armut", "Muz"];
meyveler.push("Çilek", "Kivi");
console.log(meyveler);

silinen = meyveler.pop();
console.log(silinen);
console.log(meyveler); */

/* // slice() -> dizinin belirli bir bölümünü döndürür (başlangıç indeksi, bitiş indeksi)
let sayilar = [10, 20, 30, 40, 50];
let yeniDizi = sayilar.slice(1, 4); // 1. indexten 4. indexe kadar (4 dahil değil)
console.log(yeniDizi); // [20, 30, 40]
console.log(sayilar); // orijinal dizi değişmez */

/* // splice() -> dizinin belirli bir bölümünü çıkarır ve yerine yeni elemanlar ekler
// ilk parametre: başlangıç indeksi
// ikinci parametre: kaç eleman silinecek
let diller = ["JavaScript", "Python", "Java", "C++"];
diller.splice(1, 2); // 1. indexten başlayarak 2 eleman sil
console.log(diller); */

/* let oyunlar = ["CS:GO", "Dota"];
oyunlar.splice(1, "Valorant", "Owerwatch");
console.log(oyunlar); */

// senaryo
// bir kitap listesi oluşturun ve işlemleri gerçekleştirin
// listeye yeni kitap ekle
// son kitabı sil
// ilk iki kitabı seç
// bir kitabı silip yerine yenisini ekle
/* let kitaplar = ["1984", "Suç ve Ceza", "Sefiller"];
kitaplar.push("Hayvan Çiftliği");
console.log(kitaplar);
silinenKitap = kitaplar.pop();
console.log("Silinen Kitap: " + silinenKitap);
console.log(kitaplar);
let secilenKitaplar = kitaplar.slice(0, 2);
console.log("Seçilen Kitaplar: " + secilenKitaplar);
kitaplar.splice(1, 1, "Karamazov Kardeşler");
console.log(kitaplar); */

// dizilerde döngüler -> for döngüsü
/* let renkler = ["Kırmızı", "Yeşil", "Mavi", "Sarı"];
for (let i = 0; i < renkler.length; i++) {
  console.log(renkler[i]);
} */

// dizilerde filtreleme -> filter()
// bir restoran için siparişlerin yönetildiği bir sistem yapalım
// müşteri sipariş verdiğinde sepete ekleyin
// yanlış sipariş verdiyse son siparişi silin
// belirli siparişi seçin (2. ve 4. sipariş arası)
// listeye yeni bir siparişi belirli bir sıraya ekleyin
/* let siparisler = ["Kebap", "Lahmacun", "Döner"];
siparisler.push("Baklava");
console.log("Güncel Siparişler: " + siparisler);
silinenSiparis = siparisler.pop();
console.log("Silinen Sipariş: " + silinenSiparis);
let secilenSiparisler = siparisler.slice(1, 3);
console.log("Seçilen Siparişler: " + secilenSiparisler);
siparisler.splice(1, 0, "Çorba");
console.log("Yeni Siparişler: " + siparisler); */

// sınıf notları analizi
// sınıf notlarıyla ilgili işlemler:
// en yüksek ve en düşük notu bulun
// ortalama hesaplayın
// geçen ve kalan öğrencileri ayırın
/* let notlar = [60, 80, 50, 95, 40];
console.log("Notlar: " + notlar);

let enYuksek = Math.max(...notlar);
let enDusuk = Math.min(...notlar);

console.log("En Yüksek Not: " + enYuksek);
console.log("En Düşük Not: " + enDusuk);

let toplam = 0;

for (let i = 0; i < notlar.length; i++) {
  toplam = toplam + notlar[i];
}
let ortalama = toplam / notlar.length;
console.log("Ortalama Not: " + ortalama);

gecen = [];
kalan = [];

for (let i = 0; i < notlar.length; i++) {
  if (notlar[i] > 60) {
    gecen.push(notlar[i]);
  } else {
    kalan.push(notlar[i]);
  }
}

console.log("Geçen Notlar: " + gecen);
console.log("Kalan Notlar: " + kalan); */

// alışveriş sepeti
// ürünleri sepete ekle
// belirli ürünü sil
// toplam fiyatı hesapla

/* let sepet = [
  { urun: "Kitap", fiyat: 30 },
  { urun: "Kalem", fiyat: 5 },
  { urun: "Defter", fiyat: 10 },
];

sepet.push({ urun: "Silgi", fiyat: 3 });
console.log("Güncel Sepet: ", sepet);
silinenUrun = sepet.pop();
console.log("Silinen Ürün: ", silinenUrun);
let toplamFiyat = 0;
for (let i = 0; i < sepet.length; i++) {
  toplamFiyat += sepet[i].fiyat;
}
console.log("Toplam Fiyat: " + toplamFiyat); */

// film arşivi
// filmleri alfabetik sıraya göre sıralayın
// kullanıcıdan film arayın
// belirli bir filmi arşivden kaldırın
/* let filmler = ["Matrix", "Inception", "Interstellar", "Joker"];
filmler.sort();
console.log("Sıralı Filmler: " + filmler);

let arananKelime = "Joker";
if (filmler.includes(arananKelime)) {
  console.log(arananKelime + " mevcut");
} else {
  console.log("aranan film yok", arananKelime);
}

let silinecekFilm = "Matrix";
let index = filmler.indexOf(silinecekFilm);

if (index !== -1) {
  filmler.splice(index, 1);
  console.log(silinecekFilm + " silindi");
} else {
  console.log("silmek istediğiniz film bulunamadı..");
}

console.log("Güncel Film Arşivi: " + filmler); */

// spor takımı yönetimi:
