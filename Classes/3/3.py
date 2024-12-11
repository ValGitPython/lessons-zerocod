def get_string(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:  # Проверяем, что строка не пустая
            return user_input
        print("Ошибка! Строка не может быть пустой. Попробуйте снова.")

def main():
    print("Программа для конкатенации (объединения) двух строк")
    print("-" * 50)
    
    # Получаем строки с проверкой
    string1 = get_string("Введите первую строку: ")
    string2 = get_string("Введите вторую строку: ")
    
    # Выполняем конкатенацию разными способами
    print("\nРезультаты конкатенации:")
    print(f"1. Простое объединение: {string1 + string2}")
    print(f"2. Через пробел: {string1 + ' ' + string2}")
    print(f"3. Через запятую: {string1 + ', ' + string2}")
    
    # Спрашиваем, хочет ли пользователь попробовать еще раз
    while True:
        again = input("\nХотите попробовать еще раз? (да/нет): ").lower()
        if again in ['да', 'нет']:
            break
        print("Пожалуйста, введите 'да' или 'нет'")
    
    if again == 'да':
        print("\n" + "=" * 50 + "\n")
        main()

if __name__ == "__main__":
    main()
