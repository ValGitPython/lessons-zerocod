
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализируем браузер
driver = webdriver.Chrome()

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.divan.ru/vladikavkaz/category/divany?in_stock=1"

# Открываем веб-страницу
driver.get(url)

# Задаём явное ожидание, чтобы веб-страница успела прогрузиться
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, '.lsooF')))

# Находим все карточки с товарами
vacancies = driver.find_elements(By.CSS_SELECTOR, '.lsooF')

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Перебираем коллекцию товаров
for vacancy in vacancies:
    try:
        # Находим названия товара
        name = vacancy.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct>span').text
        # Находим цены
        price = vacancy.find_element(By.CSS_SELECTOR, 'span.ui-LD-ZU.KIkOH').text
        # Находим ссылку с помощью атрибута 'href'
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.ui-GPFV8.qUioe.ProductName.ActiveProduct').get_attribute('href')
    except Exception as e:
        print("Произошла ошибка при парсинге:", e)
        continue
    # Вносим найденную информацию в список
    parsed_data.append([name, price, link])

# Закрываем подключение браузера
driver.quit()

# Записываем данные в CSV файл
with open("divan.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название модели', 'Цена', 'Ссылка на модель'])
    writer.writerows(parsed_data)
