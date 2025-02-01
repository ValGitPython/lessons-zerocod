import requests
from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator

# Функция для получения случайного английского слова и его определения
def get_english_words():
    url = "https://randomword.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен
        soup = BeautifulSoup(response.content, "html.parser")
        english_word = soup.find("div", id="random_word").text.strip()
        word_definition = soup.find("div", id="random_word_definition").text.strip()
        return {
            "english_word": english_word,
            "word_definition": word_definition
        }
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None

# Функция для перевода текста на русский язык
def translate_to_russian(text):
    try:
        translation = GoogleTranslator(source='en', target='ru').translate(text)
        return translation
    except Exception as e:
        print(f"Ошибка при переводе: {e}")
        return text  # Возвращаем оригинальный текст в случае ошибки

# Основная функция игры
def word_game():
    print("Добро пожаловать в игру!")
    while True:
        word_dict = get_english_words()
        if not word_dict:
            print("Не удалось получить слово. Попробуйте позже.")
            break

        # Переводим слово и определение
        russian_word = translate_to_russian(word_dict["english_word"])
        russian_definition = translate_to_russian(word_dict["word_definition"])

        # Игровой процесс
        print(f"Значение слова - {russian_definition}")
        user_guess = input("Что это за слово? ").strip().lower()

        # Проверка ответа
        if user_guess == russian_word.lower():
            print("Все верно!")
        else:
            print(f"Ответ неверный. Было загадано слово: {russian_word}")

        # Предложение сыграть ещё раз
        play_again = input("Хотите сыграть еще раз? (y/n): ").strip().lower()
        if play_again != "y":
            print("Спасибо за игру!")
            break

# Запуск игры
if __name__ == "__main__":
    word_game()