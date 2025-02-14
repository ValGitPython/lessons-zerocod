import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt

# URL страницы с диванами
url = 'https://www.divan.ru/category/divany-i-kresla'

# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Запрос к сайту
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

# Сбор данных
sofas = []
for item in soup.find_all('div', class_='lsooF'):  # Уточните класс, если он изменился
    # Извлечение названия дивана
    name_element = item.find('span', itemprop='name')
    if name_element:
        name = name_element.text.strip()
    else:
        name = "Название не указано"

    # Извлечение цены
    price_element = item.find('meta', itemprop='price')
    if price_element:
        price = price_element.get('content')  # Получаем значение атрибута content
        try:
            # Преобразуем цену в число
            price = int(price)
            sofas.append({'Название': name, 'Цена': price})
        except ValueError:
            print(f"Ошибка преобразования цены для дивана: {name}")
    else:
        print(f"Цена отсутствует для дивана: {name}")

# Создаем DataFrame
df = pd.DataFrame(sofas)

# Сохраняем в CSV
df.to_csv('sofas_prices.csv', index=False)

# Выводим среднюю цену
if not df.empty:
    average_price = df['Цена'].mean()
    print(f"Средняя цена на диваны: {average_price:.2f} ₽")

    # Построение гистограммы
    plt.hist(df['Цена'], bins=20, edgecolor='black')
    plt.title('Гистограмма цен на диваны')
    plt.xlabel('Цена (₽)')
    plt.ylabel('Количество')
    plt.grid(True)
    plt.show()
else:
    print("Нет данных для построения гистограммы.")