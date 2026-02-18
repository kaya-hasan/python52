// let rd1Engineer = {
//   isim: "Emre",
//   soyisim: "Korkmaz",
//   dogumt: "01.01.2000",
//   poz: "ElektrikMuh.",
//   calismaSuresi: "2Yil",
// };
// /*
// {
//   "isim": "Emre",
//   "soyisim": "Korkmaz",
//   "dogumt": "01.01.2000",
//   "poz": "ElektrikMuh.",
//   "calismaSuresi": "2Yil",
// }
//   */

// stringify() // Nesneleri bir dizeye dönüştürmek için kullanılır.
// parse() // JSON dosyasını nesneye dönüştürmek için kullanılır.

// JSON.stringify(value {, ...})

/*let rd1Engineer = {
  isim: "Emre",
  soyisim: "Korkmaz",
  dogumt: "01.01.2000",
  poz: "ElektrikMuh.",
  calismaSuresi: "2Yil",
};

const JSONVeri = JSON.stringify(rd1Engineer);
console.log("JSON Veri:", JSONVeri);

const tJS = JSON.parse(JSONVeri);
console.log("isim: ", tJS.isim);

// NOT: Eğer bir fonksiyonu dönüştürmek isterseniz stringfy yerine toJSON() fonksiyonunu kullanabilirsiniz.
// AJAX - Asenkron JavaScript ve XML

const xhr = new XMLHttpRequest();
const formData = new FormData(formElement);
xhr.open("GET", "https://jsonplaceholder.typicode.com/users/ID", true);

xhr.onload = function () {
  if (xhr.status === 200) {
    const veri = JSON.parse(xhr.responseText);
    console.log("Kullanıcı Adı: ", veri.name);
  } else {
    console.error("Hata var: ", xhr.status);
  }
};

xhr.onload = function () {
  alert("Yükleme başarılı");
};

xhr.send(formData);*/

/*
new XMLHttpRequest(); // istek oluşturma kodumuzdur
open("GET", URL, true); // Alınacak verinin nereden alınacağını ve türünü belirler
onload = function () {}; // İstek tamamlandığında çalışacak fonksiyonu belirler
onloadend // İstek başarılı da başarısız da olsa bittiği anda çalışacak olan kod kısmı için kullanılır
onerror = function () {}; // İnternet bağlantısının kopması durumunda kullanıcıya verilecek cevap kısmıdır
send(); // gönderme komutudur
*/

/*
const deneme = {
  baslik: "JS Deneme",
  tarih: new Date(),
  katilimciSayi: 3,
  toJSON() {
    return {
      egitimAdi: this.baslik,
      yil: this.tarih.getFullYear(),
    };
  },
};

console.log(JSON.stringify(deneme));
*/

// yaygın hatalar
// Virgül Hatası
//[1,2,3,]

// Süslü Parantez İçerisi Tırnak Hatası
// Hatalı olan {sayi: 3} <---- Doğru olan {"sayi": 3}
// Süslü parantez içi tırnak hatası
// {'isim': 'Emre'} <----- {"isim": "Emre"}
// NOT: JSON İÇİNDE FONKSİYON SAKLANAMAZ / AKTARILAMAZ / DÖNÜŞTÜRÜLEMEZ sadece veriler dönüştürülür

// Onload - onloadend - onerror;

// PROBLEM: Bir kullanıcı nesnesi oluşturun, toJSON ile adı ve bugünün tarihini döndürün bu nesneyi JSON.stringify ile konsola yazdıran kodu yazın

/*
const user = {
  name: "Hasan",
  toJSON() {
    const today = new Date();

    return {
      name: this.name,
      year: today.getFullYear(),
    };
  },
};

const jsonData = JSON.stringify(user);
console.log(jsonData);
*/
/*
function havaDurumuGetir(sehir) {
  let request;
  if (window.XMLHttpRequest) {
    request = new XMLHttpRequest();
  } else {
    request = new ActiveXObject("Microsoft.XMLHTTP");
  }
  const apiKey = "...";
  const url = apiurl;

  request.open("GET", url, true);

  request.onload = function () {
    if (request.stringify === 200) {
      const veri = JSON.parse(request.responseText);
      console.log('{sehir} için hava durumu');
      console.log('Hava durumu: ${veri.weather[0].description}');
      console.log(sıcaklık....);
    }
    else {
      console.error("Sunucuda bir hata oluştu. Durum kodu: " + request.status);
    }
  };
  request.onerror = function () {
    console.error("Ağ bağlantı hatası, sunucu ile iletişim kuramıyoruz");
  }
  request.send();
  havaDurumuGetir("Sehir Adı");
}
*/
