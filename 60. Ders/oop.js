class Hayvan {
  constructor(isim, yas) {
    this.isim = isim;
    this.yas = yas;
  }
  bilgiVer() {
    console.log(`Hayvanın ismi: ${this.isim}, Yaşı: ${this.yas}`);
  }
  hayvanSesi() {
    console.log("Hayvan ses çıkarıyor");
  }
}
class Kedi extends Hayvan {
  constructor(isim, yas, cins) {
    // super() her zaman ilk satırda yazılmalıdır extendsler için
    super(isim, yas);
    this.cins = cins;
  }
  tirmanabilir() {
    console.log(`${this.isim} agaca tirmaniyor`);
  }
  hayvanSesi() {
    console.log("Miyav");
  }
}

class Aslan extends Hayvan {
  constructor(isim, yas, renk) {
    super(isim, yas);
    this.renk = renk;
  }
  hayvanSesi() {
    console.log("Roar");
  }
  saldiri() {
    console.log(`${this.isim} saldiriyor`);
    super.bilgiVer(); // super ile üst sınıfın bilgiVer() metodunu çağırıyoruz
  }
}

const kedi = new Kedi("Sokak Kedisi", 2, "Tekir");
const aslan = new Aslan("Simba", 1, "Sari");
kedi.bilgiVer();
kedi.tirmanabilir();
kedi.hayvanSesi();
console.log("-------------------");
aslan.bilgiVer();
aslan.saldiri();
aslan.hayvanSesi();

// super() metodu, bir alt sınıfın constructor'ında, üst sınıfın constructor'ını çağırmak için kullanılır. Bu, alt sınıfın üst sınıfın özelliklerini ve yöntemlerini miras almasını sağlar. super() metodu, alt sınıfın constructor'ında ilk satırda çağrılmalıdır, aksi takdirde bir hata oluşur. super() metodu, ayrıca alt sınıfın yöntemlerinde de kullanılabilir ve bu durumda üst sınıfın aynı adlı yöntemini çağırır.
