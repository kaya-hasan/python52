const canvas = document.getElementById("CanvasAnlatimi");
const ctx = canvas.getContext("2d");
/*
ctx.fillStyle = "black"; // doldurma rengi
ctx.fillRect(0, 0, 15, 15);

ctx.fillStyle = "black"; // doldurma rengi
ctx.fillRect(25, 25, 50, 50);

ctx.strokeStyle = "yellow"; // çizgi rengi
ctx.lineWidth = 5; // çizgi kalınlığı
ctx.strokeRect(300, 50, 50, 50); // sadece kenar çizimi

console.log("Çizim tamamlandı.");

ctx.beginPath(); // yeni bir yol başlat
ctx.moveTo(100, 200); // başlangıç noktası

ctx.lineTo(200, 300); // çizgi son noktası
ctx.lineTo(150, 200); // çizgi son noktası
ctx.closePath(); // yolu kapat

ctx.lineWidth = 15; // çizgi kalınlığı
ctx.strokeStyle = "#280d8a";
ctx.stroke();
ctx.fillStyle = "gold";
ctx.fill();

ctx.beginPath();
// arc(x,y, radius, startAngle, endAngle);
ctx.arc(400, 250, 50, 0, Math.PI * 2);
ctx.fillStyle = "crimson";
ctx.fill();
ctx.stroke();

let gradient = ctx.createLinearGradient(0, 0, canvas.width, 0);
gradient.addColorStop(0, "white");
gradient.addColorStop(1, "blue");
ctx.fillStyle = gradient;
ctx.fillRect(50, 10, 200, 30);
*/

ctx.font = "35px Arial";
ctx.fillStyle = "gold";
ctx.textAlign = "center";
ctx.fillText("Merhaba Dünya!", canvas.width / 2, 50);

ctx.strokeStyle = "gold";
ctx.lineWidth = 2;
ctx.strokeText("Yan Yazı", 400, 100);
const img = new Image();
img.src =
  "https://platform.theverge.com/wp-content/uploads/sites/2/chorus/uploads/chorus_asset/file/24510842/john_wick_chapter_4_JW4_Unit_211027_00134_R2_rgb.jpeg?quality=90&strip=all&crop=19.583333333333%2C0%2C60.833333333333%2C100&w=2400";

img.onload = function () {
  ctx.drawImage(img, 50, 310, 400, 200);
  console.log("Resim yüklendi ve çizildi.");
};
