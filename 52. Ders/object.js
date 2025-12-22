/* let araba = {
  marka: "Toyota",
  model: "Corolla",
  renk: "Kırmızı",
};

console.log(araba.renk);
console.log(araba["marka"]);

araba.yil = 2020;
console.log(araba);

araba.marka = "BMW";

console.log(araba);

let ogrenci = {
  isim: "Ali",
  yas: 20,
  adres: {
    sehir: "İstanbul",
    ilce: "Kadıköy",
  },
};

console.log(ogrenci.adres.sehir);

let telefon = {
  marka: "Apple",
  model: "iPhone 14",
  tanit: function () {
    console.log(
      "Bu telefon " + this.marka + " marka, " + this.model + " modeldir."
    );
  },
};
telefon.tanit();

for (let i in araba) {
  console.log(araba[i]);
}

console.log(Object.keys(araba));
console.log(Object.values(araba)); 

let users = {
  isim: "Hasan",
  email: "test@gmail.com",
  yas: 31,
};

users.yeniKullanici = {
  isim: "Kaya",
  email: "kaya@gmail.com",
  yas: 28,
};

console.log(users);

if (users.email == "test@gmail.com") {
  delete users.email;
}
console.log(users); 

let gorevler = {
  liste: [],
  id: 1,
};

function gorevEkle(baslik) {
  gorevler.liste.push({ id: gorevler.id, baslik, tamamlandi: false });
  gorevler.id++;
}

function gorevTamamla(id) {
  for (let i = 0; i < gorevler.liste.length; i++) {
    if (gorevler.liste[i].id === id) {
      gorevler.liste[i].tamamlandi = true;
      break;
    }
  }
}

function gorevSilme(id) {
  for (let i = 0; i < gorevler.liste.length; i++) {
    if (gorevler.liste[i].id === id) {
      gorevler.liste.splice(i, 1);
      break;
    }
  }
}

function gorevListeleme() {
  for (let i = 0; i < gorevler.liste.length; i++) {
    console.log(
      `${gorevler.liste[i].id} - ${gorevler.liste[i].baslik} - ` +
        (gorevler.liste[i].tamamlandi ? "tamamlandi" : "Devam ediyor")
    );
  }
}

gorevEkle("Yazılım yaz");
gorevEkle("FIC robot kodlarını yaz");
gorevTamamla(1);
gorevSilme(2);
gorevListeleme();


let sepet = {
  urunler: [],
};

function urunEkle(isim, fiyat, adet) {
  sepet.urunler.push({
    isim,
    fiyat,
    adet,
  });
}

function urunleriListele() {
  for (let i = 0; i < sepet.urunler.length; i++) {
    console.log(
      `${sepet.urunler[i].isim} - ${sepet.urunler[i].fiyat} - ${sepet.urunler[i].adet}`
    );
  }
}

function urunSilme(isim) {
  for (let i = 0; i < sepet.urunler.length; i++) {
    if (sepet.urunler[i].isim === isim) {
      sepet.urunler.splice(i, 1);
      break;
    }
  }
}

function toplamFiyat() {
  let toplam = 0;
  for (let i = 0; i < sepet.urunler.length; i++) {
    toplam += sepet.urunler[i].fiyat * sepet.urunler[i].adet;
  }
  return toplam;
}

urunEkle("Kitap", 30, 2);
urunEkle("Kalem", 5, 5);
urunEkle("Defter", 10, 3);
urunleriListele();
urunSilme("Kalem");
urunleriListele();
console.log("Toplam Fiyat: " + toplamFiyat());

*/

// Kütüphane Yönetim Sistemi

let kutuphane = {
  kitaplar: [],
};

// 1) Yeni kitap ekleme
function kitapEkle(adi, yazari, yayinYili) {
  // Basit doğrulama
  if (!adi || !yazari || typeof yayinYili !== "number") {
    console.log("Hata: adi, yazari ve yayinYili (number) zorunludur.");
    return;
  }

  kutuphane.kitaplar.push({ adi, yazari, yayinYili });
}

// 2) Tüm kitapları listeleme
function kitaplariListele() {
  if (kutuphane.kitaplar.length === 0) {
    console.log("Kütüphanede hiç kitap yok.");
    return;
  }

  for (let i = 0; i < kutuphane.kitaplar.length; i++) {
    const k = kutuphane.kitaplar[i];
    console.log(`${i + 1}) ${k.adi} - ${k.yazari} - ${k.yayinYili}`);
  }
}

// 3) Bir kitabı adına göre arama (kısmi arama + büyük/küçük harf duyarsız)
function kitapAra(arananAd) {
  if (!arananAd) return [];

  const aranan = arananAd.toLowerCase();
  let sonuc = [];

  for (let i = 0; i < kutuphane.kitaplar.length; i++) {
    const k = kutuphane.kitaplar[i];
    if (k.adi.toLowerCase().includes(aranan)) {
      sonuc.push(k);
    }
  }

  return sonuc;
}

// 4) Yayın yılına göre sıralama (artan/azalan)
function yilaGoreSirala(yon = "artan") {
  // orijinali bozmamak için kopya üzerinde sıralıyoruz
  let kopya = kutuphane.kitaplar.slice();

  kopya.sort((a, b) => {
    if (yon === "azalan") return b.yayinYili - a.yayinYili;
    return a.yayinYili - b.yayinYili; // varsayılan artan
  });

  return kopya;
}

/* ====== ÖRNEK KULLANIM ====== */
kitapEkle("Suç ve Ceza", "Dostoyevski", 1866);
kitapEkle("Kürk Mantolu Madonna", "Sabahattin Ali", 1943);
kitapEkle("Sefiller", "Victor Hugo", 1862);

console.log("---- TÜM KİTAPLAR ----");
kitaplariListele();

console.log("---- ARAMA: 'su' ----");
const bulunanlar = kitapAra("su");
for (let i = 0; i < bulunanlar.length; i++) {
  console.log(
    `${bulunanlar[i].adi} - ${bulunanlar[i].yazari} - ${bulunanlar[i].yayinYili}`
  );
}

console.log("---- YILA GÖRE SIRALA (ARTAN) ----");
const siraliArtan = yilaGoreSirala("artan");
for (let i = 0; i < siraliArtan.length; i++) {
  console.log(
    `${siraliArtan[i].adi} - ${siraliArtan[i].yazari} - ${siraliArtan[i].yayinYili}`
  );
}

console.log("---- YILA GÖRE SIRALA (AZALAN) ----");
const siraliAzalan = yilaGoreSirala("azalan");
for (let i = 0; i < siraliAzalan.length; i++) {
  console.log(
    `${siraliAzalan[i].adi} - ${siraliAzalan[i].yazari} - ${siraliAzalan[i].yayinYili}`
  );
}
