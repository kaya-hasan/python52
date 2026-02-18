const input = document.getElementById("imageInput");
const preview = document.getElementById("preview");
const alertBox = document.getElementById("alertBox");
const form = document.getElementById("myForm");
const nameInput = document.getElementById("nameInput");
const surNameInput = document.getElementById("surNameInput");
const message = document.getElementById("message");
const removeImage = document.getElementById("removeImage");
input.addEventListener("change", () => {
  const file = input.files[0];
  preview.src = URL.createObjectURL(file);
  preview.style.display = "block";

  alertBox.style.display = "block";
  setTimeout(() => {
    alertBox.style.display = "none";
  }, 2000);
});

form.addEventListener("submit", (event) => {
  event.preventDefault();
  if (nameInput.value == "") {
    message.innerText = "Lütfen adinizi girin !";
    message.style.color = "red";
  }
  if (surNameInput.value == "") {
    message.innerText = "Lütfen soyadinizi girin !";
    message.style.color = "red";
  } else {
    message.innerText = "Form başarıyla gönderildi !";
    message.style.color = "green";
  }
});
removeImage.addEventListener("click", () => {
  preview.src = "";
  preview.style.display = "none";
  input.value = "";
});
