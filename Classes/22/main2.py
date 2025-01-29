# Отправляем GET-запрос с параметром userId=1
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})

# Распечатываем полученные записи
print("Полученные записи:")
print(response.json())