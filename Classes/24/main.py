from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def search_wikipedia(query):
    driver.get(f"https://ru.wikipedia.org/wiki/{query}")
    time.sleep(2)  # Даем время загрузиться странице

def list_paragraphs():
    paragraphs = driver.find_elements(By.TAG_NAME, "p")
    for i, paragraph in enumerate(paragraphs):
        print(f"Параграф {i + 1}: {paragraph.text}\n")

def list_links():
    links = driver.find_elements(By.XPATH, "//div[@id='bodyContent']//a[@href]")
    valid_links = [link for link in links if not link.get_attribute('href').startswith('#')]
    for i, link in enumerate(valid_links):
        print(f"{i + 1}: {link.text} - {link.get_attribute('href')}")
    return valid_links

def navigate_to_link(links, choice):
    href = links[choice - 1].get_attribute('href')
    driver.get(href)
    time.sleep(2)  # Даем время загрузиться странице

def main():
    global driver
    driver = webdriver.Chrome()  # Убедитесь, что путь к chromedriver указан правильно
    while True:
        query = input("Введите запрос для поиска в Википедии (или 'выход' для завершения): ")
        if query.lower() == 'выход':
            break
        search_wikipedia(query)
        while True:
            action = input("Выберите действие: 1 - Листать параграфы, 2 - Перейти на другую страницу, 3 - Выход: ")
            if action == '1':
                list_paragraphs()
            elif action == '2':
                links = list_links()
                if links:
                    choice = int(input("Введите номер ссылки для перехода: "))
                    if 1 <= choice <= len(links):
                        navigate_to_link(links, choice)
                    else:
                        print("Неверный номер ссылки.")
                else:
                    print("На этой странице нет доступных ссылок для перехода.")
            elif action == '3':
                break
            else:
                print("Неверный выбор действия.")
    driver.quit()

if __name__ == "__main__":
    main()