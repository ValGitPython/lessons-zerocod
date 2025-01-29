import requests
import pprint

# Отправляем GET-запрос к API GitHub для поиска репозиториев с кодом HTML
response = requests.get('https://api.github.com/search/repositories', params={'q': 'html'})

# Распечатываем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Распечатываем содержимое ответа в формате JSON
print("Содержимое ответа:")
pprint.pprint(response.json())