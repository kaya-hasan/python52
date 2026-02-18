// --------------------
// OBJE DESTRUCTURING
const kisi = {
  ad: "Emre",
  soyad: "Güleç",
  sehir: "Bursa",
};

const { ad, soyad, sehir } = kisi;
console.log(ad);
console.log(soyad);
console.log(sehir);

// --------------------
// VARSAYILAN DEĞERLİ DESTRUCTURING
const ayarlar1 = {
  tema: "Karanlik",
  dil: "en",
  bildirim: true,
};

const { tema, dil, yazilim = "java" } = ayarlar1;
console.log(tema);
console.log(dil);
console.log(yazilim);

// --------------------
// İÇ İÇE OBJE DESTRUCTURING
const ayarlar2 = {
  tema: "karanlik",
  dil: {
    kullaniciDil: "en",
    yazilimDil: "js",
  },
};

const {
  tema: tema2,
  dil: { yazilimDil },
} = ayarlar2;

console.log(tema2);
console.log(yazilimDil);

// --------------------
// REST OPERATOR (OBJE)
const ayarlar3 = {
  tema: "Karanlik",
  dil: "en",
  amac: "programlama öğrenmek",
  sure: "1 yil 7 ay",
  bilgisayar: "MSI",
};

const { tema: tema3, dil: dil3, ...digerB } = ayarlar3;
console.log(tema3);
console.log(dil3);
console.log(digerB);

// --------------------
// DİZİ DESTRUCTURING
const renkler1 = ["kirmizi", "siyah", "beyaz"];
const [renk1, renk2, renk3] = renkler1;
console.log(renk1);
console.log(renk2);
console.log(renk3);

// --------------------
const renkler2 = ["kirmizi", "siyah", "beyaz"];
const [renk4, , renk6] = renkler2;
console.log(renk4);
console.log(renk6);

// --------------------
const renkler3 = ["kirmizi", "siyah", "beyaz", "sari", "turuncu"];
const [renk7, renk8, ...digerleri] = renkler3;
console.log(renk7);
console.log(renk8);
console.log(digerleri);

// --------------------
// DEĞİŞKEN TAKASI
let x = 1000;
let y = 5;

[x, y] = [y, x];
console.log(x);
console.log(y);

// --------------------
// FONKSİYON + OBJE
function deneme(ad, soyad, yas) {
  console.log(`${ad}, ${soyad}, ${yas}`);
}

const d1 = {
  ad: "deneme",
  soyad: "denemelik",
  yas: "55",
  sehir: "adana",
};

deneme(d1.ad, d1.soyad, d1.yas);

// --------------------
// VARSAYILAN PARAMETRE (ESKİ YÖNTEM)
function selamla(isim) {
  isim = isim || "misafir";
  console.log("Merhaba " + isim);
}

selamla("Emre");
selamla();
