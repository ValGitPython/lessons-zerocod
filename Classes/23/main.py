from bs4 import BeautifulSoup
import requests

url = "https://asanaonline.ru/asana/"
response = requests.get(url)
html = response.text

soup = BeautifulSoup(html, "html.parser")

#Создадим отдельную переменную text, куда будут сохраняться все цитаты
text = soup.find("img")
print(text)
# links = soup.find_all("a")
# for link in links:
#     print(link)