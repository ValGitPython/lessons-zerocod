def get_name():
    while True:
        name = input("Введите ваше имя: ").strip()
        if name and name.replace(" ", "").isalpha():  # Проверяем, что имя содержит только буквы
            return name.title()  # Возвращаем имя с заглавной буквы
        print("Ошибка! Имя должно содержать только буквы.")

def get_age():
    while True:
        try:
            age = int(input("Введите ваш возраст: "))
            if 0 <= age <= 150:  # Проверяем, что возраст в разумных пределах
                return age
            print("Ошибка! Возраст должен быть от 0 до 150 лет.")
        except ValueError:
            print("Ошибка! Пожалуйста, введите целое число.")

def main():
    # Получаем имя и возраст с проверкой
    name = get_name()
    age = get_age()
    
    # Выводим приветствие
    print(f"\nПривет, {name}! Тебе {age} {'лет' if age % 10 in [0, 5, 6, 7, 8, 9] or age in range(11, 15) else 'года' if age % 10 in [2, 3, 4] else 'год' if age % 10 == 1 and age != 11 else 'лет'}.")
    
    # Дополнительные расчеты
    months = age * 12
    days = age * 365
    hours = days * 24
    
    print(f"\nЭто примерно:")
    print(f"• {months:,} месяцев".replace(",", " "))
    print(f"• {days:,} дней".replace(",", " "))
    print(f"• {hours:,} часов".replace(",", " "))

if __name__ == "__main__":
    main()
