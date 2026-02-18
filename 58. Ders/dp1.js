function Kayditamamla() {
  let isim = document.getElementById("isim").value;
  let email = document.getElementById("email").value;

  let özelK =
    "isim=" + encodeURIComponent(isim) + "&email=" + encodeURIComponent(email);

  let xhr = new XMLHttpRequest();
  xhr.open("POST", "kayit.php");
  xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
  xhr.onload = function () {
    if (xhr.status === 200 || xhr.status === 201) {
      console.log("Sunucu yanıt: ", xhr.responseText);
      let yanit = JSON.parse(xhr.responseText);
      document.getElementById("sonuc").innerHTML = (
        <>
          <h2 style="color: green;">Kayıt Tamamlanmıştır</h2>
          <p>
            <strong>Sunucu tarafından gelen id: </strong>${yanit.id}
          </p>
          <p>
            <strong>Gönderdiğimiz veri:</strong>${özelK}
          </p>
        </>
      );
    } else {
      alert("Kayıt tamamlanmıştır");
    }
  };
  xhr.send(özelK);
}
