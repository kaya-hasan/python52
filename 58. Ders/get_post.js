// sunucuda haberleşme
// GET -> Bir veriyi almak için (istemek amacıyla) kullanılır.

/*
let xhr = new XMLHttpRequest();
xhr.open("GET", "https.....");

xhr.onload = function () {
  if (xhr.status === 200) {
    console.log("gelen veri: ", xhr.responseText);
    let kullanici = JSON.parse(xhr.responseText);
    alert("Kullanici adi: " + kullanici.name);
  }
};

xhr.send();
*/

// POST -> Bir veriyi göndermek için kullanılır. (Text, formlar (genelde form olur) dosyalar )
