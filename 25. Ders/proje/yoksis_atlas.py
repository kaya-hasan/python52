import requests
from bs4 import BeautifulSoup
from googletrans import Translator
import asyncio

translator = Translator()


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

            async def translate_text():
                async with Translator() as translator:
                    result = await translator.translate(uni_name, src='tr', dest='en')
                    return result
            uni_name_en = asyncio.run(translate_text())
            university_data.append({
                "id": data_id,
                "name": uni_name,
                "name_en": uni_name_en.text
            })
        return university_data


def save_to_txt(data):
    with open('university_data.txt', 'w', encoding='utf-8') as file:
        file.write("Id, Name\n")
        for uni in data:
            file.write(f"{uni['id']}, {uni['name']}, {uni['name_en']}\n")


url = "https://yokatlas.yok.gov.tr/universite.php"
university_data = get_university_data(url)
print(university_data)

for uni in university_data:
    print(f"ID: {uni['id']}, Name: {uni['name']}")

save_to_txt(university_data)
