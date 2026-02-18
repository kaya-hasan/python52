export default class Ogrenci {
  constructor(ad, soyad) {
    this.ad = ad;
    this.soyad = soyad;
  }
  bilgilendir() {
    console.log(`Öğrenci Adı: ${this.ad}, Soyadı: ${this.soyad}`);
  }
}

export const SINIF_Mevcut = 2;
