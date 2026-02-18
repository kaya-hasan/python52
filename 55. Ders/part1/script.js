const input = document.getElementById("taskInput");
const button = document.getElementById("addBtn");
const list = document.getElementById("taskList");
const deleteButton = document.getElementById("deleteBtn");

button.addEventListener("click", function () {
  const text = input.value;

  if (text === "") {
    alert("Lütfen bir görev girin");
    return;
  }
  const li = document.createElement("li");
  li.textContent = text;
  list.appendChild(li);
  input.value = "";
});

deleteButton.addEventListener("click", function () {
  list.innerHTML = "";
});
