# request -> http istekleri yapmak için kullanılır
# beautifulsoup -> html sayfalarını parse etmek için kullanılır
import requests
from bs4 import BeautifulSoup

url = "https://selcukakarin.github.io/"

response = requests.get(url)

html_content = response.content
soup = BeautifulSoup(html_content, "html.parser")
# print(soup.prettify())

# print(soup.find_all("a"))

# for i in soup.find_all("a"):
#     print(i.get("href"))

# for i in soup.find_all("a"):
#     print(i.text)

for i in soup.find_all("div", {"class": "wave"}):
    print(i)
