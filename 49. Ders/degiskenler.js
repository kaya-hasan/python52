/* function testVar() {
  if (true) {
    var message = "Var ile tanimladim!";
  }
  console.log(message); // Çıktı: "Var ile tanimladim!"
}
testVar();

for (var i = 0; i < 3; i++) {
  console.log("Döngü içindeki i: ", i);
}
console.log("Döngü dışındaki i: ", i); // Çıktı: 3

function testLet() {
  if (true) {
    let message = "Let ile tanimladim!";
    console.log(message); // Çıktı: "Let ile tanimladim!"
  }
  console.log(message); // Hata: message tanımlı değil
}
testLet(); */

/* for (let i = 0; i < 3; i++) {
  console.log("Döngü içindeki i: ", i);
}
console.log("Döngü dışındaki i: ", i); // Çıktı: 3 */

/* const PI = 3.14159;
console.log(PI); // Çıktı: 3.14159
PI = 3.14; // Hata: Atama hatası, çünkü PI sabit bir değişkendir */

/* const colors = ["red", "green", "blue"];
colors.push("yellow"); // Bu geçerli
console.log(colors); // Çıktı: ["red", "green", "blue", "yellow"]

let mesaj = "Merhaba, Dünya";
selam = "Merhaba"; // Tek tirnak
mesaj = `Merhaba, Dünya`; // Backtick

let mesaj ="JavaScript";
console.log(mesaj.length);
console.log(mesaj.charAt(0));
console.log(mesaj.charAt(4));
console.log(mesaj.toUpperCase()); // Çıktı: MERHABA
console.log(mesaj.toLowerCase()); // Çıktı: merhaba/

console.log(mesaj).indexOf("a"); // Çıktır 4
console.log(mesaj.lastIndexOf("a")); // Çakta: 10 */
/* let mesaj = "JavaScript";
console.log(mesaj.slice(0, 4)); // Çikts: Javaconsole.log(mesaj.slice(4)); // Çıktı: Script
console.log(mesaj.replace("Java", "Type")); // Çıktı: TypeScript */

/* let mesaj = "Merhaba JavaScript";
console.log(mesaj.replace("JavaScript", "Dünya")); // Çıktı: Merhaba Dünya
console.log(mesaj.includes("JavaScript")); // Çıkt: true
console.log(mesaj.includes("Python")); // Çikta: false */

/* let mesaj = "JavaScript öğreniyorum";
console.log(mesaj.startsWith("Java")); // Çıktı: true
console.log(mesaj.endsWith("yorum")); // Çıktı: true */

/* let mesaj = "  Merhaba Dünya  ";
console.log(mesaj.trim()); // Çıktı: "Merhaba Dünya" */

/* let mesaj = "Merhaba, Dünya, JavaScript";
console.log(mesaj.split(", ")); // Çıktı: ["Merhaba", "Dünya", "JavaScript"]
 */

// bir kullanıcı adını ve soyadını girdiğinde, sistem bu isimleri uygun biçimde (baş harf büyük, diğer harfler küçük) birleştirmelidir.

/* firstName = "hasan";
surname = "kaya";

firstName =
  firstName.charAt(0).toUpperCase() + firstName.slice(1).toLowerCase();
console.log(firstName);

surname = surname.charAt(0).toUpperCase() + surname.slice(1).toLowerCase();
console.log(surname);
console.log("benim adım " + firstName + " soyadim " + surname); */

// kullanıcıdan alınan bir cümledeki kelime sayısını bulan bir program yazın.
/* let sentence = "JavaScript öğreniyorum ve çok eğleniyorum";
console.log(sentence.length); */

// kullanıcıdan bir e-posta adresi alın ve "@" işareti ile .com içermeyen eposta adreslerinin geçersiz olduğunu bildiirin

/* let email = "hellogmail.com";

if (email.includes("@") && email.endsWith(".com")) {
  console.log("E-posta adresi geçerli.");
} else {
  console.log("Geçersiz e-posta adresi!");
} */

// kullanıcıdan kelime alın ve bu kelimenin ters çevrilmiş halini ekrana yazdırın
/* kelime = "kelime";
yeniKelime = kelime.split("").reverse().join("");
console.log(yeniKelime); */

// kullanıcının girdiği bir cümledeki tüm "kötü" kelimeleri sansürleyin. Örneğin, "Javascript çok zor" cümlesinde "zor" kelimesini "****" ile değiştirin.

/* let cumle = "JavaScript çok zor ve sıkıcı";
let sansurluCumle = cumle.replace("zor", "****").replace("sıkıcı", "****");
console.log(sansurluCumle); */
// let cumle = "JavaScript çok zor ve sıkıcı";
// let sansurluCumle = cumle.replace("zor", "****").replace("sıkıcı", "****");
// console.log(sansurluCumle);

// kullanıcının girdiği bir isim listesindeki isimleri uygun biçime dönüştürürerek ekrana yazdıırın. tüm isimlerin ilk harfi büyük diğer harfler küçük olacak.
/* let isimler = "ali, veli, ayse, fatma";
let isimListesi = isimler.split(", ");
for (let i = 0; i < isimListesi.length; i++) {
  isimListesi[i] =
    isimListesi[i].charAt(0).toUpperCase() +
    isimListesi[i].slice(1).toLowerCase();
}
console.log(isimListesi.join(", ")); */

// Kullanıcıdan bir isim alın ve ismi içeren özel bir mesaj oluşturun. Örneğin, kullanıcı "Ahmet" girerse "Merhaba, Ahmet! JavaScript öğrenmeye hazır mısın?" mesajını döndürün.
/* let kullaniciIsmi = "Ahmet";
let mesaj = "Merhaba " + kullaniciIsmi + "! JavaScript öğrenmeye hazır mısın?";
console.log(mesaj); */

// döngüler
// for
/* const meyveler = ["elma", "muz", "çilek"];
for (let i = 0; i < meyveler.length; i++) {
  console.log(meyveler[i]);
} */

// while
/* let i = 1;
while (i <= 5) {
  console.log("Sayı: " + i);
  i++;
} */
