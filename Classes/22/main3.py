# Создаем словарь с данными для отправки
import requests

data = {
    'title': 'foo',
    'body': 'bar',
    'userId': 1
}

# Отправляем POST-запрос с данными
response = requests.post('https://jsonplaceholder.typicode.com/posts', json=data)

# Распечатываем статус-код ответа
print("Статус-код ответа:", response.status_code)

# Распечатываем содержимое ответа
print("Содержимое ответа:")
print(response.json())