function veriGetir() {
  const linkedin = "https://www.linkedin.com/company/apple/";
  const url =
    "https://fresh-linkedin-profile-data.p.rapidapi.com/get-company-by-linkedinurl?linkedin_url=" +
    encodeURIComponent(linkedin) +
    "&country=us";

  fetch(url, {
    method: "GET",
    headers: {
      "x-rapidapi-key": "dec0e8b660msh7d6e4decaac2accp15831bjsnb2b210d83cc8",
      "x-rapidapi-host": "fresh-linkedin-profile-data.p.rapidapi.com",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      const liste = document.getElementById("liste");
      liste.innerHTML = "";

      const li = document.createElement("li");
      li.textContent = JSON.stringify(data);
      liste.appendChild(li);
    })
    .catch((error) => {
      console.log("Hata oluştu:", error);
    });
}
