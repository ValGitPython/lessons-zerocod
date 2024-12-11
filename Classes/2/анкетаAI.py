# -*- coding: utf-8 -*-

def get_valid_name():
    while True:
        name = input("Как тебя зовут? ").strip()
        if name and name.replace(" ", "").isalpha():  # Проверка, что имя состоит только из букв
            return name.title()  # Возвращает имя с заглавной буквы
        print("Пожалуйста, введите корректное имя (только буквы)!")

def get_valid_age():
    while True:
        try:
            age = input("Сколько тебе лет? ")
            age = int(age)
            if age < 0:
                print("Возраст не может быть отрицательным!")
                continue
            if age > 120:
                print("Пожалуйста, введите реальный возраст!")
                continue
            return age
        except ValueError:
            print("Пожалуйста, введите число!")

def determine_status(age):
    if age <= 3:
        return "Ты совсем малыш!"
    elif age <= 7:
        return "Ты ходишь в садик!"
    elif age <= 18:
        return "Ты ходишь в школу!"
    elif age <= 23:
        return "Ты студент!"
    else:
        return "Да ты уже взрослый!"

def main():
    print("Здравствуй!")
    
    try:
        # Получаем имя
        name = get_valid_name()
        print(f"Приятно познакомиться, {name}!")

        # Получаем возраст
        age = get_valid_age()
        
        # Определяем статус и выводим сообщение
        status = determine_status(age)
        print(status)

        # Дополнительная информация в зависимости от возраста
        if age < 18:
            print(f"Тебе осталось {18 - age} лет до совершеннолетия!")
        
    except KeyboardInterrupt:
        print("\nПрограмма прервана пользователем. До свидания!")
    except Exception as e:
        print(f"\nПроизошла ошибка: {e}")
        print("Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()