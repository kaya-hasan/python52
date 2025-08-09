import requests
from bs4 import BeautifulSoup


def get_university_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        university_data = []
        ul_tag = soup.find('ul', {"id": "myUl"})
        li_tags = ul_tag.find_all("li", {"class": "unilist"})

        for li_tag in li_tags:
            data_id = li_tag.find("a", href=True)["data-id"]
            uni_name = li_tag.find("h3", class_="baslik").text.strip()
            university_data.append({
                "id": data_id,
                "name": uni_name
            })
        return university_data


url = "https://yokatlas.yok.gov.tr/universite.php"
university_data = get_university_data(url)
print(university_data)

for uni in university_data:
    print(f"ID: {uni['id']}, Name: {uni['name']}")
